from langchain_core.messages import AIMessage

from llm.llm_manager import LLMManager
from agent.state import AgentState


llm = LLMManager()


def chatbot(state: AgentState):

    response = llm.ask(state["messages"])

    print("\n========== LLM RESPONSE ==========\n")
    print(response)
    print("\n==================================\n")

    return {
        "messages": [
            response
        ]
    }