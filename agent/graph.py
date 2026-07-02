from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver

from agent.state import AgentState
from agent.nodes import chatbot
from agent.tools import calculator, search_company_policy


class AgentGraph:

    def __init__(self):

        graph = StateGraph(AgentState)

        memory = MemorySaver()

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

        graph.add_edge(
            START,
            "chatbot"
        )

        graph.add_conditional_edges(
            "chatbot",
            tools_condition
        )

        graph.add_edge(
            "tools",
            "chatbot"
        )

        self.graph = graph.compile(
            checkpointer=memory
        )

    def invoke(self, messages, config):

        return self.graph.invoke(
            {
                "messages": messages
            },
            config=config
        )