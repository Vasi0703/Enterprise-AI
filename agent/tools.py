from langchain_core.tools import tool

from rag.rag_pipeline import RAGPipeline


# Construim pipeline-ul o singură dată
rag_pipeline = RAGPipeline("data/pdfs/hr.pdf")
rag_pipeline.build()


@tool
def calculator(expression: str) -> str:
    """
    Evaluates a mathematical expression.
    """
    try:
        return str(eval(expression))
    except Exception:
        return "Invalid mathematical expression."


@tool
def search_company_policy(question: str) -> str:
    """
    Search ONLY the internal HR policy documents.

    Use this tool ONLY if the user's question is specifically about:

    - HR policies
    - employee benefits
    - annual leave
    - sick leave
    - working hours
    - remote work
    - company regulations

    DO NOT use this tool for:

    - greetings
    - general conversation
    - mathematics
    - programming
    - general knowledge
    """

    response = rag_pipeline.ask(question)

    return response.content