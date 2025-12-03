import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.timeseriesgridstatistics_document_format import TimeseriesgridstatisticsDocumentFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    layer_id: str,
    location_id: str,
    aggregation: Union[Unset, str] = UNSET,
    function: Union[Unset, str] = UNSET,
    document_format: Union[Unset, TimeseriesgridstatisticsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params["layerId"] = layer_id

    params["locationId"] = location_id

    params["aggregation"] = aggregation

    params["function"] = function

    json_document_format: Union[Unset, str] = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/timeseries/grid/statistics",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    layer_id: str,
    location_id: str,
    aggregation: Union[Unset, str] = UNSET,
    function: Union[Unset, str] = UNSET,
    document_format: Union[Unset, TimeseriesgridstatisticsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """apply a spatial transformation (min/max/sum/average) to each time step of a grid (defined by the
    layerId

     apply a spatial transformation (min/max/sum/average) to each time step of a grid (defined by the
    layerId. The output is defined by a location with a polygon<p>apply a spatial transformation
    (min/max/sum/average) to each time step of a grid (defined by the layerId. The output is defined by
    a location with a polygon

    Args:
        start_time (datetime.datetime): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        end_time (datetime.datetime): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        layer_id (str):  Example: Temp_forecast.
        location_id (str):
        aggregation (Union[Unset, str]):
        function (Union[Unset, str]):
        document_format (Union[Unset, TimeseriesgridstatisticsDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        start_time=start_time,
        end_time=end_time,
        layer_id=layer_id,
        location_id=location_id,
        aggregation=aggregation,
        function=function,
        document_format=document_format,
        document_version=document_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    layer_id: str,
    location_id: str,
    aggregation: Union[Unset, str] = UNSET,
    function: Union[Unset, str] = UNSET,
    document_format: Union[Unset, TimeseriesgridstatisticsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """apply a spatial transformation (min/max/sum/average) to each time step of a grid (defined by the
    layerId

     apply a spatial transformation (min/max/sum/average) to each time step of a grid (defined by the
    layerId. The output is defined by a location with a polygon<p>apply a spatial transformation
    (min/max/sum/average) to each time step of a grid (defined by the layerId. The output is defined by
    a location with a polygon

    Args:
        start_time (datetime.datetime): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        end_time (datetime.datetime): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        layer_id (str):  Example: Temp_forecast.
        location_id (str):
        aggregation (Union[Unset, str]):
        function (Union[Unset, str]):
        document_format (Union[Unset, TimeseriesgridstatisticsDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        start_time=start_time,
        end_time=end_time,
        layer_id=layer_id,
        location_id=location_id,
        aggregation=aggregation,
        function=function,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
