FROM python:3.12-slim

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy dependency definitions first
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-dev

# Copy agent code
COPY margin_agent ./margin_agent

EXPOSE 8000

CMD ["uv", "run", "adk", "api_server", "--host", "0.0.0.0", "--port", "8000"]