from llm.llm_manager import LLMManager

from prompts.supervisor_prompt import supervisor_prompt

from schemas.route import RouteResponse

from utils.logger import logger
from utils.trace import trace

from agents.supervisor.state import SupervisorState

from agents.hr.graph import HRGraph
from agents.math.graph import MathGraph
from agents.chat.graph import ChatGraph


llm = (
    LLMManager()
    .get_llm()
    .with_structured_output(RouteResponse)
)

routing_chain = supervisor_prompt | llm

hr_graph = HRGraph()
math_graph = MathGraph()
chat_graph = ChatGraph()


def route_question(state: SupervisorState):

    question = state["messages"][-1].content

    trace("SUPERVISOR")

    logger.info("Analyzing user request...")

    response = routing_chain.invoke(
        {
            "question": question
        }
    )

    logger.info(f"Structured Output: {response}")

    route = response.route

    logger.info(f"Selected Agent: {route}")

    return {
        "route": route
    }


def route_decision(state: SupervisorState):

    return state["route"]


def hr_node(state: SupervisorState):

    trace("HR AGENT")
    logger.info("Delegating request to HR Agent...")

    return hr_graph.invoke(
        state["messages"]
    )


def math_node(state: SupervisorState):

    trace("MATH AGENT")
    logger.info("Delegating request to Math Agent...")

    return math_graph.invoke(
        state["messages"]
    )


def chat_node(state: SupervisorState):

    trace("CHAT AGENT")
    logger.info("Delegating request to Chat Agent...")

    return chat_graph.invoke(
        state["messages"]
    )