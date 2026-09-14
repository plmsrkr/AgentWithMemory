from pathlib import Path
import yaml


BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_PATH = BASE_DIR / "config" / "capabilities.yaml"


with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

CAPABILITIES = config["capabilities"]


def get_capability(name: str) -> dict:
    if name not in CAPABILITIES:
        raise ValueError(
            f"Unknown capability: {name}. "
            f"Available: {list(CAPABILITIES.keys())}"
        )

    return CAPABILITIES[name]