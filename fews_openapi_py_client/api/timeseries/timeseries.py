import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.timeseries_convert_datum import TimeseriesConvertDatum
from ...models.timeseries_convert_values_to_enumeration_labels import TimeseriesConvertValuesToEnumerationLabels
from ...models.timeseries_document_format import TimeseriesDocumentFormat
from ...models.timeseries_import_from_external_data_source import TimeseriesImportFromExternalDataSource
from ...models.timeseries_match_as_qualifier_set import TimeseriesMatchAsQualifierSet
from ...models.timeseries_omit_completed_doubtful import TimeseriesOmitCompletedDoubtful
from ...models.timeseries_omit_completed_reliable import TimeseriesOmitCompletedReliable
from ...models.timeseries_omit_completed_unreliable import TimeseriesOmitCompletedUnreliable
from ...models.timeseries_omit_corrected_doubtful import TimeseriesOmitCorrectedDoubtful
from ...models.timeseries_omit_corrected_reliable import TimeseriesOmitCorrectedReliable
from ...models.timeseries_omit_corrected_unreliable import TimeseriesOmitCorrectedUnreliable
from ...models.timeseries_omit_empty_time_series import TimeseriesOmitEmptyTimeSeries
from ...models.timeseries_omit_missing import TimeseriesOmitMissing
from ...models.timeseries_omit_original_doubtful import TimeseriesOmitOriginalDoubtful
from ...models.timeseries_omit_original_reliable import TimeseriesOmitOriginalReliable
from ...models.timeseries_omit_original_unreliable import TimeseriesOmitOriginalUnreliable
from ...models.timeseries_only_forecasts import TimeseriesOnlyForecasts
from ...models.timeseries_only_headers import TimeseriesOnlyHeaders
from ...models.timeseries_only_manual_edits import TimeseriesOnlyManualEdits
from ...models.timeseries_resampling_method import TimeseriesResamplingMethod
from ...models.timeseries_resampling_omit_missing import TimeseriesResamplingOmitMissing
from ...models.timeseries_show_ensemble_member_ids import TimeseriesShowEnsembleMemberIds
from ...models.timeseries_show_products import TimeseriesShowProducts
from ...models.timeseries_show_statistics import TimeseriesShowStatistics
from ...models.timeseries_show_thresholds import TimeseriesShowThresholds
from ...models.timeseries_time_series_type import TimeseriesTimeSeriesType
from ...models.timeseries_use_display_units import TimeseriesUseDisplayUnits
from ...models.timeseries_use_milliseconds import TimeseriesUseMilliseconds
from ...types import Response


def _get_kwargs(
    *,
    filter_id: None | str = None,
    location_ids: None | list[str] = None,
    parameter_ids: None | list[str] = None,
    module_instance_ids: None | list[str] = None,
    qualifier_ids: None | list[str] = None,
    task_run_ids: None | list[str] = None,
    statistical_function: None | str = None,
    percentile_exceedance: None | str = None,
    percentil_non_exceedance: None | str = None,
    start_time: None | datetime.datetime = None,
    end_time: None | datetime.datetime = None,
    before_start_time_count: None | str = None,
    after_end_time_count: None | str = None,
    start_creation_time: None | datetime.datetime = None,
    end_creation_time: None | datetime.datetime = None,
    forecast_count: None | str = None,
    start_forecast_time: None | datetime.datetime = None,
    end_forecast_time: None | datetime.datetime = None,
    lead_time: None | str = None,
    external_forecast_times: None | list[str] = None,
    ensemble_id: None | str = None,
    ensemble_member_id: None | str = None,
    time_step_id: None | str = None,
    thinning: None | str = None,
    export_id_map: None | str = None,
    export_unit_conversion_id: None | str = None,
    time_zone_name: None | str = None,
    time_series_ids: None | list[str] = None,
    default_request_parameters_id: None | str = None,
    resampling_method: None | TimeseriesResamplingMethod = None,
    resampling_time_step_id: None | str = None,
    resampling_omit_missing: None | TimeseriesResamplingOmitMissing = None,
    download_as_file: None | str = None,
    match_as_qualifier_set: None | TimeseriesMatchAsQualifierSet = None,
    import_from_external_data_source: None | TimeseriesImportFromExternalDataSource = None,
    convert_datum: None | TimeseriesConvertDatum = None,
    convert_values_to_enumeration_labels: None | TimeseriesConvertValuesToEnumerationLabels = None,
    show_ensemble_member_ids: None | TimeseriesShowEnsembleMemberIds = None,
    use_display_units: None | TimeseriesUseDisplayUnits = None,
    show_thresholds: None | TimeseriesShowThresholds = None,
    omit_missing: None | TimeseriesOmitMissing = None,
    omit_empty_time_series: None | TimeseriesOmitEmptyTimeSeries = None,
    omit_original_reliable: None | TimeseriesOmitOriginalReliable = None,
    omit_original_doubtful: None | TimeseriesOmitOriginalDoubtful = None,
    omit_original_unreliable: None | TimeseriesOmitOriginalUnreliable = None,
    omit_completed_reliable: None | TimeseriesOmitCompletedReliable = None,
    omit_completed_doubtful: None | TimeseriesOmitCompletedDoubtful = None,
    omit_completed_unreliable: None | TimeseriesOmitCompletedUnreliable = None,
    omit_corrected_reliable: None | TimeseriesOmitCorrectedReliable = None,
    omit_corrected_doubtful: None | TimeseriesOmitCorrectedDoubtful = None,
    omit_corrected_unreliable: None | TimeseriesOmitCorrectedUnreliable = None,
    only_manual_edits: None | TimeseriesOnlyManualEdits = None,
    only_headers: None | TimeseriesOnlyHeaders = None,
    only_forecasts: None | TimeseriesOnlyForecasts = None,
    show_statistics: None | TimeseriesShowStatistics = None,
    use_milliseconds: None | TimeseriesUseMilliseconds = None,
    show_products: None | TimeseriesShowProducts = None,
    time_series_type: None | TimeseriesTimeSeriesType = None,
    document_format: None | TimeseriesDocumentFormat = None,
    document_version: None | str = None,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["filterId"] = filter_id

    json_location_ids: None | list[str] = None
    if not isinstance(location_ids, None):
        json_location_ids = location_ids

    params["locationIds"] = json_location_ids

    json_parameter_ids: None | list[str] = None
    if not isinstance(parameter_ids, None):
        json_parameter_ids = parameter_ids

    params["parameterIds"] = json_parameter_ids

    json_module_instance_ids: None | list[str] = None
    if not isinstance(module_instance_ids, None):
        json_module_instance_ids = module_instance_ids

    params["moduleInstanceIds"] = json_module_instance_ids

    json_qualifier_ids: None | list[str] = None
    if not isinstance(qualifier_ids, None):
        json_qualifier_ids = qualifier_ids

    params["qualifierIds"] = json_qualifier_ids

    json_task_run_ids: None | list[str] = None
    if not isinstance(task_run_ids, None):
        json_task_run_ids = task_run_ids

    params["taskRunIds"] = json_task_run_ids

    params["statisticalFunction"] = statistical_function

    params["percentileExceedance"] = percentile_exceedance

    params["percentilNonExceedance"] = percentil_non_exceedance

    json_start_time: datetime.datetime | None = None
    if not isinstance(start_time, None):
        json_start_time = start_time.isoformat()
    
    params["startTime"] = json_start_time

    json_end_time: None | datetime.datetime = None
    if not isinstance(end_time, None):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params["beforeStartTimeCount"] = before_start_time_count

    params["afterEndTimeCount"] = after_end_time_count

    json_start_creation_time: None | datetime.datetime = None
    if not isinstance(start_creation_time, None):
        json_start_creation_time = start_creation_time.isoformat()
    params["startCreationTime"] = json_start_creation_time

    json_end_creation_time: None | datetime.datetime = None
    if not isinstance(end_creation_time, None):
        json_end_creation_time = end_creation_time.isoformat()
    params["endCreationTime"] = json_end_creation_time

    params["forecastCount"] = forecast_count

    json_start_forecast_time: None | datetime.datetime = None
    if not isinstance(start_forecast_time, None):
        json_start_forecast_time = start_forecast_time.isoformat()
    params["startForecastTime"] = json_start_forecast_time

    json_end_forecast_time: None | datetime.datetime = None
    if not isinstance(end_forecast_time, None):
        json_end_forecast_time = end_forecast_time.isoformat()
    params["endForecastTime"] = json_end_forecast_time

    params["leadTime"] = lead_time

    json_external_forecast_times: None | list[str] = None
    if not isinstance(external_forecast_times, None):
        json_external_forecast_times = external_forecast_times

    params["externalForecastTimes"] = json_external_forecast_times

    params["ensembleId"] = ensemble_id

    params["ensembleMemberId"] = ensemble_member_id

    params["timeStepId"] = time_step_id

    params["thinning"] = thinning

    params["exportIdMap"] = export_id_map

    params["exportUnitConversionId"] = export_unit_conversion_id

    params["timeZoneName"] = time_zone_name

    json_time_series_ids: None | list[str] = None
    if not isinstance(time_series_ids, None):
        json_time_series_ids = time_series_ids

    params["timeSeriesIds"] = json_time_series_ids

    params["defaultRequestParametersId"] = default_request_parameters_id

    json_resampling_method: None | str = None
    if not isinstance(resampling_method, None):
        json_resampling_method = resampling_method.value

    params["resamplingMethod"] = json_resampling_method

    params["resamplingTimeStepId"] = resampling_time_step_id

    json_resampling_omit_missing: None | str = None
    if not isinstance(resampling_omit_missing, None):
        json_resampling_omit_missing = resampling_omit_missing.value

    params["resamplingOmitMissing"] = json_resampling_omit_missing

    params["downloadAsFile"] = download_as_file

    json_match_as_qualifier_set: None | str = None
    if not isinstance(match_as_qualifier_set, None):
        json_match_as_qualifier_set = match_as_qualifier_set.value

    params["matchAsQualifierSet"] = json_match_as_qualifier_set

    json_import_from_external_data_source: None | str = None
    if not isinstance(import_from_external_data_source, None):
        json_import_from_external_data_source = import_from_external_data_source.value

    params["importFromExternalDataSource"] = json_import_from_external_data_source

    json_convert_datum: None | str = None
    if not isinstance(convert_datum, None):
        json_convert_datum = convert_datum.value

    params["convertDatum"] = json_convert_datum

    json_convert_values_to_enumeration_labels: None | str = None
    if not isinstance(convert_values_to_enumeration_labels, None):
        json_convert_values_to_enumeration_labels = convert_values_to_enumeration_labels.value

    params["convertValuesToEnumerationLabels"] = json_convert_values_to_enumeration_labels

    json_show_ensemble_member_ids: None | str = None
    if not isinstance(show_ensemble_member_ids, None):
        json_show_ensemble_member_ids = show_ensemble_member_ids.value

    params["showEnsembleMemberIds"] = json_show_ensemble_member_ids

    json_use_display_units: None | str = None
    if not isinstance(use_display_units, None):
        json_use_display_units = use_display_units.value

    params["useDisplayUnits"] = json_use_display_units

    json_show_thresholds: None | str = None
    if not isinstance(show_thresholds, None):
        json_show_thresholds = show_thresholds.value

    params["showThresholds"] = json_show_thresholds

    json_omit_missing: None | str = None
    if not isinstance(omit_missing, None):
        json_omit_missing = omit_missing.value

    params["omitMissing"] = json_omit_missing

    json_omit_empty_time_series: None | str = None
    if not isinstance(omit_empty_time_series, None):
        json_omit_empty_time_series = omit_empty_time_series.value

    params["omitEmptyTimeSeries"] = json_omit_empty_time_series

    json_omit_original_reliable: None | str = None
    if not isinstance(omit_original_reliable, None):
        json_omit_original_reliable = omit_original_reliable.value

    params["omitOriginalReliable"] = json_omit_original_reliable

    json_omit_original_doubtful: None | str = None
    if not isinstance(omit_original_doubtful, None):
        json_omit_original_doubtful = omit_original_doubtful.value

    params["omitOriginalDoubtful"] = json_omit_original_doubtful

    json_omit_original_unreliable: None | str = None
    if not isinstance(omit_original_unreliable, None):
        json_omit_original_unreliable = omit_original_unreliable.value

    params["omitOriginalUnreliable"] = json_omit_original_unreliable

    json_omit_completed_reliable: None | str = None
    if not isinstance(omit_completed_reliable, None):
        json_omit_completed_reliable = omit_completed_reliable.value

    params["omitCompletedReliable"] = json_omit_completed_reliable

    json_omit_completed_doubtful: None | str = None
    if not isinstance(omit_completed_doubtful, None):
        json_omit_completed_doubtful = omit_completed_doubtful.value

    params["omitCompletedDoubtful"] = json_omit_completed_doubtful

    json_omit_completed_unreliable: None | str = None
    if not isinstance(omit_completed_unreliable, None):
        json_omit_completed_unreliable = omit_completed_unreliable.value

    params["omitCompletedUnreliable"] = json_omit_completed_unreliable

    json_omit_corrected_reliable: None | str = None
    if not isinstance(omit_corrected_reliable, None):
        json_omit_corrected_reliable = omit_corrected_reliable.value

    params["omitCorrectedReliable"] = json_omit_corrected_reliable

    json_omit_corrected_doubtful: None | str = None
    if not isinstance(omit_corrected_doubtful, None):
        json_omit_corrected_doubtful = omit_corrected_doubtful.value

    params["omitCorrectedDoubtful"] = json_omit_corrected_doubtful

    json_omit_corrected_unreliable: None | str = None
    if not isinstance(omit_corrected_unreliable, None):
        json_omit_corrected_unreliable = omit_corrected_unreliable.value

    params["omitCorrectedUnreliable"] = json_omit_corrected_unreliable

    json_only_manual_edits: None | str = None
    if not isinstance(only_manual_edits, None):
        json_only_manual_edits = only_manual_edits.value

    params["onlyManualEdits"] = json_only_manual_edits

    json_only_headers: None | str = None
    if not isinstance(only_headers, None):
        json_only_headers = only_headers.value

    params["onlyHeaders"] = json_only_headers

    json_only_forecasts: None | str = None
    if not isinstance(only_forecasts, None):
        json_only_forecasts = only_forecasts.value

    params["onlyForecasts"] = json_only_forecasts

    json_show_statistics: None | str = None
    if not isinstance(show_statistics, None):
        json_show_statistics = show_statistics.value

    params["showStatistics"] = json_show_statistics

    json_use_milliseconds: None | str = None
    if not isinstance(use_milliseconds, None):
        json_use_milliseconds = use_milliseconds.value

    params["useMilliseconds"] = json_use_milliseconds

    json_show_products: None | str = None
    if not isinstance(show_products, None):
        json_show_products = show_products.value

    params["showProducts"] = json_show_products

    json_time_series_type: None | str = None
    if not isinstance(time_series_type, None):
        json_time_series_type = time_series_type.value

    params["timeSeriesType"] = json_time_series_type

    json_document_format: None | str = None
    if not isinstance(document_format, None):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not None and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/timeseries",
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
    filter_id: None | str = None,
    location_ids: None | list[str] = None,
    parameter_ids: None | list[str] = None,
    module_instance_ids: None | list[str] = None,
    qualifier_ids: None | list[str] = None,
    task_run_ids: None | list[str] = None,
    statistical_function: None | str = None,
    percentile_exceedance: None | str = None,
    percentil_non_exceedance: None | str = None,
    start_time: None | datetime.datetime = None,
    end_time: None | datetime.datetime = None,
    before_start_time_count: None | str = None,
    after_end_time_count: None | str = None,
    start_creation_time: None | datetime.datetime = None,
    end_creation_time: None | datetime.datetime = None,
    forecast_count: None | str = None,
    start_forecast_time: None | datetime.datetime = None,
    end_forecast_time: None | datetime.datetime = None,
    lead_time: None | str = None,
    external_forecast_times: None | list[str] = None,
    ensemble_id: None | str = None,
    ensemble_member_id: None | str = None,
    time_step_id: None | str = None,
    thinning: None | str = None,
    export_id_map: None | str = None,
    export_unit_conversion_id: None | str = None,
    time_zone_name: None | str = None,
    time_series_ids: None | list[str] = None,
    default_request_parameters_id: None | str = None,
    resampling_method: None | TimeseriesResamplingMethod = None,
    resampling_time_step_id: None | str = None,
    resampling_omit_missing: None | TimeseriesResamplingOmitMissing = None,
    download_as_file: None | str = None,
    match_as_qualifier_set: None | TimeseriesMatchAsQualifierSet = None,
    import_from_external_data_source: None | TimeseriesImportFromExternalDataSource = None,
    convert_datum: None | TimeseriesConvertDatum = None,
    convert_values_to_enumeration_labels: None | TimeseriesConvertValuesToEnumerationLabels = None,
    show_ensemble_member_ids: None | TimeseriesShowEnsembleMemberIds = None,
    use_display_units: None | TimeseriesUseDisplayUnits = None,
    show_thresholds: None | TimeseriesShowThresholds = None,
    omit_missing: None | TimeseriesOmitMissing = None,
    omit_empty_time_series: None | TimeseriesOmitEmptyTimeSeries = None,
    omit_original_reliable: None | TimeseriesOmitOriginalReliable = None,
    omit_original_doubtful: None | TimeseriesOmitOriginalDoubtful = None,
    omit_original_unreliable: None | TimeseriesOmitOriginalUnreliable = None,
    omit_completed_reliable: None | TimeseriesOmitCompletedReliable = None,
    omit_completed_doubtful: None | TimeseriesOmitCompletedDoubtful = None,
    omit_completed_unreliable: None | TimeseriesOmitCompletedUnreliable = None,
    omit_corrected_reliable: None | TimeseriesOmitCorrectedReliable = None,
    omit_corrected_doubtful: None | TimeseriesOmitCorrectedDoubtful = None,
    omit_corrected_unreliable: None | TimeseriesOmitCorrectedUnreliable = None,
    only_manual_edits: None | TimeseriesOnlyManualEdits = None,
    only_headers: None | TimeseriesOnlyHeaders = None,
    only_forecasts: None | TimeseriesOnlyForecasts = None,
    show_statistics: None | TimeseriesShowStatistics = None,
    use_milliseconds: None | TimeseriesUseMilliseconds = None,
    show_products: None | TimeseriesShowProducts = None,
    time_series_type: None | TimeseriesTimeSeriesType = None,
    document_format: None | TimeseriesDocumentFormat = None,
    document_version: None | str = None,
) -> Response[Any]:
    r"""Get timeseries that are part of the default filter

     Get timeseries that are part of the default filter. The HEAD request is also supported. It is
    recommended to use the HEAD request when using the taskRunIds parameter to check if the timeseries
    are available before using the GET request<p><h2>parameters</h2>
    Not all parameters can be combined. The following combinations are commonly used valid combinations
    of parameters. The main way to filter timeseries is by using filter ids or taskrun ids.<p>
    <table border='1'>
        <tr>
            <th>Use cases</th>
            <th>filterId</th>
            <th>taskRunIds</th>
            <th>startTime, endTime</th>
            <th>startCreationTime, endCreationTime</th>
            <th>startForecastTime, endForecastTime</th>
        </tr>
        <tr>
            <td>Apply a filter to the time series. The requested period will be set to the current time
    minus one day and one hour ago until the current time plus one day and one hour</td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Get all time series created by one or more taskRuns. All time steps of the matching time
    series are returned.</td>
            <td></td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Get the time series created by a taskrun and apply a filter from the Filters
    configuration. startTime and endTime cannot be specified. The complete time series will be returned.
    Since
                2020.01.
            </td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Apply a filter to the time series and return time steps that are in the startTime and
    endTime range. If the startTime or endTime doesn't match a timestamp of the time series, the closest
    time step before startTime and/or after endTime is returned as well.</td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Apply a filter to the time series. Only time series created during the startCreationTime
    and endCreationTime period will be returned. All time steps of the matching time series are
                returned.
            </td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td></td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
        </tr>
        <tr>
            <td>Apply a filter to the time series. Return only time series created during the creation
    time period. Only return timesteps in the startTime and endTime range.</td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
        </tr>
        <tr>
            <td>Apply a filter to the time series. Return only time series with external forecast times
    in the startForecastTime and endForecastTime period. Only return timesteps in the startTime and
                endTime range.
            </td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
        </tr>
        <tr>
            <td>Apply a filter to the time series. Return only time series with external forecast times
    in the startForecastTime and endForecastTime period that were created in the creation time period.
                Only return time steps in the startTime and endTime range.
            </td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
        </tr>
        <tr>
            <td>Apply a filter to the time series. Return only time series created during the creation
    time period. All time steps of the matching time series are returned. (before 2020.01 startTime and
                endTime had to be specified).
            </td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td></td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
        </tr>
        <tr>
            <td>Apply a filter to the time series. Return only time series with external forecast times
    in the startForecastTime and endForecastTime period. All time steps of the matching time series are
                returned.
            </td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td></td>
            <td></td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
        </tr>
        <tr>
            <td>Apply a filter to the time series. Return only time series created during the creation
    time period and with external forecast times in the startForecastTime and endForecastTime period.
    All
                time steps of the matching time series are returned..
            </td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td></td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
        </tr>
    </table>

    <h2>no data vs no time series</h2>
    If a timeseries query has matching timeseries sets a http 200 code will be returned and the headers
    of all matching time series sets will be returned.
    If there is any data for the requested period, the headers will be followed by the actual events
    that contain the data. So even if no data is available at all the headers are always returned.

    It is also possible that a timeseries query doesn't match any time series sets at all. This is seen
    as in invalid request and will result in a HTTP 400 response code.
    The following are examples of use cases where this might occur:
    <ul>
        <li>query parameters don't occur in filter. For example: the default filter has subfilters:
    filterA and filterB. filterA contains timeseries sets with module instance id moduleInstanceA and
    filterB contains timeseries sets with module instance id moduleInstanceB.
            If a timeseries query is done with parameters: filterId=filterA and
    moduleInstanceId=moduleInstanceB, this will return in a HTTP 400 response</li>
        <li>no timeseries for creation period. For example: if a query is using startCreationTime and
    endCreationTime and no time series have been produced during that period, this is seen as an invalid
    request and a HTTP 400 response is returned.</li>
    </ul>

    <h2>availability of new timeseries</h2>
    When new timeseries have been created, it can take some time before they can be found by the
    WebServices. The web services updates its indexes every second (every five seconds before 2023.01).
    Once the indexes have been updated, newly created time series can be found. So it typically can take
    a few seconds before newly created time series can be found. <h3>array of string</h3> For an array
    of strings the query parameter can be repeated, or added once with values in a comma separated
    fashion

    Args:
        filter_id (Union[None, str]):
        location_ids (Union[None, list[str]]): The parameter can be repeated
        parameter_ids (Union[None, list[str]]): The parameter can be repeated
        module_instance_ids (Union[None, list[str]]): The parameter can be repeated
        qualifier_ids (Union[None, list[str]]): The parameter can be repeated
        task_run_ids (Union[None, list[str]]): The parameter can be repeated
        statistical_function (Union[None, str]):
        percentile_exceedance (Union[None, str]):
        percentil_non_exceedance (Union[None, str]):
        start_time (Union[None, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (Union[None, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        before_start_time_count (Union[None, str]):  Example: 5.
        after_end_time_count (Union[None, str]):  Example: 5.
        start_creation_time (Union[None, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_creation_time (Union[None, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        forecast_count (Union[None, str]):  Example: 1.
        start_forecast_time (Union[None, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_forecast_time (Union[None, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        lead_time (Union[None, str]):  Example: 3600000.
        external_forecast_times (Union[None, list[str]]): The parameter can be repeated Example:
            2020-03-18T15:00:00Z.
        ensemble_id (Union[None, str]):
        ensemble_member_id (Union[None, str]):
        time_step_id (Union[None, str]):
        thinning (Union[None, str]):  Example: 15408668.
        export_id_map (Union[None, str]):
        export_unit_conversion_id (Union[None, str]):
        time_zone_name (Union[None, str]):
        time_series_ids (Union[None, list[str]]): The parameter can be repeated
        default_request_parameters_id (Union[None, str]):
        resampling_method (Union[None, TimeseriesResamplingMethod]):
        resampling_time_step_id (Union[None, str]):
        resampling_omit_missing (Union[None, TimeseriesResamplingOmitMissing]):
        download_as_file (Union[None, str]):
        match_as_qualifier_set (Union[None, TimeseriesMatchAsQualifierSet]):
        import_from_external_data_source (Union[None, TimeseriesImportFromExternalDataSource]):
        convert_datum (Union[None, TimeseriesConvertDatum]):
        convert_values_to_enumeration_labels (Union[None,
            TimeseriesConvertValuesToEnumerationLabels]):
        show_ensemble_member_ids (Union[None, TimeseriesShowEnsembleMemberIds]):
        use_display_units (Union[None, TimeseriesUseDisplayUnits]):
        show_thresholds (Union[None, TimeseriesShowThresholds]):
        omit_missing (Union[None, TimeseriesOmitMissing]):
        omit_empty_time_series (Union[None, TimeseriesOmitEmptyTimeSeries]):
        omit_original_reliable (Union[None, TimeseriesOmitOriginalReliable]):
        omit_original_doubtful (Union[None, TimeseriesOmitOriginalDoubtful]):
        omit_original_unreliable (Union[None, TimeseriesOmitOriginalUnreliable]):
        omit_completed_reliable (Union[None, TimeseriesOmitCompletedReliable]):
        omit_completed_doubtful (Union[None, TimeseriesOmitCompletedDoubtful]):
        omit_completed_unreliable (Union[None, TimeseriesOmitCompletedUnreliable]):
        omit_corrected_reliable (Union[None, TimeseriesOmitCorrectedReliable]):
        omit_corrected_doubtful (Union[None, TimeseriesOmitCorrectedDoubtful]):
        omit_corrected_unreliable (Union[None, TimeseriesOmitCorrectedUnreliable]):
        only_manual_edits (Union[None, TimeseriesOnlyManualEdits]):
        only_headers (Union[None, TimeseriesOnlyHeaders]):
        only_forecasts (Union[None, TimeseriesOnlyForecasts]):
        show_statistics (Union[None, TimeseriesShowStatistics]):
        use_milliseconds (Union[None, TimeseriesUseMilliseconds]):
        show_products (Union[None, TimeseriesShowProducts]):
        time_series_type (Union[None, TimeseriesTimeSeriesType]):
        document_format (Union[None, TimeseriesDocumentFormat]):
        document_version (Union[None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        filter_id=filter_id,
        location_ids=location_ids,
        parameter_ids=parameter_ids,
        module_instance_ids=module_instance_ids,
        qualifier_ids=qualifier_ids,
        task_run_ids=task_run_ids,
        statistical_function=statistical_function,
        percentile_exceedance=percentile_exceedance,
        percentil_non_exceedance=percentil_non_exceedance,
        start_time=start_time,
        end_time=end_time,
        before_start_time_count=before_start_time_count,
        after_end_time_count=after_end_time_count,
        start_creation_time=start_creation_time,
        end_creation_time=end_creation_time,
        forecast_count=forecast_count,
        start_forecast_time=start_forecast_time,
        end_forecast_time=end_forecast_time,
        lead_time=lead_time,
        external_forecast_times=external_forecast_times,
        ensemble_id=ensemble_id,
        ensemble_member_id=ensemble_member_id,
        time_step_id=time_step_id,
        thinning=thinning,
        export_id_map=export_id_map,
        export_unit_conversion_id=export_unit_conversion_id,
        time_zone_name=time_zone_name,
        time_series_ids=time_series_ids,
        default_request_parameters_id=default_request_parameters_id,
        resampling_method=resampling_method,
        resampling_time_step_id=resampling_time_step_id,
        resampling_omit_missing=resampling_omit_missing,
        download_as_file=download_as_file,
        match_as_qualifier_set=match_as_qualifier_set,
        import_from_external_data_source=import_from_external_data_source,
        convert_datum=convert_datum,
        convert_values_to_enumeration_labels=convert_values_to_enumeration_labels,
        show_ensemble_member_ids=show_ensemble_member_ids,
        use_display_units=use_display_units,
        show_thresholds=show_thresholds,
        omit_missing=omit_missing,
        omit_empty_time_series=omit_empty_time_series,
        omit_original_reliable=omit_original_reliable,
        omit_original_doubtful=omit_original_doubtful,
        omit_original_unreliable=omit_original_unreliable,
        omit_completed_reliable=omit_completed_reliable,
        omit_completed_doubtful=omit_completed_doubtful,
        omit_completed_unreliable=omit_completed_unreliable,
        omit_corrected_reliable=omit_corrected_reliable,
        omit_corrected_doubtful=omit_corrected_doubtful,
        omit_corrected_unreliable=omit_corrected_unreliable,
        only_manual_edits=only_manual_edits,
        only_headers=only_headers,
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
    client: AuthenticatedClient | Client,
    filter_id: None | str = None,
    location_ids: None | list[str] = None,
    parameter_ids: None | list[str] = None,
    module_instance_ids: None | list[str] = None,
    qualifier_ids: None | list[str] = None,
    task_run_ids: None | list[str] = None,
    statistical_function: None | str = None,
    percentile_exceedance: None | str = None,
    percentil_non_exceedance: None | str = None,
    start_time: None | datetime.datetime = None,
    end_time: None | datetime.datetime = None,
    before_start_time_count: None | str = None,
    after_end_time_count: None | str = None,
    start_creation_time: None | datetime.datetime = None,
    end_creation_time: None | datetime.datetime = None,
    forecast_count: None | str = None,
    start_forecast_time: None | datetime.datetime = None,
    end_forecast_time: None | datetime.datetime = None,
    lead_time: None | str = None,
    external_forecast_times: None | list[str] = None,
    ensemble_id: None | str = None,
    ensemble_member_id: None | str = None,
    time_step_id: None | str = None,
    thinning: None | str = None,
    export_id_map: None | str = None,
    export_unit_conversion_id: None | str = None,
    time_zone_name: None | str = None,
    time_series_ids: None | list[str] = None,
    default_request_parameters_id: None | str = None,
    resampling_method: None | TimeseriesResamplingMethod = None,
    resampling_time_step_id: None | str = None,
    resampling_omit_missing: None | TimeseriesResamplingOmitMissing = None,
    download_as_file: None | str = None,
    match_as_qualifier_set: None | TimeseriesMatchAsQualifierSet = None,
    import_from_external_data_source: None | TimeseriesImportFromExternalDataSource = None,
    convert_datum: None | TimeseriesConvertDatum = None,
    convert_values_to_enumeration_labels: None | TimeseriesConvertValuesToEnumerationLabels = None,
    show_ensemble_member_ids: None | TimeseriesShowEnsembleMemberIds = None,
    use_display_units: None | TimeseriesUseDisplayUnits = None,
    show_thresholds: None | TimeseriesShowThresholds = None,
    omit_missing: None | TimeseriesOmitMissing = None,
    omit_empty_time_series: None | TimeseriesOmitEmptyTimeSeries = None,
    omit_original_reliable: None | TimeseriesOmitOriginalReliable = None,
    omit_original_doubtful: None | TimeseriesOmitOriginalDoubtful = None,
    omit_original_unreliable: None | TimeseriesOmitOriginalUnreliable = None,
    omit_completed_reliable: None | TimeseriesOmitCompletedReliable = None,
    omit_completed_doubtful: None | TimeseriesOmitCompletedDoubtful = None,
    omit_completed_unreliable: None | TimeseriesOmitCompletedUnreliable = None,
    omit_corrected_reliable: None | TimeseriesOmitCorrectedReliable = None,
    omit_corrected_doubtful: None | TimeseriesOmitCorrectedDoubtful = None,
    omit_corrected_unreliable: None | TimeseriesOmitCorrectedUnreliable = None,
    only_manual_edits: None | TimeseriesOnlyManualEdits = None,
    only_headers: None | TimeseriesOnlyHeaders = None,
    only_forecasts: None | TimeseriesOnlyForecasts = None,
    show_statistics: None | TimeseriesShowStatistics = None,
    use_milliseconds: None | TimeseriesUseMilliseconds = None,
    show_products: None | TimeseriesShowProducts = None,
    time_series_type: None | TimeseriesTimeSeriesType = None,
    document_format: None | TimeseriesDocumentFormat = None,
    document_version: None | str = None,
) -> Response[Any]:
    r"""Get timeseries that are part of the default filter

     Get timeseries that are part of the default filter. The HEAD request is also supported. It is
    recommended to use the HEAD request when using the taskRunIds parameter to check if the timeseries
    are available before using the GET request<p><h2>parameters</h2>
    Not all parameters can be combined. The following combinations are commonly used valid combinations
    of parameters. The main way to filter timeseries is by using filter ids or taskrun ids.<p>
    <table border='1'>
        <tr>
            <th>Use cases</th>
            <th>filterId</th>
            <th>taskRunIds</th>
            <th>startTime, endTime</th>
            <th>startCreationTime, endCreationTime</th>
            <th>startForecastTime, endForecastTime</th>
        </tr>
        <tr>
            <td>Apply a filter to the time series. The requested period will be set to the current time
    minus one day and one hour ago until the current time plus one day and one hour</td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Get all time series created by one or more taskRuns. All time steps of the matching time
    series are returned.</td>
            <td></td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Get the time series created by a taskrun and apply a filter from the Filters
    configuration. startTime and endTime cannot be specified. The complete time series will be returned.
    Since
                2020.01.
            </td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Apply a filter to the time series and return time steps that are in the startTime and
    endTime range. If the startTime or endTime doesn't match a timestamp of the time series, the closest
    time step before startTime and/or after endTime is returned as well.</td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Apply a filter to the time series. Only time series created during the startCreationTime
    and endCreationTime period will be returned. All time steps of the matching time series are
                returned.
            </td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td></td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
        </tr>
        <tr>
            <td>Apply a filter to the time series. Return only time series created during the creation
    time period. Only return timesteps in the startTime and endTime range.</td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
        </tr>
        <tr>
            <td>Apply a filter to the time series. Return only time series with external forecast times
    in the startForecastTime and endForecastTime period. Only return timesteps in the startTime and
                endTime range.
            </td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
        </tr>
        <tr>
            <td>Apply a filter to the time series. Return only time series with external forecast times
    in the startForecastTime and endForecastTime period that were created in the creation time period.
                Only return time steps in the startTime and endTime range.
            </td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
        </tr>
        <tr>
            <td>Apply a filter to the time series. Return only time series created during the creation
    time period. All time steps of the matching time series are returned. (before 2020.01 startTime and
                endTime had to be specified).
            </td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td></td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
        </tr>
        <tr>
            <td>Apply a filter to the time series. Return only time series with external forecast times
    in the startForecastTime and endForecastTime period. All time steps of the matching time series are
                returned.
            </td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td></td>
            <td></td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
        </tr>
        <tr>
            <td>Apply a filter to the time series. Return only time series created during the creation
    time period and with external forecast times in the startForecastTime and endForecastTime period.
    All
                time steps of the matching time series are returned..
            </td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td></td>
            <td></td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
            <td  style=\"background-color: LightGray; text-align: center;\">&nbsp;X</td>
        </tr>
    </table>

    <h2>no data vs no time series</h2>
    If a timeseries query has matching timeseries sets a http 200 code will be returned and the headers
    of all matching time series sets will be returned.
    If there is any data for the requested period, the headers will be followed by the actual events
    that contain the data. So even if no data is available at all the headers are always returned.

    It is also possible that a timeseries query doesn't match any time series sets at all. This is seen
    as in invalid request and will result in a HTTP 400 response code.
    The following are examples of use cases where this might occur:
    <ul>
        <li>query parameters don't occur in filter. For example: the default filter has subfilters:
    filterA and filterB. filterA contains timeseries sets with module instance id moduleInstanceA and
    filterB contains timeseries sets with module instance id moduleInstanceB.
            If a timeseries query is done with parameters: filterId=filterA and
    moduleInstanceId=moduleInstanceB, this will return in a HTTP 400 response</li>
        <li>no timeseries for creation period. For example: if a query is using startCreationTime and
    endCreationTime and no time series have been produced during that period, this is seen as an invalid
    request and a HTTP 400 response is returned.</li>
    </ul>

    <h2>availability of new timeseries</h2>
    When new timeseries have been created, it can take some time before they can be found by the
    WebServices. The web services updates its indexes every second (every five seconds before 2023.01).
    Once the indexes have been updated, newly created time series can be found. So it typically can take
    a few seconds before newly created time series can be found. <h3>array of string</h3> For an array
    of strings the query parameter can be repeated, or added once with values in a comma separated
    fashion

    Args:
        filter_id (Union[None, str]):
        location_ids (Union[None, list[str]]): The parameter can be repeated
        parameter_ids (Union[None, list[str]]): The parameter can be repeated
        module_instance_ids (Union[None, list[str]]): The parameter can be repeated
        qualifier_ids (Union[None, list[str]]): The parameter can be repeated
        task_run_ids (Union[None, list[str]]): The parameter can be repeated
        statistical_function (Union[None, str]):
        percentile_exceedance (Union[None, str]):
        percentil_non_exceedance (Union[None, str]):
        start_time (Union[None, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (Union[None, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        before_start_time_count (Union[None, str]):  Example: 5.
        after_end_time_count (Union[None, str]):  Example: 5.
        start_creation_time (Union[None, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_creation_time (Union[None, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        forecast_count (Union[None, str]):  Example: 1.
        start_forecast_time (Union[None, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_forecast_time (Union[None, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        lead_time (Union[None, str]):  Example: 3600000.
        external_forecast_times (Union[None, list[str]]): The parameter can be repeated Example:
            2020-03-18T15:00:00Z.
        ensemble_id (Union[None, str]):
        ensemble_member_id (Union[None, str]):
        time_step_id (Union[None, str]):
        thinning (Union[None, str]):  Example: 15408668.
        export_id_map (Union[None, str]):
        export_unit_conversion_id (Union[None, str]):
        time_zone_name (Union[None, str]):
        time_series_ids (Union[None, list[str]]): The parameter can be repeated
        default_request_parameters_id (Union[None, str]):
        resampling_method (Union[None, TimeseriesResamplingMethod]):
        resampling_time_step_id (Union[None, str]):
        resampling_omit_missing (Union[None, TimeseriesResamplingOmitMissing]):
        download_as_file (Union[None, str]):
        match_as_qualifier_set (Union[None, TimeseriesMatchAsQualifierSet]):
        import_from_external_data_source (Union[None, TimeseriesImportFromExternalDataSource]):
        convert_datum (Union[None, TimeseriesConvertDatum]):
        convert_values_to_enumeration_labels (Union[None,
            TimeseriesConvertValuesToEnumerationLabels]):
        show_ensemble_member_ids (Union[None, TimeseriesShowEnsembleMemberIds]):
        use_display_units (Union[None, TimeseriesUseDisplayUnits]):
        show_thresholds (Union[None, TimeseriesShowThresholds]):
        omit_missing (Union[None, TimeseriesOmitMissing]):
        omit_empty_time_series (Union[None, TimeseriesOmitEmptyTimeSeries]):
        omit_original_reliable (Union[None, TimeseriesOmitOriginalReliable]):
        omit_original_doubtful (Union[None, TimeseriesOmitOriginalDoubtful]):
        omit_original_unreliable (Union[None, TimeseriesOmitOriginalUnreliable]):
        omit_completed_reliable (Union[None, TimeseriesOmitCompletedReliable]):
        omit_completed_doubtful (Union[None, TimeseriesOmitCompletedDoubtful]):
        omit_completed_unreliable (Union[None, TimeseriesOmitCompletedUnreliable]):
        omit_corrected_reliable (Union[None, TimeseriesOmitCorrectedReliable]):
        omit_corrected_doubtful (Union[None, TimeseriesOmitCorrectedDoubtful]):
        omit_corrected_unreliable (Union[None, TimeseriesOmitCorrectedUnreliable]):
        only_manual_edits (Union[None, TimeseriesOnlyManualEdits]):
        only_headers (Union[None, TimeseriesOnlyHeaders]):
        only_forecasts (Union[None, TimeseriesOnlyForecasts]):
        show_statistics (Union[None, TimeseriesShowStatistics]):
        use_milliseconds (Union[None, TimeseriesUseMilliseconds]):
        show_products (Union[None, TimeseriesShowProducts]):
        time_series_type (Union[None, TimeseriesTimeSeriesType]):
        document_format (Union[None, TimeseriesDocumentFormat]):
        document_version (Union[None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        filter_id=filter_id,
        location_ids=location_ids,
        parameter_ids=parameter_ids,
        module_instance_ids=module_instance_ids,
        qualifier_ids=qualifier_ids,
        task_run_ids=task_run_ids,
        statistical_function=statistical_function,
        percentile_exceedance=percentile_exceedance,
        percentil_non_exceedance=percentil_non_exceedance,
        start_time=start_time,
        end_time=end_time,
        before_start_time_count=before_start_time_count,
        after_end_time_count=after_end_time_count,
        start_creation_time=start_creation_time,
        end_creation_time=end_creation_time,
        forecast_count=forecast_count,
        start_forecast_time=start_forecast_time,
        end_forecast_time=end_forecast_time,
        lead_time=lead_time,
        external_forecast_times=external_forecast_times,
        ensemble_id=ensemble_id,
        ensemble_member_id=ensemble_member_id,
        time_step_id=time_step_id,
        thinning=thinning,
        export_id_map=export_id_map,
        export_unit_conversion_id=export_unit_conversion_id,
        time_zone_name=time_zone_name,
        time_series_ids=time_series_ids,
        default_request_parameters_id=default_request_parameters_id,
        resampling_method=resampling_method,
        resampling_time_step_id=resampling_time_step_id,
        resampling_omit_missing=resampling_omit_missing,
        download_as_file=download_as_file,
        match_as_qualifier_set=match_as_qualifier_set,
        import_from_external_data_source=import_from_external_data_source,
        convert_datum=convert_datum,
        convert_values_to_enumeration_labels=convert_values_to_enumeration_labels,
        show_ensemble_member_ids=show_ensemble_member_ids,
        use_display_units=use_display_units,
        show_thresholds=show_thresholds,
        omit_missing=omit_missing,
        omit_empty_time_series=omit_empty_time_series,
        omit_original_reliable=omit_original_reliable,
        omit_original_doubtful=omit_original_doubtful,
        omit_original_unreliable=omit_original_unreliable,
        omit_completed_reliable=omit_completed_reliable,
        omit_completed_doubtful=omit_completed_doubtful,
        omit_completed_unreliable=omit_completed_unreliable,
        omit_corrected_reliable=omit_corrected_reliable,
        omit_corrected_doubtful=omit_corrected_doubtful,
        omit_corrected_unreliable=omit_corrected_unreliable,
        only_manual_edits=only_manual_edits,
        only_headers=only_headers,
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
