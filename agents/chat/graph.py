from langgraph.graph import StateGraph, START, END

from agents.chat.state import ChatState
from agents.chat.nodes import chat


class ChatGraph:

    def __init__(self):
        graph = StateGraph(ChatState)

        graph.add_node("chat", chat)

        graph.add_edge(START, "chat")
        graph.add_edge("chat", END)

        self.graph = graph.compile()

    def invoke(self, messages):
        return self.graph.invoke(
            {
                "messages": messages
            }
        )
