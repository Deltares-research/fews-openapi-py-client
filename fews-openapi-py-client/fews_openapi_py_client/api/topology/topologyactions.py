import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.topologyactions_convert_datum import TopologyactionsConvertDatum
from ...models.topologyactions_current_forecasts_always_visible import TopologyactionsCurrentForecastsAlwaysVisible
from ...models.topologyactions_document_format import TopologyactionsDocumentFormat
from ...models.topologyactions_use_display_units import TopologyactionsUseDisplayUnits
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    node_id: str,
    task_run_ids: Union[Unset, str] = UNSET,
    time_zero: Union[Unset, str] = UNSET,
    start_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    end_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    forecast_count: Union[Unset, str] = UNSET,
    current_forecasts_always_visible: Union[Unset, TopologyactionsCurrentForecastsAlwaysVisible] = UNSET,
    use_display_units: Union[Unset, TopologyactionsUseDisplayUnits] = UNSET,
    convert_datum: Union[Unset, TopologyactionsConvertDatum] = UNSET,
    document_format: Union[Unset, TopologyactionsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["nodeId"] = node_id

    params["taskRunIds"] = task_run_ids

    params["timeZero"] = time_zero

    json_start_forecast_time: Union[Unset, str] = UNSET
    if not isinstance(start_forecast_time, Unset):
        json_start_forecast_time = start_forecast_time.isoformat()
    params["startForecastTime"] = json_start_forecast_time

    json_end_forecast_time: Union[Unset, str] = UNSET
    if not isinstance(end_forecast_time, Unset):
        json_end_forecast_time = end_forecast_time.isoformat()
    params["endForecastTime"] = json_end_forecast_time

    params["forecastCount"] = forecast_count

    json_current_forecasts_always_visible: Union[Unset, str] = UNSET
    if not isinstance(current_forecasts_always_visible, Unset):
        json_current_forecasts_always_visible = current_forecasts_always_visible.value

    params["currentForecastsAlwaysVisible"] = json_current_forecasts_always_visible

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
        "url": "/topology/actions",
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
    node_id: str,
    task_run_ids: Union[Unset, str] = UNSET,
    time_zero: Union[Unset, str] = UNSET,
    start_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    end_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    forecast_count: Union[Unset, str] = UNSET,
    current_forecasts_always_visible: Union[Unset, TopologyactionsCurrentForecastsAlwaysVisible] = UNSET,
    use_display_units: Union[Unset, TopologyactionsUseDisplayUnits] = UNSET,
    convert_datum: Union[Unset, TopologyactionsConvertDatum] = UNSET,
    document_format: Union[Unset, TopologyactionsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get the display group actions for a certain topology node

     Get the display group actions for a certain topology node

    Args:
        node_id (str):
        task_run_ids (Union[Unset, str]):
        time_zero (Union[Unset, str]):
        start_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        forecast_count (Union[Unset, str]):
        current_forecasts_always_visible (Union[Unset,
            TopologyactionsCurrentForecastsAlwaysVisible]):
        use_display_units (Union[Unset, TopologyactionsUseDisplayUnits]):
        convert_datum (Union[Unset, TopologyactionsConvertDatum]):
        document_format (Union[Unset, TopologyactionsDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        task_run_ids=task_run_ids,
        time_zero=time_zero,
        start_forecast_time=start_forecast_time,
        end_forecast_time=end_forecast_time,
        forecast_count=forecast_count,
        current_forecasts_always_visible=current_forecasts_always_visible,
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
    node_id: str,
    task_run_ids: Union[Unset, str] = UNSET,
    time_zero: Union[Unset, str] = UNSET,
    start_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    end_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    forecast_count: Union[Unset, str] = UNSET,
    current_forecasts_always_visible: Union[Unset, TopologyactionsCurrentForecastsAlwaysVisible] = UNSET,
    use_display_units: Union[Unset, TopologyactionsUseDisplayUnits] = UNSET,
    convert_datum: Union[Unset, TopologyactionsConvertDatum] = UNSET,
    document_format: Union[Unset, TopologyactionsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get the display group actions for a certain topology node

     Get the display group actions for a certain topology node

    Args:
        node_id (str):
        task_run_ids (Union[Unset, str]):
        time_zero (Union[Unset, str]):
        start_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        forecast_count (Union[Unset, str]):
        current_forecasts_always_visible (Union[Unset,
            TopologyactionsCurrentForecastsAlwaysVisible]):
        use_display_units (Union[Unset, TopologyactionsUseDisplayUnits]):
        convert_datum (Union[Unset, TopologyactionsConvertDatum]):
        document_format (Union[Unset, TopologyactionsDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        task_run_ids=task_run_ids,
        time_zero=time_zero,
        start_forecast_time=start_forecast_time,
        end_forecast_time=end_forecast_time,
        forecast_count=forecast_count,
        current_forecasts_always_visible=current_forecasts_always_visible,
        use_display_units=use_display_units,
        convert_datum=convert_datum,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
