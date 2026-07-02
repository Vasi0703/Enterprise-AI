from langchain_core.tools import tool

from config.settings import PDF_PATH
from rag.rag_pipeline import RAGPipeline


_rag_pipeline = None


def get_rag_pipeline():
    global _rag_pipeline

    if _rag_pipeline is None:
        _rag_pipeline = RAGPipeline(PDF_PATH)
        _rag_pipeline.build()

    return _rag_pipeline


@tool
def search_company_policy(question: str) -> str:
    """
    Search the internal HR policy documents.
    Use this tool for HR policies, annual leave, sick leave, remote work,
    working hours, employee rules, and company regulations.
    """
    response = get_rag_pipeline().ask(question)

    return response.content
