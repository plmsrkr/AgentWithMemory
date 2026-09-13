# AgentWithMemory: Margin Analysis POC

This repository provides a minimal Proof of Concept (POC) for an autonomous agent capable of performing margin analysis. The project demonstrates the integration of skill-based prompt injection and direct tool execution to interact with BigQuery (BQ).

### Key Features:
*   **Skill Prompt Injection:** Leverages modular skill definitions injected directly into the agent's context to dynamically expand its capabilities without modifying core logic.
*   **BigQuery Integration:** Implements a streamlined tool-calling interface that allows the agent to execute SQL queries against BigQuery, retrieve financial or operational datasets, and process the results.
*   **Lightweight Architecture:** Built as a minimal POC to showcase the efficacy of using tool-use patterns for data-driven agentic decision-making.

### Getting Started:
1.  **Configure Environment:** Ensure your Google Cloud credentials are set up for BigQuery access.
2.  **Tool Setup:** Review the `margin_tool.py` script to understand how BQ queries are structured and executed.
3.  **Run Agent:** Utilize the `agent.py` entry point to trigger the margin analysis workflow, where the agent will evaluate the injected skills to formulate and run the necessary BQ operations.
