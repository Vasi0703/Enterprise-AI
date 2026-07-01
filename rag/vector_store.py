from langchain_chroma import Chroma


class VectorStoreManager:

    def __init__(self, embeddings):

        self.embeddings = embeddings

    def create(self, chunks):

        vector_store = Chroma.from_documents(

            documents=chunks,

            embedding=self.embeddings,

            persist_directory="data/chroma_db"

        )

        return vector_store