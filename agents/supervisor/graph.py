from langgraph.graph import StateGraph, START, END
from memory.checkpointer import Checkpointer

from agents.supervisor.state import SupervisorState
from agents.supervisor.nodes import (
    route_question,
    route_decision,
    hr_node,
    math_node,
    chat_node
)


class SupervisorGraph:

    def __init__(self):
        graph = StateGraph(SupervisorState)
        memory = Checkpointer().get()

        graph.add_node("router", route_question)
        graph.add_node("hr", hr_node)
        graph.add_node("math", math_node)
        graph.add_node("chat", chat_node)

        graph.add_edge(START, "router")

        graph.add_conditional_edges(
            "router",
            route_decision,
            {
                "hr": "hr",
                "math": "math",
                "chat": "chat"
            }
        )

        graph.add_edge("hr", END)
        graph.add_edge("math", END)
        graph.add_edge("chat", END)

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
