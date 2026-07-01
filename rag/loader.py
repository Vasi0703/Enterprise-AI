from langchain_community.document_loaders import PyPDFLoader


class DocumentLoader:

    def load(self, path: str):

        loader = PyPDFLoader(path)

        documents = loader.load()

        return documents