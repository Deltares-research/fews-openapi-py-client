import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archiveproductsmetadata_document_format import ArchiveproductsmetadataDocumentFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_forecast_time: Unset | datetime.datetime = UNSET,
    end_forecast_time: Unset | datetime.datetime = UNSET,
    forecast_count: Unset | str = UNSET,
    document_format: Unset | ArchiveproductsmetadataDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_forecast_time: Unset | str = UNSET
    if not isinstance(start_forecast_time, Unset):
        json_start_forecast_time = start_forecast_time.isoformat()
    params["startForecastTime"] = json_start_forecast_time

    json_end_forecast_time: Unset | str = UNSET
    if not isinstance(end_forecast_time, Unset):
        json_end_forecast_time = end_forecast_time.isoformat()
    params["endForecastTime"] = json_end_forecast_time

    params["forecastCount"] = forecast_count

    json_document_format: Unset | str = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/archive/productsmetadata",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    start_forecast_time: Unset | datetime.datetime = UNSET,
    end_forecast_time: Unset | datetime.datetime = UNSET,
    forecast_count: Unset | str = UNSET,
    document_format: Unset | ArchiveproductsmetadataDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[Any]:
    """Returns a list of metadata found in the archive, where the T0 falls between the startForecastTime
    and endForecastTime

     Returns a list of metadata found in the archive, where the T0 falls between the startForecastTime
    and endForecastTime.

    Args:
        start_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        forecast_count (Union[Unset, str]):
        document_format (Union[Unset, ArchiveproductsmetadataDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        start_forecast_time=start_forecast_time,
        end_forecast_time=end_forecast_time,
        forecast_count=forecast_count,
        document_format=document_format,
        document_version=document_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start_forecast_time: Unset | datetime.datetime = UNSET,
    end_forecast_time: Unset | datetime.datetime = UNSET,
    forecast_count: Unset | str = UNSET,
    document_format: Unset | ArchiveproductsmetadataDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[Any]:
    """Returns a list of metadata found in the archive, where the T0 falls between the startForecastTime
    and endForecastTime

     Returns a list of metadata found in the archive, where the T0 falls between the startForecastTime
    and endForecastTime.

    Args:
        start_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        forecast_count (Union[Unset, str]):
        document_format (Union[Unset, ArchiveproductsmetadataDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        start_forecast_time=start_forecast_time,
        end_forecast_time=end_forecast_time,
        forecast_count=forecast_count,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
