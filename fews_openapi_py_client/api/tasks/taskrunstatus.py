from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.taskrunstatus_document_format import TaskrunstatusDocumentFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    task_id: str,
    max_wait_millis: Unset | str = UNSET,
    document_format: Unset | TaskrunstatusDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["taskId"] = task_id

    params["maxWaitMillis"] = max_wait_millis

    json_document_format: Unset | str = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/taskrunstatus",
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
    task_id: str,
    max_wait_millis: Unset | str = UNSET,
    document_format: Unset | TaskrunstatusDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[Any]:
    """Track the status of a workflow using the taskId, typically used to determine if a taskrun is
    completed

     Track the status of a workflow using the taskId, typically used to determine if a taskrun is
    completed.<p>Possible response codes are:<ul><li>I = Invalid<li>P = Pending</li><li>T =
    Terminated<li>R = running</li><li>F = Failed</li><li>C = Completed fully successful</li><li>D =
    Completed partly successful</li><li>A = Approved</li><li>B = Approved partly successful</li><li>null
    = No status available (produces when method call times-out)</li></ul>

    Args:
        task_id (str):
        max_wait_millis (Union[Unset, str]):
        document_format (Union[Unset, TaskrunstatusDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        max_wait_millis=max_wait_millis,
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
    task_id: str,
    max_wait_millis: Unset | str = UNSET,
    document_format: Unset | TaskrunstatusDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[Any]:
    """Track the status of a workflow using the taskId, typically used to determine if a taskrun is
    completed

     Track the status of a workflow using the taskId, typically used to determine if a taskrun is
    completed.<p>Possible response codes are:<ul><li>I = Invalid<li>P = Pending</li><li>T =
    Terminated<li>R = running</li><li>F = Failed</li><li>C = Completed fully successful</li><li>D =
    Completed partly successful</li><li>A = Approved</li><li>B = Approved partly successful</li><li>null
    = No status available (produces when method call times-out)</li></ul>

    Args:
        task_id (str):
        max_wait_millis (Union[Unset, str]):
        document_format (Union[Unset, TaskrunstatusDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        max_wait_millis=max_wait_millis,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
