FROM python:3.12-slim

# uv ставим бинарником из официального образа — быстрее и без лишних слоёв
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONUNBUFFERED=1

# Зависимости ставим отдельным слоем: он переиспользуется,
# пока не изменились pyproject.toml или uv.lock
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-install-project

COPY src/ ./src/
COPY README.md ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Непривилегированный пользователь
RUN useradd --create-home --uid 1000 ooc && chown -R ooc:ooc /app
USER ooc

EXPOSE 8000

# --no-sync: окружение уже собрано на этапе build, повторная синхронизация не нужна
CMD ["uv", "run", "--no-sync", "--no-cache", "uvicorn", "ooc.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
