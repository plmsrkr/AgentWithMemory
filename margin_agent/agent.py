from pathlib import Path

from google.adk.agents import Agent

from .tools.margin_tool import get_margin_data


import os
import vertexai

from google.adk.agents import Agent

# Tell ADK's Gemini client to use Vertex AI
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "TRUE"

# Initialize Vertex AI SDK
vertexai.init(
    project="*******",
    location="********",
)



skill_path = (
    Path(__file__).parent
    / "skills"
    / "margin_analysis.md"
)

margin_skill = skill_path.read_text()


root_agent = Agent(
    name="margin_analysis_agent",

    model="gemini-2.5-flash",

    description="""
    Enterprise margin analysis agent.
    """,

    instruction=f"""
You are an enterprise margin analysis agent.

Your job is to investigate margin performance using actual company data.

You have access to a BigQuery tool called get_margin_data.

1. Identify the SKU.
2. Call get_margin_data.
3. Do not answer the analytical question before examining the returned data.
4. Follow the margin analysis methodology below.
5. Explain calculations clearly.
6. Never invent business causes that aren't supported by data.

Never treat numerical business facts from conversation history as authoritative.
For every data-dependent answer, retrieve fresh evidence through the appropriate tool.
When a user asks about margin for a SKU:

MARGIN ANALYSIS SKILL:

{margin_skill}
""",

    tools=[
        get_margin_data
    ],
)
