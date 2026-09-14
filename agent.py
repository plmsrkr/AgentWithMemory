from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

import os
import yaml
import vertexai

from google.adk.agents import Agent

from .tools.orchestrator_tool import execute_plan


os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "TRUE"


BASE_DIR = Path(__file__).resolve().parent


vertexai.init(
    project="****",
    location="****",
)


# Load root prompt
with open(
    BASE_DIR / "config" / "prompts.yaml",
    "r",
    encoding="utf-8",
) as f:
    prompt_config = yaml.safe_load(f)


# Runtime date
now = datetime.now()



current_date_context = f"""
CURRENT DATE CONTEXT

Current date: {now.date().isoformat()}
Current year: {now.year}
Previous year: {now.year - 1}

Resolve relative periods using this date.
"""


root_agent = Agent(
    name="Groot",

    model="gemini-2.5-flash",

    description=prompt_config[
        "root_agent"
    ]["description"],

    instruction=(
        prompt_config[
            "root_agent"
        ]["instruction"]
        + "\n"
        + current_date_context
    ),

    tools=[
        execute_plan
    ],
)
