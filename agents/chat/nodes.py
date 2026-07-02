from agents.chat.state import ChatState
from llm.llm_manager import LLMManager


llm = LLMManager().get_llm()


def chat(state: ChatState):
    response = llm.invoke(state["messages"])

    return {
        "messages": [response]
    }
