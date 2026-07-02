from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition

from agents.math.state import MathState
from agents.math.nodes import math_chatbot
from agents.math.tools import calculator


class MathGraph:

    def __init__(self):
        graph = StateGraph(MathState)

        graph.add_node("math_chatbot", math_chatbot)
        graph.add_node("tools", ToolNode([calculator]))

        graph.add_edge(START, "math_chatbot")

        graph.add_conditional_edges(
            "math_chatbot",
            tools_condition
        )

        graph.add_edge("tools", "math_chatbot")

        self.graph = graph.compile()

    def invoke(self, messages):
        return self.graph.invoke(
            {
                "messages": messages
            }
        )
