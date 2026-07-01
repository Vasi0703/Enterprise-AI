from langchain_core.messages import HumanMessage

from agent.graph import AgentGraph


class EnterpriseAgent:

    def __init__(self):

        self.graph = AgentGraph()

    def ask(self, question: str):

        response = self.graph.invoke(

            [

                HumanMessage(content=question)

            ]

        )

        return response["messages"][-1]