import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.timeseriesdisplaygroups_convert_datum import TimeseriesdisplaygroupsConvertDatum
from ...models.timeseriesdisplaygroups_document_format import TimeseriesdisplaygroupsDocumentFormat
from ...models.timeseriesdisplaygroups_omit_empty_time_series import TimeseriesdisplaygroupsOmitEmptyTimeSeries
from ...models.timeseriesdisplaygroups_omit_missing import TimeseriesdisplaygroupsOmitMissing
from ...models.timeseriesdisplaygroups_only_forecasts import TimeseriesdisplaygroupsOnlyForecasts
from ...models.timeseriesdisplaygroups_only_headers import TimeseriesdisplaygroupsOnlyHeaders
from ...models.timeseriesdisplaygroups_only_manual_edits import TimeseriesdisplaygroupsOnlyManualEdits
from ...models.timeseriesdisplaygroups_show_ensemble_member_ids import TimeseriesdisplaygroupsShowEnsembleMemberIds
from ...models.timeseriesdisplaygroups_show_products import TimeseriesdisplaygroupsShowProducts
from ...models.timeseriesdisplaygroups_show_statistics import TimeseriesdisplaygroupsShowStatistics
from ...models.timeseriesdisplaygroups_show_thresholds import TimeseriesdisplaygroupsShowThresholds
from ...models.timeseriesdisplaygroups_time_series_type import TimeseriesdisplaygroupsTimeSeriesType
from ...models.timeseriesdisplaygroups_use_display_units import TimeseriesdisplaygroupsUseDisplayUnits
from ...models.timeseriesdisplaygroups_use_milliseconds import TimeseriesdisplaygroupsUseMilliseconds
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    plot_id: str,
    location_ids: Union[Unset, list[str]] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    thinning: Union[Unset, str] = UNSET,
    convert_datum: Union[Unset, TimeseriesdisplaygroupsConvertDatum] = UNSET,
    show_ensemble_member_ids: Union[Unset, TimeseriesdisplaygroupsShowEnsembleMemberIds] = UNSET,
    use_display_units: Union[Unset, TimeseriesdisplaygroupsUseDisplayUnits] = UNSET,
    show_thresholds: Union[Unset, TimeseriesdisplaygroupsShowThresholds] = UNSET,
    omit_missing: Union[Unset, TimeseriesdisplaygroupsOmitMissing] = UNSET,
    omit_empty_time_series: Union[Unset, TimeseriesdisplaygroupsOmitEmptyTimeSeries] = UNSET,
    only_headers: Union[Unset, TimeseriesdisplaygroupsOnlyHeaders] = UNSET,
    only_manual_edits: Union[Unset, TimeseriesdisplaygroupsOnlyManualEdits] = UNSET,
    only_forecasts: Union[Unset, TimeseriesdisplaygroupsOnlyForecasts] = UNSET,
    show_statistics: Union[Unset, TimeseriesdisplaygroupsShowStatistics] = UNSET,
    use_milliseconds: Union[Unset, TimeseriesdisplaygroupsUseMilliseconds] = UNSET,
    show_products: Union[Unset, TimeseriesdisplaygroupsShowProducts] = UNSET,
    time_series_type: Union[Unset, TimeseriesdisplaygroupsTimeSeriesType] = UNSET,
    document_format: Union[Unset, TimeseriesdisplaygroupsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["plotId"] = plot_id

    json_location_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(location_ids, Unset):
        json_location_ids = location_ids

    params["locationIds"] = json_location_ids

    json_start_time: Union[Unset, str] = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: Union[Unset, str] = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params["thinning"] = thinning

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

    json_only_headers: Union[Unset, str] = UNSET
    if not isinstance(only_headers, Unset):
        json_only_headers = only_headers.value

    params["onlyHeaders"] = json_only_headers

    json_only_manual_edits: Union[Unset, str] = UNSET
    if not isinstance(only_manual_edits, Unset):
        json_only_manual_edits = only_manual_edits.value

    params["onlyManualEdits"] = json_only_manual_edits

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

    json_time_series_type: Union[Unset, str] = UNSET
    if not isinstance(time_series_type, Unset):
        json_time_series_type = time_series_type.value

    params["timeSeriesType"] = json_time_series_type

    json_document_format: Union[Unset, str] = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/timeseries/displaygroups",
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
    plot_id: str,
    location_ids: Union[Unset, list[str]] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    thinning: Union[Unset, str] = UNSET,
    convert_datum: Union[Unset, TimeseriesdisplaygroupsConvertDatum] = UNSET,
    show_ensemble_member_ids: Union[Unset, TimeseriesdisplaygroupsShowEnsembleMemberIds] = UNSET,
    use_display_units: Union[Unset, TimeseriesdisplaygroupsUseDisplayUnits] = UNSET,
    show_thresholds: Union[Unset, TimeseriesdisplaygroupsShowThresholds] = UNSET,
    omit_missing: Union[Unset, TimeseriesdisplaygroupsOmitMissing] = UNSET,
    omit_empty_time_series: Union[Unset, TimeseriesdisplaygroupsOmitEmptyTimeSeries] = UNSET,
    only_headers: Union[Unset, TimeseriesdisplaygroupsOnlyHeaders] = UNSET,
    only_manual_edits: Union[Unset, TimeseriesdisplaygroupsOnlyManualEdits] = UNSET,
    only_forecasts: Union[Unset, TimeseriesdisplaygroupsOnlyForecasts] = UNSET,
    show_statistics: Union[Unset, TimeseriesdisplaygroupsShowStatistics] = UNSET,
    use_milliseconds: Union[Unset, TimeseriesdisplaygroupsUseMilliseconds] = UNSET,
    show_products: Union[Unset, TimeseriesdisplaygroupsShowProducts] = UNSET,
    time_series_type: Union[Unset, TimeseriesdisplaygroupsTimeSeriesType] = UNSET,
    document_format: Union[Unset, TimeseriesdisplaygroupsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Timeseries are filtered by the plotId from the DisplayGroups

     Timeseries are filtered by the plotId from the DisplayGroups.xml configuration in the
    SystemConfigFiles folder.<p>The TimeSeriesSets configured for the plotId will be used to filter the
    timeSeries. The line, area and clusteredBars elements are used when determining the relevant
    TimeSeriesSets. In case of forecasts, this means only the current forecast will be retrieved. It is
    not possible to request older forecasts. If no line, area or clusteredBars elements are used in the
    displayGroups.xml configuration, the TimeSeriesSets will not be applied.

    Args:
        plot_id (str):
        location_ids (Union[Unset, list[str]]): The parameter can be repeated
        start_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        thinning (Union[Unset, str]):  Example: 15408668.
        convert_datum (Union[Unset, TimeseriesdisplaygroupsConvertDatum]):
        show_ensemble_member_ids (Union[Unset, TimeseriesdisplaygroupsShowEnsembleMemberIds]):
        use_display_units (Union[Unset, TimeseriesdisplaygroupsUseDisplayUnits]):
        show_thresholds (Union[Unset, TimeseriesdisplaygroupsShowThresholds]):
        omit_missing (Union[Unset, TimeseriesdisplaygroupsOmitMissing]):
        omit_empty_time_series (Union[Unset, TimeseriesdisplaygroupsOmitEmptyTimeSeries]):
        only_headers (Union[Unset, TimeseriesdisplaygroupsOnlyHeaders]):
        only_manual_edits (Union[Unset, TimeseriesdisplaygroupsOnlyManualEdits]):
        only_forecasts (Union[Unset, TimeseriesdisplaygroupsOnlyForecasts]):
        show_statistics (Union[Unset, TimeseriesdisplaygroupsShowStatistics]):
        use_milliseconds (Union[Unset, TimeseriesdisplaygroupsUseMilliseconds]):
        show_products (Union[Unset, TimeseriesdisplaygroupsShowProducts]):
        time_series_type (Union[Unset, TimeseriesdisplaygroupsTimeSeriesType]):
        document_format (Union[Unset, TimeseriesdisplaygroupsDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        plot_id=plot_id,
        location_ids=location_ids,
        start_time=start_time,
        end_time=end_time,
        thinning=thinning,
        convert_datum=convert_datum,
        show_ensemble_member_ids=show_ensemble_member_ids,
        use_display_units=use_display_units,
        show_thresholds=show_thresholds,
        omit_missing=omit_missing,
        omit_empty_time_series=omit_empty_time_series,
        only_headers=only_headers,
        only_manual_edits=only_manual_edits,
        only_forecasts=only_forecasts,
        show_statistics=show_statistics,
        use_milliseconds=use_milliseconds,
        show_products=show_products,
        time_series_type=time_series_type,
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
    plot_id: str,
    location_ids: Union[Unset, list[str]] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    thinning: Union[Unset, str] = UNSET,
    convert_datum: Union[Unset, TimeseriesdisplaygroupsConvertDatum] = UNSET,
    show_ensemble_member_ids: Union[Unset, TimeseriesdisplaygroupsShowEnsembleMemberIds] = UNSET,
    use_display_units: Union[Unset, TimeseriesdisplaygroupsUseDisplayUnits] = UNSET,
    show_thresholds: Union[Unset, TimeseriesdisplaygroupsShowThresholds] = UNSET,
    omit_missing: Union[Unset, TimeseriesdisplaygroupsOmitMissing] = UNSET,
    omit_empty_time_series: Union[Unset, TimeseriesdisplaygroupsOmitEmptyTimeSeries] = UNSET,
    only_headers: Union[Unset, TimeseriesdisplaygroupsOnlyHeaders] = UNSET,
    only_manual_edits: Union[Unset, TimeseriesdisplaygroupsOnlyManualEdits] = UNSET,
    only_forecasts: Union[Unset, TimeseriesdisplaygroupsOnlyForecasts] = UNSET,
    show_statistics: Union[Unset, TimeseriesdisplaygroupsShowStatistics] = UNSET,
    use_milliseconds: Union[Unset, TimeseriesdisplaygroupsUseMilliseconds] = UNSET,
    show_products: Union[Unset, TimeseriesdisplaygroupsShowProducts] = UNSET,
    time_series_type: Union[Unset, TimeseriesdisplaygroupsTimeSeriesType] = UNSET,
    document_format: Union[Unset, TimeseriesdisplaygroupsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Timeseries are filtered by the plotId from the DisplayGroups

     Timeseries are filtered by the plotId from the DisplayGroups.xml configuration in the
    SystemConfigFiles folder.<p>The TimeSeriesSets configured for the plotId will be used to filter the
    timeSeries. The line, area and clusteredBars elements are used when determining the relevant
    TimeSeriesSets. In case of forecasts, this means only the current forecast will be retrieved. It is
    not possible to request older forecasts. If no line, area or clusteredBars elements are used in the
    displayGroups.xml configuration, the TimeSeriesSets will not be applied.

    Args:
        plot_id (str):
        location_ids (Union[Unset, list[str]]): The parameter can be repeated
        start_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        thinning (Union[Unset, str]):  Example: 15408668.
        convert_datum (Union[Unset, TimeseriesdisplaygroupsConvertDatum]):
        show_ensemble_member_ids (Union[Unset, TimeseriesdisplaygroupsShowEnsembleMemberIds]):
        use_display_units (Union[Unset, TimeseriesdisplaygroupsUseDisplayUnits]):
        show_thresholds (Union[Unset, TimeseriesdisplaygroupsShowThresholds]):
        omit_missing (Union[Unset, TimeseriesdisplaygroupsOmitMissing]):
        omit_empty_time_series (Union[Unset, TimeseriesdisplaygroupsOmitEmptyTimeSeries]):
        only_headers (Union[Unset, TimeseriesdisplaygroupsOnlyHeaders]):
        only_manual_edits (Union[Unset, TimeseriesdisplaygroupsOnlyManualEdits]):
        only_forecasts (Union[Unset, TimeseriesdisplaygroupsOnlyForecasts]):
        show_statistics (Union[Unset, TimeseriesdisplaygroupsShowStatistics]):
        use_milliseconds (Union[Unset, TimeseriesdisplaygroupsUseMilliseconds]):
        show_products (Union[Unset, TimeseriesdisplaygroupsShowProducts]):
        time_series_type (Union[Unset, TimeseriesdisplaygroupsTimeSeriesType]):
        document_format (Union[Unset, TimeseriesdisplaygroupsDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        plot_id=plot_id,
        location_ids=location_ids,
        start_time=start_time,
        end_time=end_time,
        thinning=thinning,
        convert_datum=convert_datum,
        show_ensemble_member_ids=show_ensemble_member_ids,
        use_display_units=use_display_units,
        show_thresholds=show_thresholds,
        omit_missing=omit_missing,
        omit_empty_time_series=omit_empty_time_series,
        only_headers=only_headers,
        only_manual_edits=only_manual_edits,
        only_forecasts=only_forecasts,
        show_statistics=show_statistics,
        use_milliseconds=use_milliseconds,
        show_products=show_products,
        time_series_type=time_series_type,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
