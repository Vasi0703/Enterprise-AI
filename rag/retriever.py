class RetrieverManager:

    def __init__(self, vector_store):

        self.vector_store = vector_store

    def get_retriever(self):

        return self.vector_store.as_retriever(

            search_type="mmr",

            search_kwargs={
                "k": 5,
                "fetch_k": 20
            }
        )