import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.timeseriesgridmaxvalues_convert_datum import TimeseriesgridmaxvaluesConvertDatum
from ...models.timeseriesgridmaxvalues_document_format import TimeseriesgridmaxvaluesDocumentFormat
from ...models.timeseriesgridmaxvalues_use_display_units import TimeseriesgridmaxvaluesUseDisplayUnits
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    layers: str,
    convert_datum: Union[Unset, TimeseriesgridmaxvaluesConvertDatum] = UNSET,
    use_display_units: Union[Unset, TimeseriesgridmaxvaluesUseDisplayUnits] = UNSET,
    download_as_file: Union[Unset, str] = UNSET,
    document_format: Union[Unset, TimeseriesgridmaxvaluesDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params["layers"] = layers

    json_convert_datum: Union[Unset, str] = UNSET
    if not isinstance(convert_datum, Unset):
        json_convert_datum = convert_datum.value

    params["convertDatum"] = json_convert_datum

    json_use_display_units: Union[Unset, str] = UNSET
    if not isinstance(use_display_units, Unset):
        json_use_display_units = use_display_units.value

    params["useDisplayUnits"] = json_use_display_units

    params["downloadAsFile"] = download_as_file

    json_document_format: Union[Unset, str] = UNSET
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
    layers: str,
    convert_datum: Union[Unset, TimeseriesgridmaxvaluesConvertDatum] = UNSET,
    use_display_units: Union[Unset, TimeseriesgridmaxvaluesUseDisplayUnits] = UNSET,
    download_as_file: Union[Unset, str] = UNSET,
    document_format: Union[Unset, TimeseriesgridmaxvaluesDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get the maximum values for each time for a grid for a request period

     Get the maximum values for each time for a grid for a request period. The grid is specified by
    passing a layerId. At least a layer, startTime and endTime are required. The
    timeseries/grid/maxvalues endpoint is intended to be used together with the Delf-FEWS WMS service.
    Every layer that is provided by the WMS service, can be used with this endpoint.<p>The grid cell is
    determined by specifying a x and y coordinate and a bounding box. Currently only EPSG:3857 is
    supported for the x,y, and bounding box coordinates. At least a layer, startTime, endTime, x,y and
    bounding box are required. The timeseries/grid endpoint is intended to be used together with the
    Delf-FEWS WMS service. Every layer that is provided by the WMS service, can be used with this
    endpoint. The visibleInTimeSeriesDisplay configuration is respected. If set to false (default is
    true), the timeseries will not be returned.

    Args:
        start_time (datetime.datetime): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        end_time (datetime.datetime): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        layers (str):  Example: Temp_forecast.
        convert_datum (Union[Unset, TimeseriesgridmaxvaluesConvertDatum]):
        use_display_units (Union[Unset, TimeseriesgridmaxvaluesUseDisplayUnits]):
        download_as_file (Union[Unset, str]):
        document_format (Union[Unset, TimeseriesgridmaxvaluesDocumentFormat]):
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
        layers=layers,
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
    client: Union[AuthenticatedClient, Client],
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    layers: str,
    convert_datum: Union[Unset, TimeseriesgridmaxvaluesConvertDatum] = UNSET,
    use_display_units: Union[Unset, TimeseriesgridmaxvaluesUseDisplayUnits] = UNSET,
    download_as_file: Union[Unset, str] = UNSET,
    document_format: Union[Unset, TimeseriesgridmaxvaluesDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get the maximum values for each time for a grid for a request period

     Get the maximum values for each time for a grid for a request period. The grid is specified by
    passing a layerId. At least a layer, startTime and endTime are required. The
    timeseries/grid/maxvalues endpoint is intended to be used together with the Delf-FEWS WMS service.
    Every layer that is provided by the WMS service, can be used with this endpoint.<p>The grid cell is
    determined by specifying a x and y coordinate and a bounding box. Currently only EPSG:3857 is
    supported for the x,y, and bounding box coordinates. At least a layer, startTime, endTime, x,y and
    bounding box are required. The timeseries/grid endpoint is intended to be used together with the
    Delf-FEWS WMS service. Every layer that is provided by the WMS service, can be used with this
    endpoint. The visibleInTimeSeriesDisplay configuration is respected. If set to false (default is
    true), the timeseries will not be returned.

    Args:
        start_time (datetime.datetime): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        end_time (datetime.datetime): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        layers (str):  Example: Temp_forecast.
        convert_datum (Union[Unset, TimeseriesgridmaxvaluesConvertDatum]):
        use_display_units (Union[Unset, TimeseriesgridmaxvaluesUseDisplayUnits]):
        download_as_file (Union[Unset, str]):
        document_format (Union[Unset, TimeseriesgridmaxvaluesDocumentFormat]):
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
        layers=layers,
        convert_datum=convert_datum,
        use_display_units=use_display_units,
        download_as_file=download_as_file,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
