import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.timeseriesfiltersactions_convert_datum import TimeseriesfiltersactionsConvertDatum
from ...models.timeseriesfiltersactions_current_forecasts_always_visible import (
    TimeseriesfiltersactionsCurrentForecastsAlwaysVisible,
)
from ...models.timeseriesfiltersactions_document_format import TimeseriesfiltersactionsDocumentFormat
from ...models.timeseriesfiltersactions_use_display_units import TimeseriesfiltersactionsUseDisplayUnits
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_id: Unset | str = UNSET,
    parameter_group_id: Unset | str = UNSET,
    parameter_ids: Unset | str = UNSET,
    location_ids: Unset | str = UNSET,
    task_run_ids: Unset | str = UNSET,
    time_zero: Unset | str = UNSET,
    start_time: Unset | datetime.datetime = UNSET,
    end_time: Unset | datetime.datetime = UNSET,
    start_forecast_time: Unset | datetime.datetime = UNSET,
    end_forecast_time: Unset | datetime.datetime = UNSET,
    forecast_count: Unset | str = UNSET,
    current_forecasts_always_visible: Unset | TimeseriesfiltersactionsCurrentForecastsAlwaysVisible = UNSET,
    use_display_units: Unset | TimeseriesfiltersactionsUseDisplayUnits = UNSET,
    convert_datum: Unset | TimeseriesfiltersactionsConvertDatum = UNSET,
    download_as_file: Unset | str = UNSET,
    document_format: Unset | TimeseriesfiltersactionsDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["filterId"] = filter_id

    params["parameterGroupId"] = parameter_group_id

    params["parameterIds"] = parameter_ids

    params["locationIds"] = location_ids

    params["taskRunIds"] = task_run_ids

    params["timeZero"] = time_zero

    json_start_time: Unset | str = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: Unset | str = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    json_start_forecast_time: Unset | str = UNSET
    if not isinstance(start_forecast_time, Unset):
        json_start_forecast_time = start_forecast_time.isoformat()
    params["startForecastTime"] = json_start_forecast_time

    json_end_forecast_time: Unset | str = UNSET
    if not isinstance(end_forecast_time, Unset):
        json_end_forecast_time = end_forecast_time.isoformat()
    params["endForecastTime"] = json_end_forecast_time

    params["forecastCount"] = forecast_count

    json_current_forecasts_always_visible: Unset | str = UNSET
    if not isinstance(current_forecasts_always_visible, Unset):
        json_current_forecasts_always_visible = current_forecasts_always_visible.value

    params["currentForecastsAlwaysVisible"] = json_current_forecasts_always_visible

    json_use_display_units: Unset | str = UNSET
    if not isinstance(use_display_units, Unset):
        json_use_display_units = use_display_units.value

    params["useDisplayUnits"] = json_use_display_units

    json_convert_datum: Unset | str = UNSET
    if not isinstance(convert_datum, Unset):
        json_convert_datum = convert_datum.value

    params["convertDatum"] = json_convert_datum

    params["downloadAsFile"] = download_as_file

    json_document_format: Unset | str = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/timeseries/filters/actions",
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
    filter_id: Unset | str = UNSET,
    parameter_group_id: Unset | str = UNSET,
    parameter_ids: Unset | str = UNSET,
    location_ids: Unset | str = UNSET,
    task_run_ids: Unset | str = UNSET,
    time_zero: Unset | str = UNSET,
    start_time: Unset | datetime.datetime = UNSET,
    end_time: Unset | datetime.datetime = UNSET,
    start_forecast_time: Unset | datetime.datetime = UNSET,
    end_forecast_time: Unset | datetime.datetime = UNSET,
    forecast_count: Unset | str = UNSET,
    current_forecasts_always_visible: Unset | TimeseriesfiltersactionsCurrentForecastsAlwaysVisible = UNSET,
    use_display_units: Unset | TimeseriesfiltersactionsUseDisplayUnits = UNSET,
    convert_datum: Unset | TimeseriesfiltersactionsConvertDatum = UNSET,
    download_as_file: Unset | str = UNSET,
    document_format: Unset | TimeseriesfiltersactionsDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[Any]:
    """Get the timeseries for the actions for a set of filters

     Get the timeseries for the actions for a set of filters

    Args:
        filter_id (Union[Unset, str]):
        parameter_group_id (Union[Unset, str]):
        parameter_ids (Union[Unset, str]):
        location_ids (Union[Unset, str]):
        task_run_ids (Union[Unset, str]):
        time_zero (Union[Unset, str]):
        start_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        start_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        forecast_count (Union[Unset, str]):
        current_forecasts_always_visible (Union[Unset,
            TimeseriesfiltersactionsCurrentForecastsAlwaysVisible]):
        use_display_units (Union[Unset, TimeseriesfiltersactionsUseDisplayUnits]):
        convert_datum (Union[Unset, TimeseriesfiltersactionsConvertDatum]):
        download_as_file (Union[Unset, str]):
        document_format (Union[Unset, TimeseriesfiltersactionsDocumentFormat]):
        document_version (Union[Unset, str]):

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
        location_ids=location_ids,
        task_run_ids=task_run_ids,
        time_zero=time_zero,
        start_time=start_time,
        end_time=end_time,
        start_forecast_time=start_forecast_time,
        end_forecast_time=end_forecast_time,
        forecast_count=forecast_count,
        current_forecasts_always_visible=current_forecasts_always_visible,
        use_display_units=use_display_units,
        convert_datum=convert_datum,
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
    filter_id: Unset | str = UNSET,
    parameter_group_id: Unset | str = UNSET,
    parameter_ids: Unset | str = UNSET,
    location_ids: Unset | str = UNSET,
    task_run_ids: Unset | str = UNSET,
    time_zero: Unset | str = UNSET,
    start_time: Unset | datetime.datetime = UNSET,
    end_time: Unset | datetime.datetime = UNSET,
    start_forecast_time: Unset | datetime.datetime = UNSET,
    end_forecast_time: Unset | datetime.datetime = UNSET,
    forecast_count: Unset | str = UNSET,
    current_forecasts_always_visible: Unset | TimeseriesfiltersactionsCurrentForecastsAlwaysVisible = UNSET,
    use_display_units: Unset | TimeseriesfiltersactionsUseDisplayUnits = UNSET,
    convert_datum: Unset | TimeseriesfiltersactionsConvertDatum = UNSET,
    download_as_file: Unset | str = UNSET,
    document_format: Unset | TimeseriesfiltersactionsDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[Any]:
    """Get the timeseries for the actions for a set of filters

     Get the timeseries for the actions for a set of filters

    Args:
        filter_id (Union[Unset, str]):
        parameter_group_id (Union[Unset, str]):
        parameter_ids (Union[Unset, str]):
        location_ids (Union[Unset, str]):
        task_run_ids (Union[Unset, str]):
        time_zero (Union[Unset, str]):
        start_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        start_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        forecast_count (Union[Unset, str]):
        current_forecasts_always_visible (Union[Unset,
            TimeseriesfiltersactionsCurrentForecastsAlwaysVisible]):
        use_display_units (Union[Unset, TimeseriesfiltersactionsUseDisplayUnits]):
        convert_datum (Union[Unset, TimeseriesfiltersactionsConvertDatum]):
        download_as_file (Union[Unset, str]):
        document_format (Union[Unset, TimeseriesfiltersactionsDocumentFormat]):
        document_version (Union[Unset, str]):

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
        location_ids=location_ids,
        task_run_ids=task_run_ids,
        time_zero=time_zero,
        start_time=start_time,
        end_time=end_time,
        start_forecast_time=start_forecast_time,
        end_forecast_time=end_forecast_time,
        forecast_count=forecast_count,
        current_forecasts_always_visible=current_forecasts_always_visible,
        use_display_units=use_display_units,
        convert_datum=convert_datum,
        download_as_file=download_as_file,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
