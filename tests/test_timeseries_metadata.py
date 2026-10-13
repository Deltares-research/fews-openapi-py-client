"""Regression tests kept outside the overwritten generated project."""

import inspect
import unittest

import httpx
from fews_openapi_py_client import Client
from fews_openapi_py_client.api.timeseries import timeseries, timeseriesgrid
from fews_openapi_py_client.models.timeseries_document_format import TimeseriesDocumentFormat
from fews_openapi_py_client.models.timeseries_show_fews_time_series_metadata import TimeseriesShowFewsTimeSeriesMetadata
from fews_openapi_py_client.models.timeseriesgrid_document_format import TimeseriesgridDocumentFormat
from fews_openapi_py_client.models.timeseriesgrid_show_fews_time_series_metadata import (
    TimeseriesgridShowFewsTimeSeriesMetadata,
)
from fews_openapi_py_client.types import UNSET

ENDPOINTS = (
    (timeseries, TimeseriesShowFewsTimeSeriesMetadata, TimeseriesDocumentFormat, "/timeseries"),
    (timeseriesgrid, TimeseriesgridShowFewsTimeSeriesMetadata, TimeseriesgridDocumentFormat, "/timeseries/grid"),
)
PAYLOAD = b"raw PI_NETCDF response"


def metadata_cases(enum):
    return (
        ({}, None),
        ({"show_fews_time_series_metadata": enum.TRUE}, "true"),
        (
            {"show_fews_time_series_metadata": enum.FALSE},
            "false",
        ),
    )


class TestMetadataSignature(unittest.TestCase):
    def test_optional_named_parameter(self):
        for endpoint, _, _, _ in ENDPOINTS:
            for name in ("sync_detailed", "asyncio_detailed"):
                with self.subTest(endpoint=endpoint.__name__, function=name):
                    parameter = inspect.signature(getattr(endpoint, name)).parameters["show_fews_time_series_metadata"]
                    self.assertIs(parameter.default, UNSET)
                    self.assertEqual(parameter.kind, inspect.Parameter.KEYWORD_ONLY)

    def test_timeseries_datetime_postprocessing(self):
        kwargs = timeseries._get_kwargs(start_time="2026-10-13T00:00:00Z", end_time="2026-10-14T00:00:00Z")
        self.assertEqual(kwargs["params"]["startTime"], "2026-10-13T00:00:00Z")
        self.assertEqual(kwargs["params"]["endTime"], "2026-10-14T00:00:00Z")


class TestSyncMetadata(unittest.TestCase):
    def test_http_queries_and_raw_response(self):
        for endpoint, enum, document_format, path in ENDPOINTS:
            for arguments, expected in metadata_cases(enum):
                if endpoint is timeseriesgrid:
                    arguments["layers"] = "test-layer"
                for status in (200, 206) if endpoint is timeseries else (200,):
                    with self.subTest(endpoint=path, metadata=expected, status=status):
                        requests = []

                        def respond(request):
                            requests.append(request)
                            return httpx.Response(status, content=PAYLOAD, headers={"content-type": "application/zip"})

                        with Client(
                            base_url="https://example.test",
                            httpx_args={"transport": httpx.MockTransport(respond)},
                        ) as client:
                            response = endpoint.sync_detailed(
                                client=client, document_format=document_format.PI_NETCDF, **arguments
                            )
                        self.assertEqual(len(requests), 1)
                        request = requests[0]
                        self.assertEqual(request.method, "GET")
                        self.assertEqual(request.url.path, path)
                        self.assertEqual(request.url.params["documentFormat"], "PI_NETCDF")
                        self.assertEqual(request.url.params.get("showFewsTimeSeriesMetadata"), expected)
                        self.assertEqual(response.status_code, status)
                        self.assertEqual(response.content, PAYLOAD)


class TestAsyncMetadata(unittest.IsolatedAsyncioTestCase):
    async def test_http_queries_and_raw_response(self):
        for endpoint, enum, document_format, path in ENDPOINTS:
            for arguments, expected in metadata_cases(enum):
                if endpoint is timeseriesgrid:
                    arguments["layers"] = "test-layer"
                for status in (200, 206) if endpoint is timeseries else (200,):
                    with self.subTest(endpoint=path, metadata=expected, status=status):
                        requests = []

                        def respond(request):
                            requests.append(request)
                            return httpx.Response(status, content=PAYLOAD, headers={"content-type": "application/zip"})

                        async with Client(
                            base_url="https://example.test",
                            httpx_args={"transport": httpx.MockTransport(respond)},
                        ) as client:
                            response = await endpoint.asyncio_detailed(
                                client=client, document_format=document_format.PI_NETCDF, **arguments
                            )
                        self.assertEqual(len(requests), 1)
                        request = requests[0]
                        self.assertEqual(request.method, "GET")
                        self.assertEqual(request.url.path, path)
                        self.assertEqual(request.url.params["documentFormat"], "PI_NETCDF")
                        self.assertEqual(request.url.params.get("showFewsTimeSeriesMetadata"), expected)
                        self.assertEqual(response.status_code, status)
                        self.assertEqual(response.content, PAYLOAD)

