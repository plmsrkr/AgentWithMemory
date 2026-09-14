from ..registry.skill_registry import get_skill


def load_skill_instruction(skill_name: str) -> dict:
    """
    Load the methodology for an analytical skill.

    Use this tool only when reasoning or analytical methodology
    is required.

    Examples of skill names:
    - margin_analysis
    - forecast_variance
    - root_cause_analysis
    """

    print(
        f">>> SKILL REQUESTED: {skill_name}",
        flush=True
    )

    result = get_skill(skill_name)

    print(
        f">>> SKILL LOADED: {result.get('status')}",
        flush=True
    )

    return result