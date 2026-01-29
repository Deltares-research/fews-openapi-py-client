import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    display_group_id: str,
    display_id: str,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    width: str | Unset = UNSET,
    height: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["displayGroupId"] = display_group_id

    params["displayId"] = display_id

    json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params["width"] = width

    params["height"] = height

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/displaygroups/plot",
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
    display_group_id: str,
    display_id: str,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    width: str | Unset = UNSET,
    height: str | Unset = UNSET,
) -> Response[Any]:
    """Get a plot image from a display group using the display group id and the display id of the plot

     Get a plot image from a display group using the display group id and the display id of the plot. The
    displayId is a generated id that cannot be configured. It can be determined by using the
    displaygroups/nodes or topology/nodes endpoint that report all supported nodes and its plots.

    Args:
        display_group_id (str):
        display_id (str):
        start_time (datetime.datetime): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        end_time (datetime.datetime): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        width (str | Unset):
        height (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        display_group_id=display_group_id,
        display_id=display_id,
        start_time=start_time,
        end_time=end_time,
        width=width,
        height=height,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    display_group_id: str,
    display_id: str,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    width: str | Unset = UNSET,
    height: str | Unset = UNSET,
) -> Response[Any]:
    """Get a plot image from a display group using the display group id and the display id of the plot

     Get a plot image from a display group using the display group id and the display id of the plot. The
    displayId is a generated id that cannot be configured. It can be determined by using the
    displaygroups/nodes or topology/nodes endpoint that report all supported nodes and its plots.

    Args:
        display_group_id (str):
        display_id (str):
        start_time (datetime.datetime): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        end_time (datetime.datetime): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        width (str | Unset):
        height (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        display_group_id=display_group_id,
        display_id=display_id,
        start_time=start_time,
        end_time=end_time,
        width=width,
        height=height,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
