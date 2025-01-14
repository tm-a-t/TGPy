# syntax=docker/dockerfile:1.3
FROM python:3.12-slim as base
WORKDIR /app

FROM base as builder
RUN apt-get update  \
    && apt-get install -y git  \
    && rm -rf /var/lib/apt/lists/*

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install poetry~=2.0 \
    && pip install poetry-plugin-export
RUN python -m venv /venv

COPY pyproject.toml poetry.lock LICENSE ./
RUN --mount=type=cache,target=/root/.cache/pip \
    poetry export -o /tmp/requirements.txt && /venv/bin/pip install -r /tmp/requirements.txt

COPY . .
RUN sed -i "s/\(COMMIT_HASH *= *\).*/\1'$(git rev-parse HEAD)'/" tgpy/version.py
RUN rm -rf .git guide poetry.lock pyproject.toml .dockerignore .gitignore README.md

FROM base as runner
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"

COPY --from=builder /app /app

ENV TGPY_DATA=/data
ENV PYTHONPATH=/app
VOLUME /data

ENTRYPOINT ["/app/entrypoint.sh"]
