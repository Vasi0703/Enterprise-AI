from rag.loader import DocumentLoader
from rag.splitter import DocumentSplitter
from rag.embeddings import EmbeddingManager
from rag.vector_store import VectorStoreManager
from rag.retriever import RetrieverManager
from rag.rag_chain import RAGChain

from utils.logger import logger


class RAGPipeline:

    def __init__(self, pdf_path: str):

        self.pdf_path = pdf_path

        self.rag_chain = None

    def build(self):

        logger.info("Loading PDF...")

        loader = DocumentLoader()

        documents = loader.load(self.pdf_path)

        logger.info(f"Loaded {len(documents)} pages.")

        splitter = DocumentSplitter()

        chunks = splitter.split(documents)

        logger.info(f"Created {len(chunks)} chunks.")

        embeddings = EmbeddingManager()

        logger.info("Creating Vector Store...")

        vector_store = VectorStoreManager(
            embeddings.get_embeddings()
        ).create(chunks)

        logger.info("Vector Store created.")

        retriever = RetrieverManager(
            vector_store
        ).get_retriever()

        logger.info("Retriever initialized.")

        self.rag_chain = RAGChain(retriever)

        logger.info("RAG Pipeline ready.")

    def ask(self, question: str):

        logger.info(f"User question: {question}")

        response = self.rag_chain.ask(question)

        logger.info("Response generated successfully.")

        return response