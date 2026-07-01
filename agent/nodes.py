from agent.state import AgentState
from agent.tools import calculator, search_company_policy
from llm.llm_manager import LLMManager


llm = LLMManager().get_llm().bind_tools(
    [
        calculator,
        search_company_policy
    ]
)


def chatbot(state: AgentState):

    response = llm.invoke(state["messages"])

    return {
        "messages": [response]
    }