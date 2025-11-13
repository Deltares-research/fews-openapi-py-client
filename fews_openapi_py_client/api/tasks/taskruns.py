import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.taskruns_document_format import TaskrunsDocumentFormat
from ...models.taskruns_only_current import TaskrunsOnlyCurrent
from ...models.taskruns_only_forecasts import TaskrunsOnlyForecasts
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workflow_id: str,
    topology_node_id: Union[Unset, str] = UNSET,
    forecast_count: Union[Unset, str] = UNSET,
    task_run_ids: Union[Unset, list[str]] = UNSET,
    scenario_id: Union[Unset, str] = UNSET,
    mc_id: Union[Unset, str] = UNSET,
    start_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    end_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    start_dispatch_time: Union[Unset, datetime.datetime] = UNSET,
    end_dispatch_time: Union[Unset, datetime.datetime] = UNSET,
    task_run_status_ids: Union[Unset, list[str]] = UNSET,
    only_forecasts: Union[Unset, TaskrunsOnlyForecasts] = UNSET,
    task_run_count: Union[Unset, str] = UNSET,
    only_current: Union[Unset, TaskrunsOnlyCurrent] = UNSET,
    document_format: Union[Unset, TaskrunsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["workflowId"] = workflow_id

    params["topologyNodeId"] = topology_node_id

    params["forecastCount"] = forecast_count

    json_task_run_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(task_run_ids, Unset):
        json_task_run_ids = task_run_ids

    params["taskRunIds"] = json_task_run_ids

    params["scenarioId"] = scenario_id

    params["mcId"] = mc_id

    json_start_forecast_time: Union[Unset, str] = UNSET
    if not isinstance(start_forecast_time, Unset):
        json_start_forecast_time = start_forecast_time.isoformat()
    params["startForecastTime"] = json_start_forecast_time

    json_end_forecast_time: Union[Unset, str] = UNSET
    if not isinstance(end_forecast_time, Unset):
        json_end_forecast_time = end_forecast_time.isoformat()
    params["endForecastTime"] = json_end_forecast_time

    json_start_dispatch_time: Union[Unset, str] = UNSET
    if not isinstance(start_dispatch_time, Unset):
        json_start_dispatch_time = start_dispatch_time.isoformat()
    params["startDispatchTime"] = json_start_dispatch_time

    json_end_dispatch_time: Union[Unset, str] = UNSET
    if not isinstance(end_dispatch_time, Unset):
        json_end_dispatch_time = end_dispatch_time.isoformat()
    params["endDispatchTime"] = json_end_dispatch_time

    json_task_run_status_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(task_run_status_ids, Unset):
        json_task_run_status_ids = task_run_status_ids

    params["taskRunStatusIds"] = json_task_run_status_ids

    json_only_forecasts: Union[Unset, str] = UNSET
    if not isinstance(only_forecasts, Unset):
        json_only_forecasts = only_forecasts.value

    params["onlyForecasts"] = json_only_forecasts

    params["taskRunCount"] = task_run_count

    json_only_current: Union[Unset, str] = UNSET
    if not isinstance(only_current, Unset):
        json_only_current = only_current.value

    params["onlyCurrent"] = json_only_current

    
    if not isinstance(document_format, str):
        json_document_format = document_format.value
    else:
        json_document_format = document_format

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/taskruns",
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
    workflow_id: str,
    topology_node_id: Union[Unset, str] = UNSET,
    forecast_count: Union[Unset, str] = UNSET,
    task_run_ids: Union[Unset, list[str]] = UNSET,
    scenario_id: Union[Unset, str] = UNSET,
    mc_id: Union[Unset, str] = UNSET,
    start_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    end_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    start_dispatch_time: Union[Unset, datetime.datetime] = UNSET,
    end_dispatch_time: Union[Unset, datetime.datetime] = UNSET,
    task_run_status_ids: Union[Unset, list[str]] = UNSET,
    only_forecasts: Union[Unset, TaskrunsOnlyForecasts] = UNSET,
    task_run_count: Union[Unset, str] = UNSET,
    only_current: Union[Unset, TaskrunsOnlyCurrent] = UNSET,
    document_format: Union[Unset, TaskrunsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get all taskruns for a workflowId filtered by parameters like forecast time or taskrun status

     Get all taskruns for a workflowId filtered by parameters like forecast time or taskrun status.
    Default only taskruns of forecasts are returned.

    Args:
        workflow_id (str):
        topology_node_id (Union[Unset, str]):
        forecast_count (Union[Unset, str]):
        task_run_ids (Union[Unset, list[str]]): The parameter can be repeated
        scenario_id (Union[Unset, str]):
        mc_id (Union[Unset, str]):
        start_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        start_dispatch_time (Union[Unset, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_dispatch_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        task_run_status_ids (Union[Unset, list[str]]): The parameter can be repeated
        only_forecasts (Union[Unset, TaskrunsOnlyForecasts]):
        task_run_count (Union[Unset, str]):
        only_current (Union[Unset, TaskrunsOnlyCurrent]):
        document_format (Union[Unset, TaskrunsDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        topology_node_id=topology_node_id,
        forecast_count=forecast_count,
        task_run_ids=task_run_ids,
        scenario_id=scenario_id,
        mc_id=mc_id,
        start_forecast_time=start_forecast_time,
        end_forecast_time=end_forecast_time,
        start_dispatch_time=start_dispatch_time,
        end_dispatch_time=end_dispatch_time,
        task_run_status_ids=task_run_status_ids,
        only_forecasts=only_forecasts,
        task_run_count=task_run_count,
        only_current=only_current,
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
    workflow_id: str,
    topology_node_id: Union[Unset, str] = UNSET,
    forecast_count: Union[Unset, str] = UNSET,
    task_run_ids: Union[Unset, list[str]] = UNSET,
    scenario_id: Union[Unset, str] = UNSET,
    mc_id: Union[Unset, str] = UNSET,
    start_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    end_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    start_dispatch_time: Union[Unset, datetime.datetime] = UNSET,
    end_dispatch_time: Union[Unset, datetime.datetime] = UNSET,
    task_run_status_ids: Union[Unset, list[str]] = UNSET,
    only_forecasts: Union[Unset, TaskrunsOnlyForecasts] = UNSET,
    task_run_count: Union[Unset, str] = UNSET,
    only_current: Union[Unset, TaskrunsOnlyCurrent] = UNSET,
    document_format: Union[Unset, TaskrunsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get all taskruns for a workflowId filtered by parameters like forecast time or taskrun status

     Get all taskruns for a workflowId filtered by parameters like forecast time or taskrun status.
    Default only taskruns of forecasts are returned.

    Args:
        workflow_id (str):
        topology_node_id (Union[Unset, str]):
        forecast_count (Union[Unset, str]):
        task_run_ids (Union[Unset, list[str]]): The parameter can be repeated
        scenario_id (Union[Unset, str]):
        mc_id (Union[Unset, str]):
        start_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        start_dispatch_time (Union[Unset, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_dispatch_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        task_run_status_ids (Union[Unset, list[str]]): The parameter can be repeated
        only_forecasts (Union[Unset, TaskrunsOnlyForecasts]):
        task_run_count (Union[Unset, str]):
        only_current (Union[Unset, TaskrunsOnlyCurrent]):
        document_format (Union[Unset, TaskrunsDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        topology_node_id=topology_node_id,
        forecast_count=forecast_count,
        task_run_ids=task_run_ids,
        scenario_id=scenario_id,
        mc_id=mc_id,
        start_forecast_time=start_forecast_time,
        end_forecast_time=end_forecast_time,
        start_dispatch_time=start_dispatch_time,
        end_dispatch_time=end_dispatch_time,
        task_run_status_ids=task_run_status_ids,
        only_forecasts=only_forecasts,
        task_run_count=task_run_count,
        only_current=only_current,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
