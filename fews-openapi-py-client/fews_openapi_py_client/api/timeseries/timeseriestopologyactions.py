import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.timeseriestopologyactions_convert_datum import TimeseriestopologyactionsConvertDatum
from ...models.timeseriestopologyactions_document_format import TimeseriestopologyactionsDocumentFormat
from ...models.timeseriestopologyactions_use_display_units import TimeseriestopologyactionsUseDisplayUnits
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    node_id: str,
    time_series_display_index: str,
    download_as_file: str | Unset = UNSET,
    time_zero: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    use_display_units: TimeseriestopologyactionsUseDisplayUnits | Unset = UNSET,
    convert_datum: TimeseriestopologyactionsConvertDatum | Unset = UNSET,
    document_format: TimeseriestopologyactionsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["nodeId"] = node_id

    params["timeSeriesDisplayIndex"] = time_series_display_index

    params["downloadAsFile"] = download_as_file

    params["timeZero"] = time_zero

    json_start_time: str | Unset = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: str | Unset = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    json_use_display_units: str | Unset = UNSET
    if not isinstance(use_display_units, Unset):
        json_use_display_units = use_display_units.value

    params["useDisplayUnits"] = json_use_display_units

    json_convert_datum: str | Unset = UNSET
    if not isinstance(convert_datum, Unset):
        json_convert_datum = convert_datum.value

    params["convertDatum"] = json_convert_datum

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/timeseries/topology/actions",
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
    node_id: str,
    time_series_display_index: str,
    download_as_file: str | Unset = UNSET,
    time_zero: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    use_display_units: TimeseriestopologyactionsUseDisplayUnits | Unset = UNSET,
    convert_datum: TimeseriestopologyactionsConvertDatum | Unset = UNSET,
    document_format: TimeseriestopologyactionsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get the timeseries from the display group actions for a certain topology node

     Get the timeseries from the display group actions for a certain topology node

    Args:
        node_id (str):
        time_series_display_index (str):
        download_as_file (str | Unset):
        time_zero (str | Unset):
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        use_display_units (TimeseriestopologyactionsUseDisplayUnits | Unset):
        convert_datum (TimeseriestopologyactionsConvertDatum | Unset):
        document_format (TimeseriestopologyactionsDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        time_series_display_index=time_series_display_index,
        download_as_file=download_as_file,
        time_zero=time_zero,
        start_time=start_time,
        end_time=end_time,
        use_display_units=use_display_units,
        convert_datum=convert_datum,
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
    node_id: str,
    time_series_display_index: str,
    download_as_file: str | Unset = UNSET,
    time_zero: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    use_display_units: TimeseriestopologyactionsUseDisplayUnits | Unset = UNSET,
    convert_datum: TimeseriestopologyactionsConvertDatum | Unset = UNSET,
    document_format: TimeseriestopologyactionsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get the timeseries from the display group actions for a certain topology node

     Get the timeseries from the display group actions for a certain topology node

    Args:
        node_id (str):
        time_series_display_index (str):
        download_as_file (str | Unset):
        time_zero (str | Unset):
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        use_display_units (TimeseriestopologyactionsUseDisplayUnits | Unset):
        convert_datum (TimeseriestopologyactionsConvertDatum | Unset):
        document_format (TimeseriestopologyactionsDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        time_series_display_index=time_series_display_index,
        download_as_file=download_as_file,
        time_zero=time_zero,
        start_time=start_time,
        end_time=end_time,
        use_display_units=use_display_units,
        convert_datum=convert_datum,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
