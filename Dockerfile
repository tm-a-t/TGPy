# check=skip=FromAsCasing
FROM python:3.13-slim as base
WORKDIR /app

FROM base as builder
RUN apt-get update  \
    && apt-get install -y git  \
    && rm -rf /var/lib/apt/lists/*
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-workspace --no-dev

COPY . .
RUN sed -i "s/\(COMMIT_HASH *= *\).*/\1'$(git rev-parse HEAD)'/" tgpy/version.py
RUN rm -rf .git guide uv.lock pyproject.toml .dockerignore .gitignore README.md

FROM base as runner
COPY --from=builder /app /app
ENV PATH="/app/.venv/bin:$PATH"

ENV TGPY_DATA=/data
ENV PYTHONPATH=/app
VOLUME /data

ENTRYPOINT ["/app/entrypoint.sh"]
