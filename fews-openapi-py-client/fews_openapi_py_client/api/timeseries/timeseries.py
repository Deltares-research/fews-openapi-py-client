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
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_id: str | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    parameter_ids: list[str] | Unset = UNSET,
    module_instance_ids: list[str] | Unset = UNSET,
    qualifier_ids: list[str] | Unset = UNSET,
    task_run_ids: list[str] | Unset = UNSET,
    statistical_function: str | Unset = UNSET,
    percentile_exceedance: str | Unset = UNSET,
    percentil_non_exceedance: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    before_start_time_count: str | Unset = UNSET,
    after_end_time_count: str | Unset = UNSET,
    start_creation_time: str | Unset = UNSET,
    end_creation_time: str | Unset = UNSET,
    forecast_count: str | Unset = UNSET,
    start_forecast_time: str | Unset = UNSET,
    end_forecast_time: str | Unset = UNSET,
    lead_time: str | Unset = UNSET,
    external_forecast_times: list[str] | Unset = UNSET,
    ensemble_id: str | Unset = UNSET,
    ensemble_member_id: str | Unset = UNSET,
    time_step_id: str | Unset = UNSET,
    thinning: str | Unset = UNSET,
    export_id_map: str | Unset = UNSET,
    export_unit_conversion_id: str | Unset = UNSET,
    time_zone_name: str | Unset = UNSET,
    time_series_ids: list[str] | Unset = UNSET,
    default_request_parameters_id: str | Unset = UNSET,
    resampling_method: TimeseriesResamplingMethod | Unset = UNSET,
    resampling_time_step_id: str | Unset = UNSET,
    resampling_omit_missing: TimeseriesResamplingOmitMissing | Unset = UNSET,
    download_as_file: str | Unset = UNSET,
    match_as_qualifier_set: TimeseriesMatchAsQualifierSet | Unset = UNSET,
    import_from_external_data_source: TimeseriesImportFromExternalDataSource | Unset = UNSET,
    convert_datum: TimeseriesConvertDatum | Unset = UNSET,
    convert_values_to_enumeration_labels: TimeseriesConvertValuesToEnumerationLabels | Unset = UNSET,
    show_ensemble_member_ids: TimeseriesShowEnsembleMemberIds | Unset = UNSET,
    use_display_units: TimeseriesUseDisplayUnits | Unset = UNSET,
    show_thresholds: TimeseriesShowThresholds | Unset = UNSET,
    omit_missing: TimeseriesOmitMissing | Unset = UNSET,
    omit_empty_time_series: TimeseriesOmitEmptyTimeSeries | Unset = UNSET,
    omit_original_reliable: TimeseriesOmitOriginalReliable | Unset = UNSET,
    omit_original_doubtful: TimeseriesOmitOriginalDoubtful | Unset = UNSET,
    omit_original_unreliable: TimeseriesOmitOriginalUnreliable | Unset = UNSET,
    omit_completed_reliable: TimeseriesOmitCompletedReliable | Unset = UNSET,
    omit_completed_doubtful: TimeseriesOmitCompletedDoubtful | Unset = UNSET,
    omit_completed_unreliable: TimeseriesOmitCompletedUnreliable | Unset = UNSET,
    omit_corrected_reliable: TimeseriesOmitCorrectedReliable | Unset = UNSET,
    omit_corrected_doubtful: TimeseriesOmitCorrectedDoubtful | Unset = UNSET,
    omit_corrected_unreliable: TimeseriesOmitCorrectedUnreliable | Unset = UNSET,
    only_manual_edits: TimeseriesOnlyManualEdits | Unset = UNSET,
    only_headers: TimeseriesOnlyHeaders | Unset = UNSET,
    only_forecasts: TimeseriesOnlyForecasts | Unset = UNSET,
    show_statistics: TimeseriesShowStatistics | Unset = UNSET,
    use_milliseconds: TimeseriesUseMilliseconds | Unset = UNSET,
    show_products: TimeseriesShowProducts | Unset = UNSET,
    time_series_type: TimeseriesTimeSeriesType | Unset = UNSET,
    document_format: TimeseriesDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["filterId"] = filter_id

    json_location_ids: list[str] | Unset = UNSET
    if not isinstance(location_ids, Unset):
        json_location_ids = location_ids

    params["locationIds"] = json_location_ids

    json_parameter_ids: list[str] | Unset = UNSET
    if not isinstance(parameter_ids, Unset):
        json_parameter_ids = parameter_ids

    params["parameterIds"] = json_parameter_ids

    json_module_instance_ids: list[str] | Unset = UNSET
    if not isinstance(module_instance_ids, Unset):
        json_module_instance_ids = module_instance_ids

    params["moduleInstanceIds"] = json_module_instance_ids

    json_qualifier_ids: list[str] | Unset = UNSET
    if not isinstance(qualifier_ids, Unset):
        json_qualifier_ids = qualifier_ids

    params["qualifierIds"] = json_qualifier_ids

    json_task_run_ids: list[str] | Unset = UNSET
    if not isinstance(task_run_ids, Unset):
        json_task_run_ids = task_run_ids

    params["taskRunIds"] = json_task_run_ids

    params["statisticalFunction"] = statistical_function

    params["percentileExceedance"] = percentile_exceedance

    params["percentilNonExceedance"] = percentil_non_exceedance

    json_start_time: str | Unset = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time
    params["startTime"] = json_start_time

    json_end_time: str | Unset = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time
    params["endTime"] = json_end_time

    params["beforeStartTimeCount"] = before_start_time_count

    params["afterEndTimeCount"] = after_end_time_count

    json_start_creation_time: str | Unset = UNSET
    if not isinstance(start_creation_time, Unset):
        json_start_creation_time = start_creation_time
    params["startCreationTime"] = json_start_creation_time

    json_end_creation_time: str | Unset = UNSET
    if not isinstance(end_creation_time, Unset):
        json_end_creation_time = end_creation_time
    params["endCreationTime"] = json_end_creation_time

    params["forecastCount"] = forecast_count

    json_start_forecast_time: str | Unset = UNSET
    if not isinstance(start_forecast_time, Unset):
        json_start_forecast_time = start_forecast_time
    params["startForecastTime"] = json_start_forecast_time

    json_end_forecast_time: str | Unset = UNSET
    if not isinstance(end_forecast_time, Unset):
        json_end_forecast_time = end_forecast_time
    params["endForecastTime"] = json_end_forecast_time

    params["leadTime"] = lead_time

    json_external_forecast_times: list[str] | Unset = UNSET
    if not isinstance(external_forecast_times, Unset):
        json_external_forecast_times = external_forecast_times

    params["externalForecastTimes"] = json_external_forecast_times

    params["ensembleId"] = ensemble_id

    params["ensembleMemberId"] = ensemble_member_id

    params["timeStepId"] = time_step_id

    params["thinning"] = thinning

    params["exportIdMap"] = export_id_map

    params["exportUnitConversionId"] = export_unit_conversion_id

    params["timeZoneName"] = time_zone_name

    json_time_series_ids: list[str] | Unset = UNSET
    if not isinstance(time_series_ids, Unset):
        json_time_series_ids = time_series_ids

    params["timeSeriesIds"] = json_time_series_ids

    params["defaultRequestParametersId"] = default_request_parameters_id

    json_resampling_method: str | Unset = UNSET
    if not isinstance(resampling_method, Unset):
        json_resampling_method = resampling_method.value

    params["resamplingMethod"] = json_resampling_method

    params["resamplingTimeStepId"] = resampling_time_step_id

    json_resampling_omit_missing: str | Unset = UNSET
    if not isinstance(resampling_omit_missing, Unset):
        json_resampling_omit_missing = resampling_omit_missing.value

    params["resamplingOmitMissing"] = json_resampling_omit_missing

    params["downloadAsFile"] = download_as_file

    json_match_as_qualifier_set: str | Unset = UNSET
    if not isinstance(match_as_qualifier_set, Unset):
        json_match_as_qualifier_set = match_as_qualifier_set.value

    params["matchAsQualifierSet"] = json_match_as_qualifier_set

    json_import_from_external_data_source: str | Unset = UNSET
    if not isinstance(import_from_external_data_source, Unset):
        json_import_from_external_data_source = import_from_external_data_source.value

    params["importFromExternalDataSource"] = json_import_from_external_data_source

    json_convert_datum: str | Unset = UNSET
    if not isinstance(convert_datum, Unset):
        json_convert_datum = convert_datum.value

    params["convertDatum"] = json_convert_datum

    json_convert_values_to_enumeration_labels: str | Unset = UNSET
    if not isinstance(convert_values_to_enumeration_labels, Unset):
        json_convert_values_to_enumeration_labels = convert_values_to_enumeration_labels.value

    params["convertValuesToEnumerationLabels"] = json_convert_values_to_enumeration_labels

    json_show_ensemble_member_ids: str | Unset = UNSET
    if not isinstance(show_ensemble_member_ids, Unset):
        json_show_ensemble_member_ids = show_ensemble_member_ids.value

    params["showEnsembleMemberIds"] = json_show_ensemble_member_ids

    json_use_display_units: str | Unset = UNSET
    if not isinstance(use_display_units, Unset):
        json_use_display_units = use_display_units.value

    params["useDisplayUnits"] = json_use_display_units

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

    json_omit_original_reliable: str | Unset = UNSET
    if not isinstance(omit_original_reliable, Unset):
        json_omit_original_reliable = omit_original_reliable.value

    params["omitOriginalReliable"] = json_omit_original_reliable

    json_omit_original_doubtful: str | Unset = UNSET
    if not isinstance(omit_original_doubtful, Unset):
        json_omit_original_doubtful = omit_original_doubtful.value

    params["omitOriginalDoubtful"] = json_omit_original_doubtful

    json_omit_original_unreliable: str | Unset = UNSET
    if not isinstance(omit_original_unreliable, Unset):
        json_omit_original_unreliable = omit_original_unreliable.value

    params["omitOriginalUnreliable"] = json_omit_original_unreliable

    json_omit_completed_reliable: str | Unset = UNSET
    if not isinstance(omit_completed_reliable, Unset):
        json_omit_completed_reliable = omit_completed_reliable.value

    params["omitCompletedReliable"] = json_omit_completed_reliable

    json_omit_completed_doubtful: str | Unset = UNSET
    if not isinstance(omit_completed_doubtful, Unset):
        json_omit_completed_doubtful = omit_completed_doubtful.value

    params["omitCompletedDoubtful"] = json_omit_completed_doubtful

    json_omit_completed_unreliable: str | Unset = UNSET
    if not isinstance(omit_completed_unreliable, Unset):
        json_omit_completed_unreliable = omit_completed_unreliable.value

    params["omitCompletedUnreliable"] = json_omit_completed_unreliable

    json_omit_corrected_reliable: str | Unset = UNSET
    if not isinstance(omit_corrected_reliable, Unset):
        json_omit_corrected_reliable = omit_corrected_reliable.value

    params["omitCorrectedReliable"] = json_omit_corrected_reliable

    json_omit_corrected_doubtful: str | Unset = UNSET
    if not isinstance(omit_corrected_doubtful, Unset):
        json_omit_corrected_doubtful = omit_corrected_doubtful.value

    params["omitCorrectedDoubtful"] = json_omit_corrected_doubtful

    json_omit_corrected_unreliable: str | Unset = UNSET
    if not isinstance(omit_corrected_unreliable, Unset):
        json_omit_corrected_unreliable = omit_corrected_unreliable.value

    params["omitCorrectedUnreliable"] = json_omit_corrected_unreliable

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

    json_time_series_type: str | Unset = UNSET
    if not isinstance(time_series_type, Unset):
        json_time_series_type = time_series_type.value

    params["timeSeriesType"] = json_time_series_type

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

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
    filter_id: str | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    parameter_ids: list[str] | Unset = UNSET,
    module_instance_ids: list[str] | Unset = UNSET,
    qualifier_ids: list[str] | Unset = UNSET,
    task_run_ids: list[str] | Unset = UNSET,
    statistical_function: str | Unset = UNSET,
    percentile_exceedance: str | Unset = UNSET,
    percentil_non_exceedance: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    before_start_time_count: str | Unset = UNSET,
    after_end_time_count: str | Unset = UNSET,
    start_creation_time: str | Unset = UNSET,
    end_creation_time: str | Unset = UNSET,
    forecast_count: str | Unset = UNSET,
    start_forecast_time: str | Unset = UNSET,
    end_forecast_time: str | Unset = UNSET,
    lead_time: str | Unset = UNSET,
    external_forecast_times: list[str] | Unset = UNSET,
    ensemble_id: str | Unset = UNSET,
    ensemble_member_id: str | Unset = UNSET,
    time_step_id: str | Unset = UNSET,
    thinning: str | Unset = UNSET,
    export_id_map: str | Unset = UNSET,
    export_unit_conversion_id: str | Unset = UNSET,
    time_zone_name: str | Unset = UNSET,
    time_series_ids: list[str] | Unset = UNSET,
    default_request_parameters_id: str | Unset = UNSET,
    resampling_method: TimeseriesResamplingMethod | Unset = UNSET,
    resampling_time_step_id: str | Unset = UNSET,
    resampling_omit_missing: TimeseriesResamplingOmitMissing | Unset = UNSET,
    download_as_file: str | Unset = UNSET,
    match_as_qualifier_set: TimeseriesMatchAsQualifierSet | Unset = UNSET,
    import_from_external_data_source: TimeseriesImportFromExternalDataSource | Unset = UNSET,
    convert_datum: TimeseriesConvertDatum | Unset = UNSET,
    convert_values_to_enumeration_labels: TimeseriesConvertValuesToEnumerationLabels | Unset = UNSET,
    show_ensemble_member_ids: TimeseriesShowEnsembleMemberIds | Unset = UNSET,
    use_display_units: TimeseriesUseDisplayUnits | Unset = UNSET,
    show_thresholds: TimeseriesShowThresholds | Unset = UNSET,
    omit_missing: TimeseriesOmitMissing | Unset = UNSET,
    omit_empty_time_series: TimeseriesOmitEmptyTimeSeries | Unset = UNSET,
    omit_original_reliable: TimeseriesOmitOriginalReliable | Unset = UNSET,
    omit_original_doubtful: TimeseriesOmitOriginalDoubtful | Unset = UNSET,
    omit_original_unreliable: TimeseriesOmitOriginalUnreliable | Unset = UNSET,
    omit_completed_reliable: TimeseriesOmitCompletedReliable | Unset = UNSET,
    omit_completed_doubtful: TimeseriesOmitCompletedDoubtful | Unset = UNSET,
    omit_completed_unreliable: TimeseriesOmitCompletedUnreliable | Unset = UNSET,
    omit_corrected_reliable: TimeseriesOmitCorrectedReliable | Unset = UNSET,
    omit_corrected_doubtful: TimeseriesOmitCorrectedDoubtful | Unset = UNSET,
    omit_corrected_unreliable: TimeseriesOmitCorrectedUnreliable | Unset = UNSET,
    only_manual_edits: TimeseriesOnlyManualEdits | Unset = UNSET,
    only_headers: TimeseriesOnlyHeaders | Unset = UNSET,
    only_forecasts: TimeseriesOnlyForecasts | Unset = UNSET,
    show_statistics: TimeseriesShowStatistics | Unset = UNSET,
    use_milliseconds: TimeseriesUseMilliseconds | Unset = UNSET,
    show_products: TimeseriesShowProducts | Unset = UNSET,
    time_series_type: TimeseriesTimeSeriesType | Unset = UNSET,
    document_format: TimeseriesDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
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
        filter_id (str | Unset):
        location_ids (list[str] | Unset): The parameter can be repeated
        parameter_ids (list[str] | Unset): The parameter can be repeated
        module_instance_ids (list[str] | Unset): The parameter can be repeated
        qualifier_ids (list[str] | Unset): The parameter can be repeated
        task_run_ids (list[str] | Unset): The parameter can be repeated
        statistical_function (str | Unset):
        percentile_exceedance (str | Unset):
        percentil_non_exceedance (str | Unset):
        start_time (str | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (str | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        before_start_time_count (str | Unset):  Example: 5.
        after_end_time_count (str | Unset):  Example: 5.
        start_creation_time (str | Unset): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        end_creation_time (str | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        forecast_count (str | Unset):  Example: 1.
        start_forecast_time (str | Unset): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        end_forecast_time (str | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        lead_time (str | Unset):  Example: 3600000.
        external_forecast_times (list[str] | Unset): The parameter can be repeated Example:
            2020-03-18T15:00:00Z.
        ensemble_id (str | Unset):
        ensemble_member_id (str | Unset):
        time_step_id (str | Unset):
        thinning (str | Unset):  Example: 15408668.
        export_id_map (str | Unset):
        export_unit_conversion_id (str | Unset):
        time_zone_name (str | Unset):
        time_series_ids (list[str] | Unset): The parameter can be repeated
        default_request_parameters_id (str | Unset):
        resampling_method (TimeseriesResamplingMethod | Unset):
        resampling_time_step_id (str | Unset):
        resampling_omit_missing (TimeseriesResamplingOmitMissing | Unset):
        download_as_file (str | Unset):
        match_as_qualifier_set (TimeseriesMatchAsQualifierSet | Unset):
        import_from_external_data_source (TimeseriesImportFromExternalDataSource | Unset):
        convert_datum (TimeseriesConvertDatum | Unset):
        convert_values_to_enumeration_labels (TimeseriesConvertValuesToEnumerationLabels | Unset):
        show_ensemble_member_ids (TimeseriesShowEnsembleMemberIds | Unset):
        use_display_units (TimeseriesUseDisplayUnits | Unset):
        show_thresholds (TimeseriesShowThresholds | Unset):
        omit_missing (TimeseriesOmitMissing | Unset):
        omit_empty_time_series (TimeseriesOmitEmptyTimeSeries | Unset):
        omit_original_reliable (TimeseriesOmitOriginalReliable | Unset):
        omit_original_doubtful (TimeseriesOmitOriginalDoubtful | Unset):
        omit_original_unreliable (TimeseriesOmitOriginalUnreliable | Unset):
        omit_completed_reliable (TimeseriesOmitCompletedReliable | Unset):
        omit_completed_doubtful (TimeseriesOmitCompletedDoubtful | Unset):
        omit_completed_unreliable (TimeseriesOmitCompletedUnreliable | Unset):
        omit_corrected_reliable (TimeseriesOmitCorrectedReliable | Unset):
        omit_corrected_doubtful (TimeseriesOmitCorrectedDoubtful | Unset):
        omit_corrected_unreliable (TimeseriesOmitCorrectedUnreliable | Unset):
        only_manual_edits (TimeseriesOnlyManualEdits | Unset):
        only_headers (TimeseriesOnlyHeaders | Unset):
        only_forecasts (TimeseriesOnlyForecasts | Unset):
        show_statistics (TimeseriesShowStatistics | Unset):
        use_milliseconds (TimeseriesUseMilliseconds | Unset):
        show_products (TimeseriesShowProducts | Unset):
        time_series_type (TimeseriesTimeSeriesType | Unset):
        document_format (TimeseriesDocumentFormat | Unset):
        document_version (str | Unset):

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
    filter_id: str | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    parameter_ids: list[str] | Unset = UNSET,
    module_instance_ids: list[str] | Unset = UNSET,
    qualifier_ids: list[str] | Unset = UNSET,
    task_run_ids: list[str] | Unset = UNSET,
    statistical_function: str | Unset = UNSET,
    percentile_exceedance: str | Unset = UNSET,
    percentil_non_exceedance: str | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    before_start_time_count: str | Unset = UNSET,
    after_end_time_count: str | Unset = UNSET,
    start_creation_time: str | Unset = UNSET,
    end_creation_time: str | Unset = UNSET,
    forecast_count: str | Unset = UNSET,
    start_forecast_time: str | Unset = UNSET,
    end_forecast_time: str | Unset = UNSET,
    lead_time: str | Unset = UNSET,
    external_forecast_times: list[str] | Unset = UNSET,
    ensemble_id: str | Unset = UNSET,
    ensemble_member_id: str | Unset = UNSET,
    time_step_id: str | Unset = UNSET,
    thinning: str | Unset = UNSET,
    export_id_map: str | Unset = UNSET,
    export_unit_conversion_id: str | Unset = UNSET,
    time_zone_name: str | Unset = UNSET,
    time_series_ids: list[str] | Unset = UNSET,
    default_request_parameters_id: str | Unset = UNSET,
    resampling_method: TimeseriesResamplingMethod | Unset = UNSET,
    resampling_time_step_id: str | Unset = UNSET,
    resampling_omit_missing: TimeseriesResamplingOmitMissing | Unset = UNSET,
    download_as_file: str | Unset = UNSET,
    match_as_qualifier_set: TimeseriesMatchAsQualifierSet | Unset = UNSET,
    import_from_external_data_source: TimeseriesImportFromExternalDataSource | Unset = UNSET,
    convert_datum: TimeseriesConvertDatum | Unset = UNSET,
    convert_values_to_enumeration_labels: TimeseriesConvertValuesToEnumerationLabels | Unset = UNSET,
    show_ensemble_member_ids: TimeseriesShowEnsembleMemberIds | Unset = UNSET,
    use_display_units: TimeseriesUseDisplayUnits | Unset = UNSET,
    show_thresholds: TimeseriesShowThresholds | Unset = UNSET,
    omit_missing: TimeseriesOmitMissing | Unset = UNSET,
    omit_empty_time_series: TimeseriesOmitEmptyTimeSeries | Unset = UNSET,
    omit_original_reliable: TimeseriesOmitOriginalReliable | Unset = UNSET,
    omit_original_doubtful: TimeseriesOmitOriginalDoubtful | Unset = UNSET,
    omit_original_unreliable: TimeseriesOmitOriginalUnreliable | Unset = UNSET,
    omit_completed_reliable: TimeseriesOmitCompletedReliable | Unset = UNSET,
    omit_completed_doubtful: TimeseriesOmitCompletedDoubtful | Unset = UNSET,
    omit_completed_unreliable: TimeseriesOmitCompletedUnreliable | Unset = UNSET,
    omit_corrected_reliable: TimeseriesOmitCorrectedReliable | Unset = UNSET,
    omit_corrected_doubtful: TimeseriesOmitCorrectedDoubtful | Unset = UNSET,
    omit_corrected_unreliable: TimeseriesOmitCorrectedUnreliable | Unset = UNSET,
    only_manual_edits: TimeseriesOnlyManualEdits | Unset = UNSET,
    only_headers: TimeseriesOnlyHeaders | Unset = UNSET,
    only_forecasts: TimeseriesOnlyForecasts | Unset = UNSET,
    show_statistics: TimeseriesShowStatistics | Unset = UNSET,
    use_milliseconds: TimeseriesUseMilliseconds | Unset = UNSET,
    show_products: TimeseriesShowProducts | Unset = UNSET,
    time_series_type: TimeseriesTimeSeriesType | Unset = UNSET,
    document_format: TimeseriesDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
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
        filter_id (str | Unset):
        location_ids (list[str] | Unset): The parameter can be repeated
        parameter_ids (list[str] | Unset): The parameter can be repeated
        module_instance_ids (list[str] | Unset): The parameter can be repeated
        qualifier_ids (list[str] | Unset): The parameter can be repeated
        task_run_ids (list[str] | Unset): The parameter can be repeated
        statistical_function (str | Unset):
        percentile_exceedance (str | Unset):
        percentil_non_exceedance (str | Unset):
        start_time (str | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (str | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        before_start_time_count (str | Unset):  Example: 5.
        after_end_time_count (str | Unset):  Example: 5.
        start_creation_time (str | Unset): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        end_creation_time (str | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        forecast_count (str | Unset):  Example: 1.
        start_forecast_time (str | Unset): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        end_forecast_time (str | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        lead_time (str | Unset):  Example: 3600000.
        external_forecast_times (list[str] | Unset): The parameter can be repeated Example:
            2020-03-18T15:00:00Z.
        ensemble_id (str | Unset):
        ensemble_member_id (str | Unset):
        time_step_id (str | Unset):
        thinning (str | Unset):  Example: 15408668.
        export_id_map (str | Unset):
        export_unit_conversion_id (str | Unset):
        time_zone_name (str | Unset):
        time_series_ids (list[str] | Unset): The parameter can be repeated
        default_request_parameters_id (str | Unset):
        resampling_method (TimeseriesResamplingMethod | Unset):
        resampling_time_step_id (str | Unset):
        resampling_omit_missing (TimeseriesResamplingOmitMissing | Unset):
        download_as_file (str | Unset):
        match_as_qualifier_set (TimeseriesMatchAsQualifierSet | Unset):
        import_from_external_data_source (TimeseriesImportFromExternalDataSource | Unset):
        convert_datum (TimeseriesConvertDatum | Unset):
        convert_values_to_enumeration_labels (TimeseriesConvertValuesToEnumerationLabels | Unset):
        show_ensemble_member_ids (TimeseriesShowEnsembleMemberIds | Unset):
        use_display_units (TimeseriesUseDisplayUnits | Unset):
        show_thresholds (TimeseriesShowThresholds | Unset):
        omit_missing (TimeseriesOmitMissing | Unset):
        omit_empty_time_series (TimeseriesOmitEmptyTimeSeries | Unset):
        omit_original_reliable (TimeseriesOmitOriginalReliable | Unset):
        omit_original_doubtful (TimeseriesOmitOriginalDoubtful | Unset):
        omit_original_unreliable (TimeseriesOmitOriginalUnreliable | Unset):
        omit_completed_reliable (TimeseriesOmitCompletedReliable | Unset):
        omit_completed_doubtful (TimeseriesOmitCompletedDoubtful | Unset):
        omit_completed_unreliable (TimeseriesOmitCompletedUnreliable | Unset):
        omit_corrected_reliable (TimeseriesOmitCorrectedReliable | Unset):
        omit_corrected_doubtful (TimeseriesOmitCorrectedDoubtful | Unset):
        omit_corrected_unreliable (TimeseriesOmitCorrectedUnreliable | Unset):
        only_manual_edits (TimeseriesOnlyManualEdits | Unset):
        only_headers (TimeseriesOnlyHeaders | Unset):
        only_forecasts (TimeseriesOnlyForecasts | Unset):
        show_statistics (TimeseriesShowStatistics | Unset):
        use_milliseconds (TimeseriesUseMilliseconds | Unset):
        show_products (TimeseriesShowProducts | Unset):
        time_series_type (TimeseriesTimeSeriesType | Unset):
        document_format (TimeseriesDocumentFormat | Unset):
        document_version (str | Unset):

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
