import datetime
from http import HTTPStatus
from typing import Any

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
from ...models.timeseriesgrid_point_cloud import TimeseriesgridPointCloud
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
    bbox: str | Unset = UNSET,
    before_start_time_count: str | Unset = UNSET,
    after_end_time_count: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    layers: str,
    x: str | Unset = UNSET,
    y: str | Unset = UNSET,
    external_forecast_time: datetime.datetime | Unset = UNSET,
    ensemble_id: str | Unset = UNSET,
    ensemble_member_id: str | Unset = UNSET,
    elevation: str | Unset = UNSET,
    point_cloud: TimeseriesgridPointCloud | Unset = UNSET,
    import_from_external_data_source: TimeseriesgridImportFromExternalDataSource | Unset = UNSET,
    convert_datum: TimeseriesgridConvertDatum | Unset = UNSET,
    show_ensemble_member_ids: TimeseriesgridShowEnsembleMemberIds | Unset = UNSET,
    use_display_units: TimeseriesgridUseDisplayUnits | Unset = UNSET,
    show_vertical_profile: TimeseriesgridShowVerticalProfile | Unset = UNSET,
    show_thresholds: TimeseriesgridShowThresholds | Unset = UNSET,
    omit_missing: TimeseriesgridOmitMissing | Unset = UNSET,
    omit_empty_time_series: TimeseriesgridOmitEmptyTimeSeries | Unset = UNSET,
    only_manual_edits: TimeseriesgridOnlyManualEdits | Unset = UNSET,
    only_headers: TimeseriesgridOnlyHeaders | Unset = UNSET,
    only_forecasts: TimeseriesgridOnlyForecasts | Unset = UNSET,
    show_statistics: TimeseriesgridShowStatistics | Unset = UNSET,
    use_milliseconds: TimeseriesgridUseMilliseconds | Unset = UNSET,
    show_products: TimeseriesgridShowProducts | Unset = UNSET,
    download_as_file: str | Unset = UNSET,
    document_format: TimeseriesgridDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["bbox"] = bbox

    params["beforeStartTimeCount"] = before_start_time_count

    params["afterEndTimeCount"] = after_end_time_count

    json_start_time: str | Unset = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: str | Unset = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params["layers"] = layers

    params["x"] = x

    params["y"] = y

    json_external_forecast_time: str | Unset = UNSET
    if not isinstance(external_forecast_time, Unset):
        json_external_forecast_time = external_forecast_time.isoformat()
    params["externalForecastTime"] = json_external_forecast_time

    params["ensembleId"] = ensemble_id

    params["ensembleMemberId"] = ensemble_member_id

    params["elevation"] = elevation

    json_point_cloud: str | Unset = UNSET
    if not isinstance(point_cloud, Unset):
        json_point_cloud = point_cloud.value

    params["pointCloud"] = json_point_cloud

    json_import_from_external_data_source: str | Unset = UNSET
    if not isinstance(import_from_external_data_source, Unset):
        json_import_from_external_data_source = import_from_external_data_source.value

    params["importFromExternalDataSource"] = json_import_from_external_data_source

    json_convert_datum: str | Unset = UNSET
    if not isinstance(convert_datum, Unset):
        json_convert_datum = convert_datum.value

    params["convertDatum"] = json_convert_datum

    json_show_ensemble_member_ids: str | Unset = UNSET
    if not isinstance(show_ensemble_member_ids, Unset):
        json_show_ensemble_member_ids = show_ensemble_member_ids.value

    params["showEnsembleMemberIds"] = json_show_ensemble_member_ids

    json_use_display_units: str | Unset = UNSET
    if not isinstance(use_display_units, Unset):
        json_use_display_units = use_display_units.value

    params["useDisplayUnits"] = json_use_display_units

    json_show_vertical_profile: str | Unset = UNSET
    if not isinstance(show_vertical_profile, Unset):
        json_show_vertical_profile = show_vertical_profile.value

    params["showVerticalProfile"] = json_show_vertical_profile

    json_show_thresholds: str | Unset = UNSET
    if not isinstance(show_thresholds, Unset):
        json_show_thresholds = show_thresholds.value

    params["showThresholds"] = json_show_thresholds

    json_omit_missing: str | Unset = UNSET
    if not isinstance(omit_missing, Unset):
        json_omit_missing = omit_missing.value

    params["omitMissing"] = json_omit_missing

    json_omit_empty_time_series: str | Unset = UNSET
    if not isinstance(omit_empty_time_series, Unset):
        json_omit_empty_time_series = omit_empty_time_series.value

    params["omitEmptyTimeSeries"] = json_omit_empty_time_series

    json_only_manual_edits: str | Unset = UNSET
    if not isinstance(only_manual_edits, Unset):
        json_only_manual_edits = only_manual_edits.value

    params["onlyManualEdits"] = json_only_manual_edits

    json_only_headers: str | Unset = UNSET
    if not isinstance(only_headers, Unset):
        json_only_headers = only_headers.value

    params["onlyHeaders"] = json_only_headers

    json_only_forecasts: str | Unset = UNSET
    if not isinstance(only_forecasts, Unset):
        json_only_forecasts = only_forecasts.value

    params["onlyForecasts"] = json_only_forecasts

    json_show_statistics: str | Unset = UNSET
    if not isinstance(show_statistics, Unset):
        json_show_statistics = show_statistics.value

    params["showStatistics"] = json_show_statistics

    json_use_milliseconds: str | Unset = UNSET
    if not isinstance(use_milliseconds, Unset):
        json_use_milliseconds = use_milliseconds.value

    params["useMilliseconds"] = json_use_milliseconds

    json_show_products: str | Unset = UNSET
    if not isinstance(show_products, Unset):
        json_show_products = show_products.value

    params["showProducts"] = json_show_products

    params["downloadAsFile"] = download_as_file

    json_document_format: str | Unset = UNSET
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
    bbox: str | Unset = UNSET,
    before_start_time_count: str | Unset = UNSET,
    after_end_time_count: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    layers: str,
    x: str | Unset = UNSET,
    y: str | Unset = UNSET,
    external_forecast_time: datetime.datetime | Unset = UNSET,
    ensemble_id: str | Unset = UNSET,
    ensemble_member_id: str | Unset = UNSET,
    elevation: str | Unset = UNSET,
    point_cloud: TimeseriesgridPointCloud | Unset = UNSET,
    import_from_external_data_source: TimeseriesgridImportFromExternalDataSource | Unset = UNSET,
    convert_datum: TimeseriesgridConvertDatum | Unset = UNSET,
    show_ensemble_member_ids: TimeseriesgridShowEnsembleMemberIds | Unset = UNSET,
    use_display_units: TimeseriesgridUseDisplayUnits | Unset = UNSET,
    show_vertical_profile: TimeseriesgridShowVerticalProfile | Unset = UNSET,
    show_thresholds: TimeseriesgridShowThresholds | Unset = UNSET,
    omit_missing: TimeseriesgridOmitMissing | Unset = UNSET,
    omit_empty_time_series: TimeseriesgridOmitEmptyTimeSeries | Unset = UNSET,
    only_manual_edits: TimeseriesgridOnlyManualEdits | Unset = UNSET,
    only_headers: TimeseriesgridOnlyHeaders | Unset = UNSET,
    only_forecasts: TimeseriesgridOnlyForecasts | Unset = UNSET,
    show_statistics: TimeseriesgridShowStatistics | Unset = UNSET,
    use_milliseconds: TimeseriesgridUseMilliseconds | Unset = UNSET,
    show_products: TimeseriesgridShowProducts | Unset = UNSET,
    download_as_file: str | Unset = UNSET,
    document_format: TimeseriesgridDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get the timeseries containing the data from a grid cell for a request period

     Get the timeseries containing the data from a grid cell for a request period. The grid is specified
    by passing a layerId. For the PI_NETCDF format the complete grid can be downloaded for external
    forecasts.<p>When requesting the timeseries in PI_JSON The grid cell is determined by specifying a x
    and y coordinate and a bounding box. Currently only EPSG:3857 is supported for the x,y, and bounding
    box coordinates. At least a layer, startTime, endTime, x,y and bounding box are required. The
    timeseries/grid endpoint is intended to be used together with the Delf-FEWS WMS service. Every layer
    that is provided by the WMS service, can be used with this endpoint. The visibleInTimeSeriesDisplay
    configuration is respected. If set to false (default is true), the timeseries will not be returned.
    It is also possible to get the grid data in Netcdf format using the PI_NETCDF documentFormat. In
    this case no bbox or x,y coordinates should be specified. Timeseries configured in a datalayer will
    be stored in the the same Netcdf file. If the externalForecastTime is specified or a layer only
    contains external forecasts and the startDate and endDate are not specified, the complete forecast
    will be downloaded. There is no support for 3D data or track layers.

    Args:
        bbox (str | Unset):  Example:
            -1558755.612890017,4979850.04379049,1623657.8112034467,6709422.556884765.
        before_start_time_count (str | Unset):  Example: 5.
        after_end_time_count (str | Unset):  Example: 5.
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        layers (str):  Example: Temp_forecast.
        x (str | Unset):  Example: 458757.12883912364.
        y (str | Unset):  Example: 5811252.569955047.
        external_forecast_time (datetime.datetime | Unset): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        ensemble_id (str | Unset):
        ensemble_member_id (str | Unset):
        elevation (str | Unset):
        point_cloud (TimeseriesgridPointCloud | Unset):
        import_from_external_data_source (TimeseriesgridImportFromExternalDataSource | Unset):
        convert_datum (TimeseriesgridConvertDatum | Unset):
        show_ensemble_member_ids (TimeseriesgridShowEnsembleMemberIds | Unset):
        use_display_units (TimeseriesgridUseDisplayUnits | Unset):
        show_vertical_profile (TimeseriesgridShowVerticalProfile | Unset):
        show_thresholds (TimeseriesgridShowThresholds | Unset):
        omit_missing (TimeseriesgridOmitMissing | Unset):
        omit_empty_time_series (TimeseriesgridOmitEmptyTimeSeries | Unset):
        only_manual_edits (TimeseriesgridOnlyManualEdits | Unset):
        only_headers (TimeseriesgridOnlyHeaders | Unset):
        only_forecasts (TimeseriesgridOnlyForecasts | Unset):
        show_statistics (TimeseriesgridShowStatistics | Unset):
        use_milliseconds (TimeseriesgridUseMilliseconds | Unset):
        show_products (TimeseriesgridShowProducts | Unset):
        download_as_file (str | Unset):
        document_format (TimeseriesgridDocumentFormat | Unset):
        document_version (str | Unset):

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
        point_cloud=point_cloud,
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
    client: AuthenticatedClient | Client,
    bbox: str | Unset = UNSET,
    before_start_time_count: str | Unset = UNSET,
    after_end_time_count: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    layers: str,
    x: str | Unset = UNSET,
    y: str | Unset = UNSET,
    external_forecast_time: datetime.datetime | Unset = UNSET,
    ensemble_id: str | Unset = UNSET,
    ensemble_member_id: str | Unset = UNSET,
    elevation: str | Unset = UNSET,
    point_cloud: TimeseriesgridPointCloud | Unset = UNSET,
    import_from_external_data_source: TimeseriesgridImportFromExternalDataSource | Unset = UNSET,
    convert_datum: TimeseriesgridConvertDatum | Unset = UNSET,
    show_ensemble_member_ids: TimeseriesgridShowEnsembleMemberIds | Unset = UNSET,
    use_display_units: TimeseriesgridUseDisplayUnits | Unset = UNSET,
    show_vertical_profile: TimeseriesgridShowVerticalProfile | Unset = UNSET,
    show_thresholds: TimeseriesgridShowThresholds | Unset = UNSET,
    omit_missing: TimeseriesgridOmitMissing | Unset = UNSET,
    omit_empty_time_series: TimeseriesgridOmitEmptyTimeSeries | Unset = UNSET,
    only_manual_edits: TimeseriesgridOnlyManualEdits | Unset = UNSET,
    only_headers: TimeseriesgridOnlyHeaders | Unset = UNSET,
    only_forecasts: TimeseriesgridOnlyForecasts | Unset = UNSET,
    show_statistics: TimeseriesgridShowStatistics | Unset = UNSET,
    use_milliseconds: TimeseriesgridUseMilliseconds | Unset = UNSET,
    show_products: TimeseriesgridShowProducts | Unset = UNSET,
    download_as_file: str | Unset = UNSET,
    document_format: TimeseriesgridDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get the timeseries containing the data from a grid cell for a request period

     Get the timeseries containing the data from a grid cell for a request period. The grid is specified
    by passing a layerId. For the PI_NETCDF format the complete grid can be downloaded for external
    forecasts.<p>When requesting the timeseries in PI_JSON The grid cell is determined by specifying a x
    and y coordinate and a bounding box. Currently only EPSG:3857 is supported for the x,y, and bounding
    box coordinates. At least a layer, startTime, endTime, x,y and bounding box are required. The
    timeseries/grid endpoint is intended to be used together with the Delf-FEWS WMS service. Every layer
    that is provided by the WMS service, can be used with this endpoint. The visibleInTimeSeriesDisplay
    configuration is respected. If set to false (default is true), the timeseries will not be returned.
    It is also possible to get the grid data in Netcdf format using the PI_NETCDF documentFormat. In
    this case no bbox or x,y coordinates should be specified. Timeseries configured in a datalayer will
    be stored in the the same Netcdf file. If the externalForecastTime is specified or a layer only
    contains external forecasts and the startDate and endDate are not specified, the complete forecast
    will be downloaded. There is no support for 3D data or track layers.

    Args:
        bbox (str | Unset):  Example:
            -1558755.612890017,4979850.04379049,1623657.8112034467,6709422.556884765.
        before_start_time_count (str | Unset):  Example: 5.
        after_end_time_count (str | Unset):  Example: 5.
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        layers (str):  Example: Temp_forecast.
        x (str | Unset):  Example: 458757.12883912364.
        y (str | Unset):  Example: 5811252.569955047.
        external_forecast_time (datetime.datetime | Unset): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        ensemble_id (str | Unset):
        ensemble_member_id (str | Unset):
        elevation (str | Unset):
        point_cloud (TimeseriesgridPointCloud | Unset):
        import_from_external_data_source (TimeseriesgridImportFromExternalDataSource | Unset):
        convert_datum (TimeseriesgridConvertDatum | Unset):
        show_ensemble_member_ids (TimeseriesgridShowEnsembleMemberIds | Unset):
        use_display_units (TimeseriesgridUseDisplayUnits | Unset):
        show_vertical_profile (TimeseriesgridShowVerticalProfile | Unset):
        show_thresholds (TimeseriesgridShowThresholds | Unset):
        omit_missing (TimeseriesgridOmitMissing | Unset):
        omit_empty_time_series (TimeseriesgridOmitEmptyTimeSeries | Unset):
        only_manual_edits (TimeseriesgridOnlyManualEdits | Unset):
        only_headers (TimeseriesgridOnlyHeaders | Unset):
        only_forecasts (TimeseriesgridOnlyForecasts | Unset):
        show_statistics (TimeseriesgridShowStatistics | Unset):
        use_milliseconds (TimeseriesgridUseMilliseconds | Unset):
        show_products (TimeseriesgridShowProducts | Unset):
        download_as_file (str | Unset):
        document_format (TimeseriesgridDocumentFormat | Unset):
        document_version (str | Unset):

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
        point_cloud=point_cloud,
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
