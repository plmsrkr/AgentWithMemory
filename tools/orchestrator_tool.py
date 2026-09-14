import inspect
import json

from ..registry.capability_registry import get_capability
from ..registry.tool_registry import TOOL_REGISTRY
from ..registry.skill_registry import get_skill


def _call_tool(tool, entities: dict):
    """
    Pass only arguments that the target function accepts.
    """

    signature = inspect.signature(tool)

    supported_args = {
        name: value
        for name, value in entities.items()
        if name in signature.parameters
    }

    return tool(**supported_args)


def execute_plan(
    entities: dict,
    data: list[str],
    reasoning: list[str],
    statistics: list[str],
    web: list[str],
    execution_order: list[str],
) -> dict:
    """
    Execute the complete capability plan for the current request.

    This is the ONLY orchestration tool exposed to Groot.

    Args:
        entities:
            Resolved entities and filters.
            Example:
            {
                "sku": "SKU123",
                "start_year": 2025,
                "end_year": 2026
            }

        data:
            Data capabilities required.
            Example:
            ["margin_data", "forecast_data"]

        reasoning:
            Reasoning skills required.
            Example:
            ["margin_analysis"]

        statistics:
            Statistical capabilities required.

        web:
            Web capabilities or external-context requests.

        execution_order:
            Requested execution sequence.

    Returns:
        A single evidence bundle containing the results of
        all executed capabilities and loaded skills.
    """

    plan = {
        "entities": entities,
        "data": data,
        "reasoning": reasoning,
        "statistics": statistics,
        "web": web,
        "execution_order": execution_order,
    }

    print("\n" + "=" * 70, flush=True)
    print("EXECUTION PLAN", flush=True)
    print(json.dumps(plan, indent=2, default=str), flush=True)
    print("=" * 70 + "\n", flush=True)

    evidence = {}
    skills = {}
    stats_results = {}
    web_results = {}

    # -----------------------------
    # DATA
    # -----------------------------

    for capability_name in data:

        capability = get_capability(capability_name)

        if capability["type"] != "data":
            raise ValueError(
                f"{capability_name} is not a data capability"
            )

        tool_name = capability["tool"]

        tool = TOOL_REGISTRY[tool_name]

        print(
            f">>> EXECUTING DATA CAPABILITY: {capability_name}",
            flush=True
        )

        evidence[capability_name] = _call_tool(
            tool,
            entities
        )

    # -----------------------------
    # STATISTICS
    # -----------------------------

    for capability_name in statistics:

        capability = get_capability(capability_name)

        if capability["type"] != "statistics":
            continue

        tool_name = capability["tool"]
        tool = TOOL_REGISTRY[tool_name]

        print(
            f">>> EXECUTING STATISTICS: {capability_name}",
            flush=True
        )

        # For the POC leave this generic.
        # Later pass explicit evidence inputs.
        stats_results[capability_name] = {
            "status": "not_implemented_yet"
        }

    # -----------------------------
    # WEB
    # -----------------------------

    for item in web:

        print(
            f">>> EXECUTING WEB REQUEST: {item}",
            flush=True
        )

        if "web_search" in TOOL_REGISTRY:
            web_results[item] = TOOL_REGISTRY[
                "web_search"
            ](query=item)

    # -----------------------------
    # REASONING SKILLS
    # -----------------------------

    for skill_name in reasoning:

        capability = get_capability(skill_name)

        if capability["type"] != "reasoning":
            raise ValueError(
                f"{skill_name} is not a reasoning capability"
            )

        registered_skill_name = capability["skill"]

        print(
            f">>> LOADING SKILL: {registered_skill_name}",
            flush=True
        )

        skills[skill_name] = get_skill(
            registered_skill_name
        )

    result = {
        "status": "success",
        "plan": plan,
        "evidence": evidence,
        "statistics": stats_results,
        "web": web_results,
        "skills": skills,
    }

    print("\n" + "=" * 70, flush=True)
    print("EVIDENCE BUNDLE", flush=True)
    print(json.dumps(result, indent=2, default=str), flush=True)
    print("=" * 70 + "\n", flush=True)

    return result