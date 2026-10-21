import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.timeserieshistory_convert_datum import TimeserieshistoryConvertDatum
from ...models.timeserieshistory_document_format import TimeserieshistoryDocumentFormat
from ...models.timeserieshistory_use_display_units import TimeserieshistoryUseDisplayUnits
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    times: datetime.datetime | Unset = UNSET,
    time_series_id: str | Unset = UNSET,
    convert_datum: TimeserieshistoryConvertDatum | Unset = UNSET,
    use_display_units: TimeserieshistoryUseDisplayUnits | Unset = UNSET,
    document_format: TimeserieshistoryDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_times: str | Unset = UNSET
    if not isinstance(times, Unset):
        json_times = times.isoformat()
    params["times"] = json_times

    params["timeSeriesId"] = time_series_id

    json_convert_datum: str | Unset = UNSET
    if not isinstance(convert_datum, Unset):
        json_convert_datum = convert_datum.value

    params["convertDatum"] = json_convert_datum

    json_use_display_units: str | Unset = UNSET
    if not isinstance(use_display_units, Unset):
        json_use_display_units = use_display_units.value

    params["useDisplayUnits"] = json_use_display_units

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/timeseries/history",
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
    times: datetime.datetime | Unset = UNSET,
    time_series_id: str | Unset = UNSET,
    convert_datum: TimeserieshistoryConvertDatum | Unset = UNSET,
    use_display_units: TimeserieshistoryUseDisplayUnits | Unset = UNSET,
    document_format: TimeserieshistoryDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get the history of edits for one or more times for a certain time series

     Get the history of edits for one or more times for a certain time series<p>Get the history of edits
    for one or more times for a certain time series

    Args:
        times (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        time_series_id (str | Unset):
        convert_datum (TimeserieshistoryConvertDatum | Unset):
        use_display_units (TimeserieshistoryUseDisplayUnits | Unset):
        document_format (TimeserieshistoryDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        times=times,
        time_series_id=time_series_id,
        convert_datum=convert_datum,
        use_display_units=use_display_units,
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
    times: datetime.datetime | Unset = UNSET,
    time_series_id: str | Unset = UNSET,
    convert_datum: TimeserieshistoryConvertDatum | Unset = UNSET,
    use_display_units: TimeserieshistoryUseDisplayUnits | Unset = UNSET,
    document_format: TimeserieshistoryDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get the history of edits for one or more times for a certain time series

     Get the history of edits for one or more times for a certain time series<p>Get the history of edits
    for one or more times for a certain time series

    Args:
        times (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        time_series_id (str | Unset):
        convert_datum (TimeserieshistoryConvertDatum | Unset):
        use_display_units (TimeserieshistoryUseDisplayUnits | Unset):
        document_format (TimeserieshistoryDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        times=times,
        time_series_id=time_series_id,
        convert_datum=convert_datum,
        use_display_units=use_display_units,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
