from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition

from agent.state import AgentState
from agent.nodes import chatbot
from agent.tools import calculator, search_company_policy


class AgentGraph:

    def __init__(self):

        graph = StateGraph(AgentState)

        # Nodes
        graph.add_node("chatbot", chatbot)

        graph.add_node(
            "tools",
            ToolNode(
                [
                    calculator,
                    search_company_policy
                ]
                    )
        )

        # Start
        graph.add_edge(
            START,
            "chatbot"
        )

        # Dacă LLM cere un tool -> mergem în ToolNode
        # Dacă nu -> END automat
        graph.add_conditional_edges(
            "chatbot",
            tools_condition
        )

        # După executarea tool-ului revenim la chatbot
        graph.add_edge(
            "tools",
            "chatbot"
        )

        self.graph = graph.compile()

    def invoke(self, messages):

        return self.graph.invoke(
            {
                "messages": messages
            }
        )