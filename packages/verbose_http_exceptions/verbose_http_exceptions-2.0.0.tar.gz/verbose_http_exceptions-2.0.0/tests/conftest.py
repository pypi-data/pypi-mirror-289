import asyncio
from typing import TYPE_CHECKING, Literal

import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

from verbose_http_exceptions.exc import InternalServerErrorHTTPException
from verbose_http_exceptions.ext.fastapi import (
    apply_all_handlers,
    apply_verbose_http_exception_handler,
)

if TYPE_CHECKING:
    from collections.abc import Generator


@pytest.fixture(scope="session")
def event_loop() -> "Generator[asyncio.AbstractEventLoop, None, None]":
    """Event loop fixture."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture()
def test_app_only_verbose() -> "Generator[TestClient, None, None]":
    app = FastAPI()

    @app.get("/")
    def index():  # type: ignore reportUnusedFunction # noqa: ANN202
        raise InternalServerErrorHTTPException(template_vars={"reason": "test"})

    apply_verbose_http_exception_handler(app)

    with TestClient(
        app=app,
        base_url="http://test/",
    ) as c:
        yield c


@pytest.fixture()
def test_app_all_verbose() -> "Generator[TestClient, None, None]":
    app = FastAPI()

    @app.get("/")
    def index(a: Literal[1, 2], b: Literal[25]):  # type: ignore reportUnusedFunction  # noqa: ANN202, ARG001
        return {"message": "abc"}

    @app.get("/error")
    def error():  # type: ignore reportUnusedFunction # noqa: ANN202
        raise HTTPException(status_code=500, detail="test detail")

    @app.get("/verbose_error")
    def verbose_error():  # type: ignore reportUnusedFunction # noqa: ANN202
        raise InternalServerErrorHTTPException(template_vars={"reason": "test"})

    apply_all_handlers(app)

    with TestClient(
        app=app,
        base_url="http://test/",
    ) as c:
        yield c
