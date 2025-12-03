import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.timeseriesgrid_convert_datum import TimeseriesgridConvertDatum
from ...models.timeseriesgrid_document_format import TimeseriesgridDocumentFormat
from ...models.timeseriesgrid_import_from_external_data_source import TimeseriesgridImportFromExternalDataSource
from ...models.timeseriesgrid_omit_empty_time_series import TimeseriesgridOmitEmptyTimeSeries
from ...models.timeseriesgrid_omit_missing import TimeseriesgridOmitMissing
from ...models.timeseriesgrid_only_forecasts import TimeseriesgridOnlyForecasts
from ...models.timeseriesgrid_only_headers import TimeseriesgridOnlyHeaders
from ...models.timeseriesgrid_only_manual_edits import TimeseriesgridOnlyManualEdits
from ...models.timeseriesgrid_show_ensemble_member_ids import TimeseriesgridShowEnsembleMemberIds
from ...models.timeseriesgrid_show_products import TimeseriesgridShowProducts
from ...models.timeseriesgrid_show_statistics import TimeseriesgridShowStatistics
from ...models.timeseriesgrid_show_thresholds import TimeseriesgridShowThresholds
from ...models.timeseriesgrid_show_vertical_profile import TimeseriesgridShowVerticalProfile
from ...models.timeseriesgrid_use_display_units import TimeseriesgridUseDisplayUnits
from ...models.timeseriesgrid_use_milliseconds import TimeseriesgridUseMilliseconds
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    bbox: Union[Unset, str] = UNSET,
    before_start_time_count: Union[Unset, str] = UNSET,
    after_end_time_count: Union[Unset, str] = UNSET,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    layers: str,
    x: Union[Unset, str] = UNSET,
    y: Union[Unset, str] = UNSET,
    external_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    ensemble_id: Union[Unset, str] = UNSET,
    ensemble_member_id: Union[Unset, str] = UNSET,
    elevation: Union[Unset, str] = UNSET,
    import_from_external_data_source: Union[Unset, TimeseriesgridImportFromExternalDataSource] = UNSET,
    convert_datum: Union[Unset, TimeseriesgridConvertDatum] = UNSET,
    show_ensemble_member_ids: Union[Unset, TimeseriesgridShowEnsembleMemberIds] = UNSET,
    use_display_units: Union[Unset, TimeseriesgridUseDisplayUnits] = UNSET,
    show_vertical_profile: Union[Unset, TimeseriesgridShowVerticalProfile] = UNSET,
    show_thresholds: Union[Unset, TimeseriesgridShowThresholds] = UNSET,
    omit_missing: Union[Unset, TimeseriesgridOmitMissing] = UNSET,
    omit_empty_time_series: Union[Unset, TimeseriesgridOmitEmptyTimeSeries] = UNSET,
    only_manual_edits: Union[Unset, TimeseriesgridOnlyManualEdits] = UNSET,
    only_headers: Union[Unset, TimeseriesgridOnlyHeaders] = UNSET,
    only_forecasts: Union[Unset, TimeseriesgridOnlyForecasts] = UNSET,
    show_statistics: Union[Unset, TimeseriesgridShowStatistics] = UNSET,
    use_milliseconds: Union[Unset, TimeseriesgridUseMilliseconds] = UNSET,
    show_products: Union[Unset, TimeseriesgridShowProducts] = UNSET,
    download_as_file: Union[Unset, str] = UNSET,
    document_format: Union[Unset, TimeseriesgridDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["bbox"] = bbox

    params["beforeStartTimeCount"] = before_start_time_count

    params["afterEndTimeCount"] = after_end_time_count

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

    json_convert_datum: Union[Unset, str] = UNSET
    if not isinstance(convert_datum, Unset):
        json_convert_datum = convert_datum.value

    params["convertDatum"] = json_convert_datum

    json_show_ensemble_member_ids: Union[Unset, str] = UNSET
    if not isinstance(show_ensemble_member_ids, Unset):
        json_show_ensemble_member_ids = show_ensemble_member_ids.value

    params["showEnsembleMemberIds"] = json_show_ensemble_member_ids

    json_use_display_units: Union[Unset, str] = UNSET
    if not isinstance(use_display_units, Unset):
        json_use_display_units = use_display_units.value

    params["useDisplayUnits"] = json_use_display_units

    json_show_vertical_profile: Union[Unset, str] = UNSET
    if not isinstance(show_vertical_profile, Unset):
        json_show_vertical_profile = show_vertical_profile.value

    params["showVerticalProfile"] = json_show_vertical_profile

    json_show_thresholds: Union[Unset, str] = UNSET
    if not isinstance(show_thresholds, Unset):
        json_show_thresholds = show_thresholds.value

    params["showThresholds"] = json_show_thresholds

    json_omit_missing: Union[Unset, str] = UNSET
    if not isinstance(omit_missing, Unset):
        json_omit_missing = omit_missing.value

    params["omitMissing"] = json_omit_missing

    json_omit_empty_time_series: Union[Unset, str] = UNSET
    if not isinstance(omit_empty_time_series, Unset):
        json_omit_empty_time_series = omit_empty_time_series.value

    params["omitEmptyTimeSeries"] = json_omit_empty_time_series

    json_only_manual_edits: Union[Unset, str] = UNSET
    if not isinstance(only_manual_edits, Unset):
        json_only_manual_edits = only_manual_edits.value

    params["onlyManualEdits"] = json_only_manual_edits

    json_only_headers: Union[Unset, str] = UNSET
    if not isinstance(only_headers, Unset):
        json_only_headers = only_headers.value

    params["onlyHeaders"] = json_only_headers

    json_only_forecasts: Union[Unset, str] = UNSET
    if not isinstance(only_forecasts, Unset):
        json_only_forecasts = only_forecasts.value

    params["onlyForecasts"] = json_only_forecasts

    json_show_statistics: Union[Unset, str] = UNSET
    if not isinstance(show_statistics, Unset):
        json_show_statistics = show_statistics.value

    params["showStatistics"] = json_show_statistics

    json_use_milliseconds: Union[Unset, str] = UNSET
    if not isinstance(use_milliseconds, Unset):
        json_use_milliseconds = use_milliseconds.value

    params["useMilliseconds"] = json_use_milliseconds

    json_show_products: Union[Unset, str] = UNSET
    if not isinstance(show_products, Unset):
        json_show_products = show_products.value

    params["showProducts"] = json_show_products

    params["downloadAsFile"] = download_as_file

    json_document_format: Union[Unset, str] = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/timeseries/grid",
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
    bbox: Union[Unset, str] = UNSET,
    before_start_time_count: Union[Unset, str] = UNSET,
    after_end_time_count: Union[Unset, str] = UNSET,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    layers: str,
    x: Union[Unset, str] = UNSET,
    y: Union[Unset, str] = UNSET,
    external_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    ensemble_id: Union[Unset, str] = UNSET,
    ensemble_member_id: Union[Unset, str] = UNSET,
    elevation: Union[Unset, str] = UNSET,
    import_from_external_data_source: Union[Unset, TimeseriesgridImportFromExternalDataSource] = UNSET,
    convert_datum: Union[Unset, TimeseriesgridConvertDatum] = UNSET,
    show_ensemble_member_ids: Union[Unset, TimeseriesgridShowEnsembleMemberIds] = UNSET,
    use_display_units: Union[Unset, TimeseriesgridUseDisplayUnits] = UNSET,
    show_vertical_profile: Union[Unset, TimeseriesgridShowVerticalProfile] = UNSET,
    show_thresholds: Union[Unset, TimeseriesgridShowThresholds] = UNSET,
    omit_missing: Union[Unset, TimeseriesgridOmitMissing] = UNSET,
    omit_empty_time_series: Union[Unset, TimeseriesgridOmitEmptyTimeSeries] = UNSET,
    only_manual_edits: Union[Unset, TimeseriesgridOnlyManualEdits] = UNSET,
    only_headers: Union[Unset, TimeseriesgridOnlyHeaders] = UNSET,
    only_forecasts: Union[Unset, TimeseriesgridOnlyForecasts] = UNSET,
    show_statistics: Union[Unset, TimeseriesgridShowStatistics] = UNSET,
    use_milliseconds: Union[Unset, TimeseriesgridUseMilliseconds] = UNSET,
    show_products: Union[Unset, TimeseriesgridShowProducts] = UNSET,
    download_as_file: Union[Unset, str] = UNSET,
    document_format: Union[Unset, TimeseriesgridDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get the timeseries containing the data from a grid cell for a request period

     Get the timeseries containing the data from a grid cell for a request period. The grid is specified
    by passing a layerId.<p>When requesting the timeseries in PI_JSON The grid cell is determined by
    specifying a x and y coordinate and a bounding box. Currently only EPSG:3857 is supported for the
    x,y, and bounding box coordinates. At least a layer, startTime, endTime, x,y and bounding box are
    required. The timeseries/grid endpoint is intended to be used together with the Delf-FEWS WMS
    service. Every layer that is provided by the WMS service, can be used with this endpoint. The
    visibleInTimeSeriesDisplay configuration is respected. If set to false (default is true), the
    timeseries will not be returned.
    It is also possible to get the grid data in Netcdf format using the PI_NETCDF documentFormat. In
    this case no bbox or x,y coordinates should be specified. Timeseries configured in a datalayer will
    be stored in the the same Netcdf file. There is no support for 3D data or track layers.

    Args:
        bbox (Union[Unset, str]):  Example:
            -1558755.612890017,4979850.04379049,1623657.8112034467,6709422.556884765.
        before_start_time_count (Union[Unset, str]):  Example: 5.
        after_end_time_count (Union[Unset, str]):  Example: 5.
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
            TimeseriesgridImportFromExternalDataSource]):
        convert_datum (Union[Unset, TimeseriesgridConvertDatum]):
        show_ensemble_member_ids (Union[Unset, TimeseriesgridShowEnsembleMemberIds]):
        use_display_units (Union[Unset, TimeseriesgridUseDisplayUnits]):
        show_vertical_profile (Union[Unset, TimeseriesgridShowVerticalProfile]):
        show_thresholds (Union[Unset, TimeseriesgridShowThresholds]):
        omit_missing (Union[Unset, TimeseriesgridOmitMissing]):
        omit_empty_time_series (Union[Unset, TimeseriesgridOmitEmptyTimeSeries]):
        only_manual_edits (Union[Unset, TimeseriesgridOnlyManualEdits]):
        only_headers (Union[Unset, TimeseriesgridOnlyHeaders]):
        only_forecasts (Union[Unset, TimeseriesgridOnlyForecasts]):
        show_statistics (Union[Unset, TimeseriesgridShowStatistics]):
        use_milliseconds (Union[Unset, TimeseriesgridUseMilliseconds]):
        show_products (Union[Unset, TimeseriesgridShowProducts]):
        download_as_file (Union[Unset, str]):
        document_format (Union[Unset, TimeseriesgridDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bbox=bbox,
        before_start_time_count=before_start_time_count,
        after_end_time_count=after_end_time_count,
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
        convert_datum=convert_datum,
        show_ensemble_member_ids=show_ensemble_member_ids,
        use_display_units=use_display_units,
        show_vertical_profile=show_vertical_profile,
        show_thresholds=show_thresholds,
        omit_missing=omit_missing,
        omit_empty_time_series=omit_empty_time_series,
        only_manual_edits=only_manual_edits,
        only_headers=only_headers,
        only_forecasts=only_forecasts,
        show_statistics=show_statistics,
        use_milliseconds=use_milliseconds,
        show_products=show_products,
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
    bbox: Union[Unset, str] = UNSET,
    before_start_time_count: Union[Unset, str] = UNSET,
    after_end_time_count: Union[Unset, str] = UNSET,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    layers: str,
    x: Union[Unset, str] = UNSET,
    y: Union[Unset, str] = UNSET,
    external_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    ensemble_id: Union[Unset, str] = UNSET,
    ensemble_member_id: Union[Unset, str] = UNSET,
    elevation: Union[Unset, str] = UNSET,
    import_from_external_data_source: Union[Unset, TimeseriesgridImportFromExternalDataSource] = UNSET,
    convert_datum: Union[Unset, TimeseriesgridConvertDatum] = UNSET,
    show_ensemble_member_ids: Union[Unset, TimeseriesgridShowEnsembleMemberIds] = UNSET,
    use_display_units: Union[Unset, TimeseriesgridUseDisplayUnits] = UNSET,
    show_vertical_profile: Union[Unset, TimeseriesgridShowVerticalProfile] = UNSET,
    show_thresholds: Union[Unset, TimeseriesgridShowThresholds] = UNSET,
    omit_missing: Union[Unset, TimeseriesgridOmitMissing] = UNSET,
    omit_empty_time_series: Union[Unset, TimeseriesgridOmitEmptyTimeSeries] = UNSET,
    only_manual_edits: Union[Unset, TimeseriesgridOnlyManualEdits] = UNSET,
    only_headers: Union[Unset, TimeseriesgridOnlyHeaders] = UNSET,
    only_forecasts: Union[Unset, TimeseriesgridOnlyForecasts] = UNSET,
    show_statistics: Union[Unset, TimeseriesgridShowStatistics] = UNSET,
    use_milliseconds: Union[Unset, TimeseriesgridUseMilliseconds] = UNSET,
    show_products: Union[Unset, TimeseriesgridShowProducts] = UNSET,
    download_as_file: Union[Unset, str] = UNSET,
    document_format: Union[Unset, TimeseriesgridDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get the timeseries containing the data from a grid cell for a request period

     Get the timeseries containing the data from a grid cell for a request period. The grid is specified
    by passing a layerId.<p>When requesting the timeseries in PI_JSON The grid cell is determined by
    specifying a x and y coordinate and a bounding box. Currently only EPSG:3857 is supported for the
    x,y, and bounding box coordinates. At least a layer, startTime, endTime, x,y and bounding box are
    required. The timeseries/grid endpoint is intended to be used together with the Delf-FEWS WMS
    service. Every layer that is provided by the WMS service, can be used with this endpoint. The
    visibleInTimeSeriesDisplay configuration is respected. If set to false (default is true), the
    timeseries will not be returned.
    It is also possible to get the grid data in Netcdf format using the PI_NETCDF documentFormat. In
    this case no bbox or x,y coordinates should be specified. Timeseries configured in a datalayer will
    be stored in the the same Netcdf file. There is no support for 3D data or track layers.

    Args:
        bbox (Union[Unset, str]):  Example:
            -1558755.612890017,4979850.04379049,1623657.8112034467,6709422.556884765.
        before_start_time_count (Union[Unset, str]):  Example: 5.
        after_end_time_count (Union[Unset, str]):  Example: 5.
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
            TimeseriesgridImportFromExternalDataSource]):
        convert_datum (Union[Unset, TimeseriesgridConvertDatum]):
        show_ensemble_member_ids (Union[Unset, TimeseriesgridShowEnsembleMemberIds]):
        use_display_units (Union[Unset, TimeseriesgridUseDisplayUnits]):
        show_vertical_profile (Union[Unset, TimeseriesgridShowVerticalProfile]):
        show_thresholds (Union[Unset, TimeseriesgridShowThresholds]):
        omit_missing (Union[Unset, TimeseriesgridOmitMissing]):
        omit_empty_time_series (Union[Unset, TimeseriesgridOmitEmptyTimeSeries]):
        only_manual_edits (Union[Unset, TimeseriesgridOnlyManualEdits]):
        only_headers (Union[Unset, TimeseriesgridOnlyHeaders]):
        only_forecasts (Union[Unset, TimeseriesgridOnlyForecasts]):
        show_statistics (Union[Unset, TimeseriesgridShowStatistics]):
        use_milliseconds (Union[Unset, TimeseriesgridUseMilliseconds]):
        show_products (Union[Unset, TimeseriesgridShowProducts]):
        download_as_file (Union[Unset, str]):
        document_format (Union[Unset, TimeseriesgridDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        bbox=bbox,
        before_start_time_count=before_start_time_count,
        after_end_time_count=after_end_time_count,
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
        convert_datum=convert_datum,
        show_ensemble_member_ids=show_ensemble_member_ids,
        use_display_units=use_display_units,
        show_vertical_profile=show_vertical_profile,
        show_thresholds=show_thresholds,
        omit_missing=omit_missing,
        omit_empty_time_series=omit_empty_time_series,
        only_manual_edits=only_manual_edits,
        only_headers=only_headers,
        only_forecasts=only_forecasts,
        show_statistics=show_statistics,
        use_milliseconds=use_milliseconds,
        show_products=show_products,
        download_as_file=download_as_file,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
