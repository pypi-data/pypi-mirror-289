# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from flux_client import Flux, AsyncFlux
from tests.utils import assert_matches_type
from flux_client.types import ClassifyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTopLevel:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_classify(self, client: Flux) -> None:
        top_level = client.classify(
            input="string",
            labels=["string", "string", "string"],
        )
        assert_matches_type(ClassifyResponse, top_level, path=["response"])

    @parametrize
    def test_raw_response_classify(self, client: Flux) -> None:
        response = client.with_raw_response.classify(
            input="string",
            labels=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_level = response.parse()
        assert_matches_type(ClassifyResponse, top_level, path=["response"])

    @parametrize
    def test_streaming_response_classify(self, client: Flux) -> None:
        with client.with_streaming_response.classify(
            input="string",
            labels=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_level = response.parse()
            assert_matches_type(ClassifyResponse, top_level, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTopLevel:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_classify(self, async_client: AsyncFlux) -> None:
        top_level = await async_client.classify(
            input="string",
            labels=["string", "string", "string"],
        )
        assert_matches_type(ClassifyResponse, top_level, path=["response"])

    @parametrize
    async def test_raw_response_classify(self, async_client: AsyncFlux) -> None:
        response = await async_client.with_raw_response.classify(
            input="string",
            labels=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_level = await response.parse()
        assert_matches_type(ClassifyResponse, top_level, path=["response"])

    @parametrize
    async def test_streaming_response_classify(self, async_client: AsyncFlux) -> None:
        async with async_client.with_streaming_response.classify(
            input="string",
            labels=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_level = await response.parse()
            assert_matches_type(ClassifyResponse, top_level, path=["response"])

        assert cast(Any, response.is_closed) is True
