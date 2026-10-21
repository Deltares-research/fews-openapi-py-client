import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.filtersactions_convert_datum import FiltersactionsConvertDatum
from ...models.filtersactions_current_forecasts_always_visible import FiltersactionsCurrentForecastsAlwaysVisible
from ...models.filtersactions_document_format import FiltersactionsDocumentFormat
from ...models.filtersactions_full_data_period import FiltersactionsFullDataPeriod
from ...models.filtersactions_include_non_resampled import FiltersactionsIncludeNonResampled
from ...models.filtersactions_resampling_methods import FiltersactionsResamplingMethods
from ...models.filtersactions_resampling_omit_missing import FiltersactionsResamplingOmitMissing
from ...models.filtersactions_use_display_units import FiltersactionsUseDisplayUnits
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_id: str | Unset = UNSET,
    parameter_group_id: str | Unset = UNSET,
    parameter_ids: list[str] | Unset = UNSET,
    module_instance_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    time_zero: str | Unset = UNSET,
    resampling_methods: FiltersactionsResamplingMethods | Unset = UNSET,
    resampling_time_step_ids: list[str] | Unset = UNSET,
    resampling_omit_missing: FiltersactionsResamplingOmitMissing | Unset = UNSET,
    include_non_resampled: FiltersactionsIncludeNonResampled | Unset = UNSET,
    use_display_units: FiltersactionsUseDisplayUnits | Unset = UNSET,
    convert_datum: FiltersactionsConvertDatum | Unset = UNSET,
    start_forecast_time: datetime.datetime | Unset = UNSET,
    end_forecast_time: datetime.datetime | Unset = UNSET,
    forecast_count: str | Unset = UNSET,
    full_data_period: FiltersactionsFullDataPeriod | Unset = UNSET,
    task_run_ids: list[str] | Unset = UNSET,
    current_forecasts_always_visible: FiltersactionsCurrentForecastsAlwaysVisible | Unset = UNSET,
    document_format: FiltersactionsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["filterId"] = filter_id

    params["parameterGroupId"] = parameter_group_id

    json_parameter_ids: list[str] | Unset = UNSET
    if not isinstance(parameter_ids, Unset):
        json_parameter_ids = parameter_ids

    params["parameterIds"] = json_parameter_ids

    json_module_instance_ids: list[str] | Unset = UNSET
    if not isinstance(module_instance_ids, Unset):
        json_module_instance_ids = module_instance_ids

    params["moduleInstanceIds"] = json_module_instance_ids

    json_location_ids: list[str] | Unset = UNSET
    if not isinstance(location_ids, Unset):
        json_location_ids = location_ids

    params["locationIds"] = json_location_ids

    params["timeZero"] = time_zero

    json_resampling_methods: str | Unset = UNSET
    if not isinstance(resampling_methods, Unset):
        json_resampling_methods = resampling_methods.value

    params["resamplingMethods"] = json_resampling_methods

    json_resampling_time_step_ids: list[str] | Unset = UNSET
    if not isinstance(resampling_time_step_ids, Unset):
        json_resampling_time_step_ids = resampling_time_step_ids

    params["resamplingTimeStepIds"] = json_resampling_time_step_ids

    json_resampling_omit_missing: str | Unset = UNSET
    if not isinstance(resampling_omit_missing, Unset):
        json_resampling_omit_missing = resampling_omit_missing.value

    params["resamplingOmitMissing"] = json_resampling_omit_missing

    json_include_non_resampled: str | Unset = UNSET
    if not isinstance(include_non_resampled, Unset):
        json_include_non_resampled = include_non_resampled.value

    params["includeNonResampled"] = json_include_non_resampled

    json_use_display_units: str | Unset = UNSET
    if not isinstance(use_display_units, Unset):
        json_use_display_units = use_display_units.value

    params["useDisplayUnits"] = json_use_display_units

    json_convert_datum: str | Unset = UNSET
    if not isinstance(convert_datum, Unset):
        json_convert_datum = convert_datum.value

    params["convertDatum"] = json_convert_datum

    json_start_forecast_time: str | Unset = UNSET
    if not isinstance(start_forecast_time, Unset):
        json_start_forecast_time = start_forecast_time.isoformat()
    params["startForecastTime"] = json_start_forecast_time

    json_end_forecast_time: str | Unset = UNSET
    if not isinstance(end_forecast_time, Unset):
        json_end_forecast_time = end_forecast_time.isoformat()
    params["endForecastTime"] = json_end_forecast_time

    params["forecastCount"] = forecast_count

    json_full_data_period: str | Unset = UNSET
    if not isinstance(full_data_period, Unset):
        json_full_data_period = full_data_period.value

    params["fullDataPeriod"] = json_full_data_period

    json_task_run_ids: list[str] | Unset = UNSET
    if not isinstance(task_run_ids, Unset):
        json_task_run_ids = task_run_ids

    params["taskRunIds"] = json_task_run_ids

    json_current_forecasts_always_visible: str | Unset = UNSET
    if not isinstance(current_forecasts_always_visible, Unset):
        json_current_forecasts_always_visible = current_forecasts_always_visible.value

    params["currentForecastsAlwaysVisible"] = json_current_forecasts_always_visible

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/filters/actions",
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
    parameter_group_id: str | Unset = UNSET,
    parameter_ids: list[str] | Unset = UNSET,
    module_instance_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    time_zero: str | Unset = UNSET,
    resampling_methods: FiltersactionsResamplingMethods | Unset = UNSET,
    resampling_time_step_ids: list[str] | Unset = UNSET,
    resampling_omit_missing: FiltersactionsResamplingOmitMissing | Unset = UNSET,
    include_non_resampled: FiltersactionsIncludeNonResampled | Unset = UNSET,
    use_display_units: FiltersactionsUseDisplayUnits | Unset = UNSET,
    convert_datum: FiltersactionsConvertDatum | Unset = UNSET,
    start_forecast_time: datetime.datetime | Unset = UNSET,
    end_forecast_time: datetime.datetime | Unset = UNSET,
    forecast_count: str | Unset = UNSET,
    full_data_period: FiltersactionsFullDataPeriod | Unset = UNSET,
    task_run_ids: list[str] | Unset = UNSET,
    current_forecasts_always_visible: FiltersactionsCurrentForecastsAlwaysVisible | Unset = UNSET,
    document_format: FiltersactionsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get the actions for a set of filters

     Get the actions for a set of filters

    Args:
        filter_id (str | Unset):
        parameter_group_id (str | Unset):
        parameter_ids (list[str] | Unset): The parameter can be repeated
        module_instance_ids (list[str] | Unset): The parameter can be repeated
        location_ids (list[str] | Unset): The parameter can be repeated
        time_zero (str | Unset):
        resampling_methods (FiltersactionsResamplingMethods | Unset):
        resampling_time_step_ids (list[str] | Unset): The parameter can be repeated
        resampling_omit_missing (FiltersactionsResamplingOmitMissing | Unset):
        include_non_resampled (FiltersactionsIncludeNonResampled | Unset):
        use_display_units (FiltersactionsUseDisplayUnits | Unset):
        convert_datum (FiltersactionsConvertDatum | Unset):
        start_forecast_time (datetime.datetime | Unset): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        end_forecast_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        forecast_count (str | Unset):
        full_data_period (FiltersactionsFullDataPeriod | Unset):
        task_run_ids (list[str] | Unset): The parameter can be repeated
        current_forecasts_always_visible (FiltersactionsCurrentForecastsAlwaysVisible | Unset):
        document_format (FiltersactionsDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        filter_id=filter_id,
        parameter_group_id=parameter_group_id,
        parameter_ids=parameter_ids,
        module_instance_ids=module_instance_ids,
        location_ids=location_ids,
        time_zero=time_zero,
        resampling_methods=resampling_methods,
        resampling_time_step_ids=resampling_time_step_ids,
        resampling_omit_missing=resampling_omit_missing,
        include_non_resampled=include_non_resampled,
        use_display_units=use_display_units,
        convert_datum=convert_datum,
        start_forecast_time=start_forecast_time,
        end_forecast_time=end_forecast_time,
        forecast_count=forecast_count,
        full_data_period=full_data_period,
        task_run_ids=task_run_ids,
        current_forecasts_always_visible=current_forecasts_always_visible,
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
    parameter_group_id: str | Unset = UNSET,
    parameter_ids: list[str] | Unset = UNSET,
    module_instance_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    time_zero: str | Unset = UNSET,
    resampling_methods: FiltersactionsResamplingMethods | Unset = UNSET,
    resampling_time_step_ids: list[str] | Unset = UNSET,
    resampling_omit_missing: FiltersactionsResamplingOmitMissing | Unset = UNSET,
    include_non_resampled: FiltersactionsIncludeNonResampled | Unset = UNSET,
    use_display_units: FiltersactionsUseDisplayUnits | Unset = UNSET,
    convert_datum: FiltersactionsConvertDatum | Unset = UNSET,
    start_forecast_time: datetime.datetime | Unset = UNSET,
    end_forecast_time: datetime.datetime | Unset = UNSET,
    forecast_count: str | Unset = UNSET,
    full_data_period: FiltersactionsFullDataPeriod | Unset = UNSET,
    task_run_ids: list[str] | Unset = UNSET,
    current_forecasts_always_visible: FiltersactionsCurrentForecastsAlwaysVisible | Unset = UNSET,
    document_format: FiltersactionsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get the actions for a set of filters

     Get the actions for a set of filters

    Args:
        filter_id (str | Unset):
        parameter_group_id (str | Unset):
        parameter_ids (list[str] | Unset): The parameter can be repeated
        module_instance_ids (list[str] | Unset): The parameter can be repeated
        location_ids (list[str] | Unset): The parameter can be repeated
        time_zero (str | Unset):
        resampling_methods (FiltersactionsResamplingMethods | Unset):
        resampling_time_step_ids (list[str] | Unset): The parameter can be repeated
        resampling_omit_missing (FiltersactionsResamplingOmitMissing | Unset):
        include_non_resampled (FiltersactionsIncludeNonResampled | Unset):
        use_display_units (FiltersactionsUseDisplayUnits | Unset):
        convert_datum (FiltersactionsConvertDatum | Unset):
        start_forecast_time (datetime.datetime | Unset): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        end_forecast_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        forecast_count (str | Unset):
        full_data_period (FiltersactionsFullDataPeriod | Unset):
        task_run_ids (list[str] | Unset): The parameter can be repeated
        current_forecasts_always_visible (FiltersactionsCurrentForecastsAlwaysVisible | Unset):
        document_format (FiltersactionsDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        filter_id=filter_id,
        parameter_group_id=parameter_group_id,
        parameter_ids=parameter_ids,
        module_instance_ids=module_instance_ids,
        location_ids=location_ids,
        time_zero=time_zero,
        resampling_methods=resampling_methods,
        resampling_time_step_ids=resampling_time_step_ids,
        resampling_omit_missing=resampling_omit_missing,
        include_non_resampled=include_non_resampled,
        use_display_units=use_display_units,
        convert_datum=convert_datum,
        start_forecast_time=start_forecast_time,
        end_forecast_time=end_forecast_time,
        forecast_count=forecast_count,
        full_data_period=full_data_period,
        task_run_ids=task_run_ids,
        current_forecasts_always_visible=current_forecasts_always_visible,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
