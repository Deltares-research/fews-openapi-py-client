from http import HTTPStatus
from typing import Any
from urllib.parse import quote

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
    log_type: LogdisplayslogDisplayIdlogsLogType | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    level: LogdisplayslogDisplayIdlogsLevel | Unset = UNSET,
    source: LogdisplayslogDisplayIdlogsSource | Unset = UNSET,
    event_code: str | Unset = UNSET,
    text: str | Unset = UNSET,
    task_run_id: str | Unset = UNSET,
    max_count: str | Unset = UNSET,
    document_format: LogdisplayslogDisplayIdlogsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_log_type: str | Unset = UNSET
    if not isinstance(log_type, Unset):
        json_log_type = log_type.value

    params["logType"] = json_log_type

    params["startTime"] = start_time

    params["endTime"] = end_time

    json_level: str | Unset = UNSET
    if not isinstance(level, Unset):
        json_level = level.value

    params["level"] = json_level

    json_source: str | Unset = UNSET
    if not isinstance(source, Unset):
        json_source = source.value

    params["source"] = json_source

    params["eventCode"] = event_code

    params["text"] = text

    params["taskRunId"] = task_run_id

    params["maxCount"] = max_count

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/logdisplays/{log_display_id}/logs".format(
            log_display_id=quote(str(log_display_id), safe=""),
        ),
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
    log_display_id: str,
    *,
    client: AuthenticatedClient | Client,
    log_type: LogdisplayslogDisplayIdlogsLogType | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    level: LogdisplayslogDisplayIdlogsLevel | Unset = UNSET,
    source: LogdisplayslogDisplayIdlogsSource | Unset = UNSET,
    event_code: str | Unset = UNSET,
    text: str | Unset = UNSET,
    task_run_id: str | Unset = UNSET,
    max_count: str | Unset = UNSET,
    document_format: LogdisplayslogDisplayIdlogsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get the logs from the configured log display in JSON format

     Get the logs from the configured log display in JSON format.

    Args:
        log_display_id (str):
        log_type (LogdisplayslogDisplayIdlogsLogType | Unset):
        start_time (str | Unset):
        end_time (str | Unset):
        level (LogdisplayslogDisplayIdlogsLevel | Unset):
        source (LogdisplayslogDisplayIdlogsSource | Unset):
        event_code (str | Unset):
        text (str | Unset):
        task_run_id (str | Unset):
        max_count (str | Unset):
        document_format (LogdisplayslogDisplayIdlogsDocumentFormat | Unset):
        document_version (str | Unset):

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
    client: AuthenticatedClient | Client,
    log_type: LogdisplayslogDisplayIdlogsLogType | Unset = UNSET,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    level: LogdisplayslogDisplayIdlogsLevel | Unset = UNSET,
    source: LogdisplayslogDisplayIdlogsSource | Unset = UNSET,
    event_code: str | Unset = UNSET,
    text: str | Unset = UNSET,
    task_run_id: str | Unset = UNSET,
    max_count: str | Unset = UNSET,
    document_format: LogdisplayslogDisplayIdlogsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get the logs from the configured log display in JSON format

     Get the logs from the configured log display in JSON format.

    Args:
        log_display_id (str):
        log_type (LogdisplayslogDisplayIdlogsLogType | Unset):
        start_time (str | Unset):
        end_time (str | Unset):
        level (LogdisplayslogDisplayIdlogsLevel | Unset):
        source (LogdisplayslogDisplayIdlogsSource | Unset):
        event_code (str | Unset):
        text (str | Unset):
        task_run_id (str | Unset):
        max_count (str | Unset):
        document_format (LogdisplayslogDisplayIdlogsDocumentFormat | Unset):
        document_version (str | Unset):

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
