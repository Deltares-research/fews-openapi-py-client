from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    module_instance_id: Union[Unset, str] = UNSET,
    task_run_id: Union[Unset, str] = UNSET,
    report_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["moduleInstanceId"] = module_instance_id

    params["taskRunId"] = task_run_id

    params["reportId"] = report_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/report",
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
    module_instance_id: Union[Unset, str] = UNSET,
    task_run_id: Union[Unset, str] = UNSET,
    report_id: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get a report file

     Get a report file.

    Args:
        module_instance_id (Union[Unset, str]):
        task_run_id (Union[Unset, str]):
        report_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        module_instance_id=module_instance_id,
        task_run_id=task_run_id,
        report_id=report_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    module_instance_id: Union[Unset, str] = UNSET,
    task_run_id: Union[Unset, str] = UNSET,
    report_id: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get a report file

     Get a report file.

    Args:
        module_instance_id (Union[Unset, str]):
        task_run_id (Union[Unset, str]):
        report_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        module_instance_id=module_instance_id,
        task_run_id=task_run_id,
        report_id=report_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
