import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.timeseriesgridactions_convert_datum import TimeseriesgridactionsConvertDatum
from ...models.timeseriesgridactions_document_format import TimeseriesgridactionsDocumentFormat
from ...models.timeseriesgridactions_import_from_external_data_source import (
    TimeseriesgridactionsImportFromExternalDataSource,
)
from ...models.timeseriesgridactions_show_vertical_profile import TimeseriesgridactionsShowVerticalProfile
from ...models.timeseriesgridactions_use_display_units import TimeseriesgridactionsUseDisplayUnits
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    bbox: str,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    layers: str,
    x: Union[Unset, str] = UNSET,
    y: Union[Unset, str] = UNSET,
    external_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    ensemble_id: Union[Unset, str] = UNSET,
    ensemble_member_id: Union[Unset, str] = UNSET,
    elevation: Union[Unset, str] = UNSET,
    import_from_external_data_source: Union[Unset, TimeseriesgridactionsImportFromExternalDataSource] = UNSET,
    show_vertical_profile: Union[Unset, TimeseriesgridactionsShowVerticalProfile] = UNSET,
    use_display_units: Union[Unset, TimeseriesgridactionsUseDisplayUnits] = UNSET,
    convert_datum: Union[Unset, TimeseriesgridactionsConvertDatum] = UNSET,
    document_format: Union[Unset, TimeseriesgridactionsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["bbox"] = bbox

    json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params["layers"] = layers

    params["x"] = x

    params["y"] = y

    json_external_forecast_time: Union[Unset, str] = UNSET
    if not isinstance(external_forecast_time, Unset):
        json_external_forecast_time = external_forecast_time.isoformat()
    params["externalForecastTime"] = json_external_forecast_time

    params["ensembleId"] = ensemble_id

    params["ensembleMemberId"] = ensemble_member_id

    params["elevation"] = elevation

    json_import_from_external_data_source: Union[Unset, str] = UNSET
    if not isinstance(import_from_external_data_source, Unset):
        json_import_from_external_data_source = import_from_external_data_source.value

    params["importFromExternalDataSource"] = json_import_from_external_data_source

    json_show_vertical_profile: Union[Unset, str] = UNSET
    if not isinstance(show_vertical_profile, Unset):
        json_show_vertical_profile = show_vertical_profile.value

    params["showVerticalProfile"] = json_show_vertical_profile

    json_use_display_units: Union[Unset, str] = UNSET
    if not isinstance(use_display_units, Unset):
        json_use_display_units = use_display_units.value

    params["useDisplayUnits"] = json_use_display_units

    json_convert_datum: Union[Unset, str] = UNSET
    if not isinstance(convert_datum, Unset):
        json_convert_datum = convert_datum.value

    params["convertDatum"] = json_convert_datum

    json_document_format: Union[Unset, str] = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/timeseries/grid/actions",
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
    bbox: str,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    layers: str,
    x: Union[Unset, str] = UNSET,
    y: Union[Unset, str] = UNSET,
    external_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    ensemble_id: Union[Unset, str] = UNSET,
    ensemble_member_id: Union[Unset, str] = UNSET,
    elevation: Union[Unset, str] = UNSET,
    import_from_external_data_source: Union[Unset, TimeseriesgridactionsImportFromExternalDataSource] = UNSET,
    show_vertical_profile: Union[Unset, TimeseriesgridactionsShowVerticalProfile] = UNSET,
    use_display_units: Union[Unset, TimeseriesgridactionsUseDisplayUnits] = UNSET,
    convert_datum: Union[Unset, TimeseriesgridactionsConvertDatum] = UNSET,
    document_format: Union[Unset, TimeseriesgridactionsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get the details about how to display time series from a grid cell

     Get the details about how to display time series from a grid cell. The grid is specified by passing
    a layerId.<p>The grid cell is determined by specifying a x and y coordinate and a bounding box.
    Currenly only EPSG:3857 is supported for the x,y, and bounding box coordinates. At least a layer,
    startTime, endTime, x,y and bounding box are required. The timeseries/grid endpoint is intended to
    be used together with the Delf-FEWS WMS service. Every layer that is provided by the WMS service,
    can be used with this endpoint.

    Args:
        bbox (str):  Example:
            -1558755.612890017,4979850.04379049,1623657.8112034467,6709422.556884765.
        start_time (datetime.datetime): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        end_time (datetime.datetime): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        layers (str):  Example: Temp_forecast.
        x (Union[Unset, str]):  Example: 458757.12883912364.
        y (Union[Unset, str]):  Example: 5811252.569955047.
        external_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        ensemble_id (Union[Unset, str]):
        ensemble_member_id (Union[Unset, str]):
        elevation (Union[Unset, str]):
        import_from_external_data_source (Union[Unset,
            TimeseriesgridactionsImportFromExternalDataSource]):
        show_vertical_profile (Union[Unset, TimeseriesgridactionsShowVerticalProfile]):
        use_display_units (Union[Unset, TimeseriesgridactionsUseDisplayUnits]):
        convert_datum (Union[Unset, TimeseriesgridactionsConvertDatum]):
        document_format (Union[Unset, TimeseriesgridactionsDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bbox=bbox,
        start_time=start_time,
        end_time=end_time,
        layers=layers,
        x=x,
        y=y,
        external_forecast_time=external_forecast_time,
        ensemble_id=ensemble_id,
        ensemble_member_id=ensemble_member_id,
        elevation=elevation,
        import_from_external_data_source=import_from_external_data_source,
        show_vertical_profile=show_vertical_profile,
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
    client: Union[AuthenticatedClient, Client],
    bbox: str,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    layers: str,
    x: Union[Unset, str] = UNSET,
    y: Union[Unset, str] = UNSET,
    external_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    ensemble_id: Union[Unset, str] = UNSET,
    ensemble_member_id: Union[Unset, str] = UNSET,
    elevation: Union[Unset, str] = UNSET,
    import_from_external_data_source: Union[Unset, TimeseriesgridactionsImportFromExternalDataSource] = UNSET,
    show_vertical_profile: Union[Unset, TimeseriesgridactionsShowVerticalProfile] = UNSET,
    use_display_units: Union[Unset, TimeseriesgridactionsUseDisplayUnits] = UNSET,
    convert_datum: Union[Unset, TimeseriesgridactionsConvertDatum] = UNSET,
    document_format: Union[Unset, TimeseriesgridactionsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get the details about how to display time series from a grid cell

     Get the details about how to display time series from a grid cell. The grid is specified by passing
    a layerId.<p>The grid cell is determined by specifying a x and y coordinate and a bounding box.
    Currenly only EPSG:3857 is supported for the x,y, and bounding box coordinates. At least a layer,
    startTime, endTime, x,y and bounding box are required. The timeseries/grid endpoint is intended to
    be used together with the Delf-FEWS WMS service. Every layer that is provided by the WMS service,
    can be used with this endpoint.

    Args:
        bbox (str):  Example:
            -1558755.612890017,4979850.04379049,1623657.8112034467,6709422.556884765.
        start_time (datetime.datetime): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        end_time (datetime.datetime): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        layers (str):  Example: Temp_forecast.
        x (Union[Unset, str]):  Example: 458757.12883912364.
        y (Union[Unset, str]):  Example: 5811252.569955047.
        external_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        ensemble_id (Union[Unset, str]):
        ensemble_member_id (Union[Unset, str]):
        elevation (Union[Unset, str]):
        import_from_external_data_source (Union[Unset,
            TimeseriesgridactionsImportFromExternalDataSource]):
        show_vertical_profile (Union[Unset, TimeseriesgridactionsShowVerticalProfile]):
        use_display_units (Union[Unset, TimeseriesgridactionsUseDisplayUnits]):
        convert_datum (Union[Unset, TimeseriesgridactionsConvertDatum]):
        document_format (Union[Unset, TimeseriesgridactionsDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bbox=bbox,
        start_time=start_time,
        end_time=end_time,
        layers=layers,
        x=x,
        y=y,
        external_forecast_time=external_forecast_time,
        ensemble_id=ensemble_id,
        ensemble_member_id=ensemble_member_id,
        elevation=elevation,
        import_from_external_data_source=import_from_external_data_source,
        show_vertical_profile=show_vertical_profile,
        use_display_units=use_display_units,
        convert_datum=convert_datum,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
