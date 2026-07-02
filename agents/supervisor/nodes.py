import re

from utils.logger import logger
from utils.trace import trace

from agents.supervisor.state import SupervisorState
from agents.hr.graph import HRGraph
from agents.math.graph import MathGraph
from agents.chat.graph import ChatGraph


hr_graph = HRGraph()
math_graph = MathGraph()
chat_graph = ChatGraph()


def route_question(state: SupervisorState):
    question = state["messages"][-1].content.lower()

    trace("SUPERVISOR")
    logger.info("Analyzing user request...")

    hr_keywords = [
        "leave",
        "vacation",
        "holiday",
        "remote",
        "policy",
        "working hours",
        "sick",
        "employee",
        "hr",
        "annual leave",
        "paid leave",
        "personal leave"
    ]

    math_intent = (
        "calculate" in question
        or bool(re.search(r"\d+\s*[+\-*/]\s*\d+", question))
    )

    if math_intent:
        logger.info("Selected Agent: Math Agent")
        return {"route": "math"}

    if any(keyword in question for keyword in hr_keywords):
        logger.info("Selected Agent: HR Agent")
        return {"route": "hr"}

    logger.info("Selected Agent: Chat Agent")
    return {"route": "chat"}


def route_decision(state: SupervisorState):
    return state["route"]


def hr_node(state: SupervisorState):
    result = hr_graph.invoke([
        state["messages"][-1]
    ])

    return {
        "messages": [
            result["messages"][-1]
        ]
    }


def math_node(state: SupervisorState):
    result = math_graph.invoke([
        state["messages"][-1]
    ])

    return {
        "messages": [
            result["messages"][-1]
        ]
    }


def chat_node(state: SupervisorState):
    result = chat_graph.invoke(
        state["messages"]
    )

    return {
        "messages": [
            result["messages"][-1]
        ]
    }
