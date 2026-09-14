from pathlib import Path
import yaml


BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_PATH = BASE_DIR / "config" / "skills.yaml"
SKILLS_DIR = BASE_DIR / "skills"


with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)


SKILLS = config["skills"]


def get_skill(skill_name: str) -> dict:
    """
    Resolve a logical skill name into its actual instruction content.
    """

    if skill_name not in SKILLS:
        return {
            "status": "not_found",
            "skill": skill_name,
            "available_skills": list(SKILLS.keys())
        }

    skill_config = SKILLS[skill_name]

    file_path = SKILLS_DIR / skill_config["file"]

    instruction = file_path.read_text(encoding="utf-8")

    return {
        "status": "success",
        "skill": skill_name,
        "description": skill_config["description"],
        "instruction": instruction
    }