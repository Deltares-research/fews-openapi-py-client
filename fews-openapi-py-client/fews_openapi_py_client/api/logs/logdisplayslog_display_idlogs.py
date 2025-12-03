from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.logdisplayslog_display_idlogs_document_format import LogdisplayslogDisplayIdlogsDocumentFormat
from ...models.logdisplayslog_display_idlogs_level import LogdisplayslogDisplayIdlogsLevel
from ...models.logdisplayslog_display_idlogs_log_type import LogdisplayslogDisplayIdlogsLogType
from ...models.logdisplayslog_display_idlogs_source import LogdisplayslogDisplayIdlogsSource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    log_display_id: str,
    *,
    log_type: Union[Unset, LogdisplayslogDisplayIdlogsLogType] = UNSET,
    start_time: Union[Unset, str] = UNSET,
    end_time: Union[Unset, str] = UNSET,
    level: Union[Unset, LogdisplayslogDisplayIdlogsLevel] = UNSET,
    source: Union[Unset, LogdisplayslogDisplayIdlogsSource] = UNSET,
    event_code: Union[Unset, str] = UNSET,
    text: Union[Unset, str] = UNSET,
    task_run_id: Union[Unset, str] = UNSET,
    max_count: Union[Unset, str] = UNSET,
    document_format: Union[Unset, LogdisplayslogDisplayIdlogsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_log_type: Union[Unset, str] = UNSET
    if not isinstance(log_type, Unset):
        json_log_type = log_type.value

    params["logType"] = json_log_type

    params["startTime"] = start_time

    params["endTime"] = end_time

    json_level: Union[Unset, str] = UNSET
    if not isinstance(level, Unset):
        json_level = level.value

    params["level"] = json_level

    json_source: Union[Unset, str] = UNSET
    if not isinstance(source, Unset):
        json_source = source.value

    params["source"] = json_source

    params["eventCode"] = event_code

    params["text"] = text

    params["taskRunId"] = task_run_id

    params["maxCount"] = max_count

    json_document_format: Union[Unset, str] = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/logdisplays/{log_display_id}/logs",
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
    log_display_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    log_type: Union[Unset, LogdisplayslogDisplayIdlogsLogType] = UNSET,
    start_time: Union[Unset, str] = UNSET,
    end_time: Union[Unset, str] = UNSET,
    level: Union[Unset, LogdisplayslogDisplayIdlogsLevel] = UNSET,
    source: Union[Unset, LogdisplayslogDisplayIdlogsSource] = UNSET,
    event_code: Union[Unset, str] = UNSET,
    text: Union[Unset, str] = UNSET,
    task_run_id: Union[Unset, str] = UNSET,
    max_count: Union[Unset, str] = UNSET,
    document_format: Union[Unset, LogdisplayslogDisplayIdlogsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get the logs from the configured log display in JSON format

     Get the logs from the configured log display in JSON format.

    Args:
        log_display_id (str):
        log_type (Union[Unset, LogdisplayslogDisplayIdlogsLogType]):
        start_time (Union[Unset, str]):
        end_time (Union[Unset, str]):
        level (Union[Unset, LogdisplayslogDisplayIdlogsLevel]):
        source (Union[Unset, LogdisplayslogDisplayIdlogsSource]):
        event_code (Union[Unset, str]):
        text (Union[Unset, str]):
        task_run_id (Union[Unset, str]):
        max_count (Union[Unset, str]):
        document_format (Union[Unset, LogdisplayslogDisplayIdlogsDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        log_display_id=log_display_id,
        log_type=log_type,
        start_time=start_time,
        end_time=end_time,
        level=level,
        source=source,
        event_code=event_code,
        text=text,
        task_run_id=task_run_id,
        max_count=max_count,
        document_format=document_format,
        document_version=document_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    log_display_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    log_type: Union[Unset, LogdisplayslogDisplayIdlogsLogType] = UNSET,
    start_time: Union[Unset, str] = UNSET,
    end_time: Union[Unset, str] = UNSET,
    level: Union[Unset, LogdisplayslogDisplayIdlogsLevel] = UNSET,
    source: Union[Unset, LogdisplayslogDisplayIdlogsSource] = UNSET,
    event_code: Union[Unset, str] = UNSET,
    text: Union[Unset, str] = UNSET,
    task_run_id: Union[Unset, str] = UNSET,
    max_count: Union[Unset, str] = UNSET,
    document_format: Union[Unset, LogdisplayslogDisplayIdlogsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get the logs from the configured log display in JSON format

     Get the logs from the configured log display in JSON format.

    Args:
        log_display_id (str):
        log_type (Union[Unset, LogdisplayslogDisplayIdlogsLogType]):
        start_time (Union[Unset, str]):
        end_time (Union[Unset, str]):
        level (Union[Unset, LogdisplayslogDisplayIdlogsLevel]):
        source (Union[Unset, LogdisplayslogDisplayIdlogsSource]):
        event_code (Union[Unset, str]):
        text (Union[Unset, str]):
        task_run_id (Union[Unset, str]):
        max_count (Union[Unset, str]):
        document_format (Union[Unset, LogdisplayslogDisplayIdlogsDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        log_display_id=log_display_id,
        log_type=log_type,
        start_time=start_time,
        end_time=end_time,
        level=level,
        source=source,
        event_code=event_code,
        text=text,
        task_run_id=task_run_id,
        max_count=max_count,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
