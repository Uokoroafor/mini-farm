ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}

# COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# WORKDIR /usr/src/app
# COPY uv.lock pyproject.toml ./

# RUN uv sync --frozen

# EXPOSE 3001

# CMD ["uv", "run", ".src/server.py"]

# Set working directory
WORKDIR /usr/src/app

# Install dependencies
COPY uv.lock pyproject.toml ./
RUN uv sync --frozen

# Copy application files
COPY . .

# Use a non-root user
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /usr/src/app
USER appuser

# Expose port
EXPOSE 3001

# Set runtime command
CMD ["uv", "run", "./src/server.py"]