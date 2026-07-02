from langgraph.graph import StateGraph, START, END

from agents.hr.state import HRState
from agents.hr.nodes import answer_hr_question


class HRGraph:

    def __init__(self):
        graph = StateGraph(HRState)

        graph.add_node("answer_hr_question", answer_hr_question)

        graph.add_edge(START, "answer_hr_question")
        graph.add_edge("answer_hr_question", END)

        self.graph = graph.compile()

    def invoke(self, messages):
        return self.graph.invoke(
            {
                "messages": messages
            }
        )
