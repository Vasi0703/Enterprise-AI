from agents.math.state import MathState
from agents.math.tools import calculator
from llm.llm_manager import LLMManager


llm = LLMManager().get_llm().bind_tools(
    [calculator]
)


def math_chatbot(state: MathState):
    response = llm.invoke(state["messages"])

    return {
        "messages": [response]
    }
