from typing import List, Tuple, Literal
from pydantic import BaseModel
import ollama
import numpy as np
import faiss


class Embedding(BaseModel):
    id: str
    embedding: List[float]
    document: str


def embed(documents: List[str], model: str = "nomic-embed-text") -> List[Embedding]:
    embeddings = []
    for i, document in enumerate(documents):
        response = ollama.embeddings(model=model, prompt=document)
        embedding = response["embedding"]
        embeddings.append(Embedding(id=str(i), embedding=embedding, document=document))
    return embeddings


class FAISSVectorIndex:
    def __init__(
        self,
        dimension: int,
        method: Literal["l2", "inner_product", "cosine"] = "l2",
        use_ivf: bool = False,
        nlist: int = 100,
    ):
        self.dimension = dimension
        self.method = method
        self.use_ivf = use_ivf
        self.nlist = nlist
        self.embeddings = []

        if method == "l2":
            if use_ivf:
                quantizer = faiss.IndexFlatL2(self.dimension)
                self.index = faiss.IndexIVFFlat(quantizer, self.dimension, nlist)
            else:
                self.index = faiss.IndexFlatL2(self.dimension)
        elif method in ["inner_product", "cosine"]:
            if use_ivf:
                quantizer = faiss.IndexFlatIP(self.dimension)
                self.index = faiss.IndexIVFFlat(
                    quantizer, self.dimension, nlist, faiss.METRIC_INNER_PRODUCT
                )
            else:
                self.index = faiss.IndexFlatIP(self.dimension)

        self.is_trained = not use_ivf  # Flat indexes don't need training

    def add_vectors(self, new_embeddings: List[Embedding], batch_size: int = 10000):
        for i in range(0, len(new_embeddings), batch_size):
            batch = new_embeddings[i : i + batch_size]
            vectors = np.array([e.embedding for e in batch]).astype("float32")

            if vectors.shape[1] != self.dimension:
                raise ValueError(f"Vectors must have dimension {self.dimension}")

            if self.method == "cosine":
                faiss.normalize_L2(vectors)

            if not self.is_trained:
                self.index.train(vectors)
                self.is_trained = True

            self.index.add(vectors)
            self.embeddings.extend(batch)

    def remove_vectors(self, ids_to_remove: List[str]):
        mask = np.ones(len(self.embeddings), dtype=bool)
        for id_to_remove in ids_to_remove:
            for i, embedding in enumerate(self.embeddings):
                if embedding.id == id_to_remove:
                    mask[i] = False
                    break

        self.embeddings = [e for i, e in enumerate(self.embeddings) if mask[i]]
        vectors = np.array([e.embedding for e in self.embeddings]).astype("float32")

        if self.method == "cosine":
            faiss.normalize_L2(vectors)

        # Recreate and retrain the index
        self.__init__(self.dimension, self.method, self.use_ivf, self.nlist)
        if vectors.shape[0] > 0:
            self.add_vectors(self.embeddings)

    def search(
        self, query_vector: List[float], k: int = 5
    ) -> Tuple[List[float], List[Embedding]]:
        query_vector = np.array([query_vector]).astype("float32")
        if query_vector.shape[1] != self.dimension:
            raise ValueError(f"Query vector must have dimension {self.dimension}")

        if self.use_ivf:
            self.index.nprobe = min(self.nlist, 10)  # Set nprobe for better recall

        if self.method == "cosine":
            faiss.normalize_L2(query_vector)

        distances, indices = self.index.search(query_vector, k)

        results = [
            (float(dist), self.embeddings[idx])
            for dist, idx in zip(distances[0], indices[0])
        ]

        if self.method == "l2":
            results.sort(key=lambda x: x[0])
        else:
            results.sort(key=lambda x: x[0], reverse=True)

        scores, embeddings = zip(*results)
        return list(scores), list(embeddings)

    def get_num_vectors(self) -> int:
        return self.index.ntotal


def direct_search(
    query: str,
    embeddings=List[Embedding],
    method: Literal["l2", "inner_product", "cosine"] = "l2",
    use_ivf: bool = False,
    nlist: int = 100,
    k: int = 5,
) -> Tuple[List[float], List[Embedding]]:
    """Note: it is inefficient if used with `use_ivf`"""

    indexer = FAISSVectorIndex(
        dimension=768, method=method, use_ivf=use_ivf, nlist=nlist
    )
    indexer.add_vectors(embeddings)
    query_vector = embed([query])[0].embedding
    result = indexer.search(query_vector, k=k)
    return result
