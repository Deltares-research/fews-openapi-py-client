import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.timeseriesgridmaxvalues_convert_datum import TimeseriesgridmaxvaluesConvertDatum
from ...models.timeseriesgridmaxvalues_document_format import TimeseriesgridmaxvaluesDocumentFormat
from ...models.timeseriesgridmaxvalues_use_display_units import TimeseriesgridmaxvaluesUseDisplayUnits
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    layers: str,
    aggregation: str | Unset = UNSET,
    external_forecast_time: datetime.datetime | Unset = UNSET,
    convert_datum: TimeseriesgridmaxvaluesConvertDatum | Unset = UNSET,
    use_display_units: TimeseriesgridmaxvaluesUseDisplayUnits | Unset = UNSET,
    download_as_file: str | Unset = UNSET,
    document_format: TimeseriesgridmaxvaluesDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_time: str | Unset = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: str | Unset = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params["layers"] = layers

    params["aggregation"] = aggregation

    json_external_forecast_time: str | Unset = UNSET
    if not isinstance(external_forecast_time, Unset):
        json_external_forecast_time = external_forecast_time.isoformat()
    params["externalForecastTime"] = json_external_forecast_time

    json_convert_datum: str | Unset = UNSET
    if not isinstance(convert_datum, Unset):
        json_convert_datum = convert_datum.value

    params["convertDatum"] = json_convert_datum

    json_use_display_units: str | Unset = UNSET
    if not isinstance(use_display_units, Unset):
        json_use_display_units = use_display_units.value

    params["useDisplayUnits"] = json_use_display_units

    params["downloadAsFile"] = download_as_file

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/timeseries/grid/maxvalues",
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
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    layers: str,
    aggregation: str | Unset = UNSET,
    external_forecast_time: datetime.datetime | Unset = UNSET,
    convert_datum: TimeseriesgridmaxvaluesConvertDatum | Unset = UNSET,
    use_display_units: TimeseriesgridmaxvaluesUseDisplayUnits | Unset = UNSET,
    download_as_file: str | Unset = UNSET,
    document_format: TimeseriesgridmaxvaluesDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get the maximum values for each time for a grid for a request period

     Get the maximum values for each time for a grid for a request period. The grid is specified by
    passing a layerId. At least a layer, startTime and endTime are required. The
    timeseries/grid/maxvalues endpoint is intended to be used together with the Delf-FEWS WMS service.
    Every layer that is provided by the WMS service, can be used with this endpoint.<p>Every layer that
    is provided by the WMS service, can be used with this endpoint. startTime and endTime are required
    if no externalForecastTime is passed.

    Args:
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        layers (str):  Example: Temp_forecast.
        aggregation (str | Unset):  Example: day.
        external_forecast_time (datetime.datetime | Unset): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        convert_datum (TimeseriesgridmaxvaluesConvertDatum | Unset):
        use_display_units (TimeseriesgridmaxvaluesUseDisplayUnits | Unset):
        download_as_file (str | Unset):
        document_format (TimeseriesgridmaxvaluesDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        start_time=start_time,
        end_time=end_time,
        layers=layers,
        aggregation=aggregation,
        external_forecast_time=external_forecast_time,
        convert_datum=convert_datum,
        use_display_units=use_display_units,
        download_as_file=download_as_file,
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
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    layers: str,
    aggregation: str | Unset = UNSET,
    external_forecast_time: datetime.datetime | Unset = UNSET,
    convert_datum: TimeseriesgridmaxvaluesConvertDatum | Unset = UNSET,
    use_display_units: TimeseriesgridmaxvaluesUseDisplayUnits | Unset = UNSET,
    download_as_file: str | Unset = UNSET,
    document_format: TimeseriesgridmaxvaluesDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get the maximum values for each time for a grid for a request period

     Get the maximum values for each time for a grid for a request period. The grid is specified by
    passing a layerId. At least a layer, startTime and endTime are required. The
    timeseries/grid/maxvalues endpoint is intended to be used together with the Delf-FEWS WMS service.
    Every layer that is provided by the WMS service, can be used with this endpoint.<p>Every layer that
    is provided by the WMS service, can be used with this endpoint. startTime and endTime are required
    if no externalForecastTime is passed.

    Args:
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        layers (str):  Example: Temp_forecast.
        aggregation (str | Unset):  Example: day.
        external_forecast_time (datetime.datetime | Unset): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        convert_datum (TimeseriesgridmaxvaluesConvertDatum | Unset):
        use_display_units (TimeseriesgridmaxvaluesUseDisplayUnits | Unset):
        download_as_file (str | Unset):
        document_format (TimeseriesgridmaxvaluesDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        start_time=start_time,
        end_time=end_time,
        layers=layers,
        aggregation=aggregation,
        external_forecast_time=external_forecast_time,
        convert_datum=convert_datum,
        use_display_units=use_display_units,
        download_as_file=download_as_file,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
