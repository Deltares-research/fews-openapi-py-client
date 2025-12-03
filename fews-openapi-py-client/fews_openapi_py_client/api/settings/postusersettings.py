from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postusersettings_body import PostusersettingsBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostusersettingsBody,
    user_id: Union[Unset, str] = UNSET,
    topic_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["userId"] = user_id

    params["topicId"] = topic_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/usersettings",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[str]:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostusersettingsBody,
    user_id: Union[Unset, str] = UNSET,
    topic_id: Union[Unset, str] = UNSET,
) -> Response[str]:
    """Writes the user setting json for the specified user and topic id

     Writes the user setting json for the specified user and topic id

    Args:
        user_id (Union[Unset, str]):
        topic_id (Union[Unset, str]):
        body (PostusersettingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        body=body,
        user_id=user_id,
        topic_id=topic_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostusersettingsBody,
    user_id: Union[Unset, str] = UNSET,
    topic_id: Union[Unset, str] = UNSET,
) -> Optional[str]:
    """Writes the user setting json for the specified user and topic id

     Writes the user setting json for the specified user and topic id

    Args:
        user_id (Union[Unset, str]):
        topic_id (Union[Unset, str]):
        body (PostusersettingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        client=client,
        body=body,
        user_id=user_id,
        topic_id=topic_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostusersettingsBody,
    user_id: Union[Unset, str] = UNSET,
    topic_id: Union[Unset, str] = UNSET,
) -> Response[str]:
    """Writes the user setting json for the specified user and topic id

     Writes the user setting json for the specified user and topic id

    Args:
        user_id (Union[Unset, str]):
        topic_id (Union[Unset, str]):
        body (PostusersettingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        body=body,
        user_id=user_id,
        topic_id=topic_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostusersettingsBody,
    user_id: Union[Unset, str] = UNSET,
    topic_id: Union[Unset, str] = UNSET,
) -> Optional[str]:
    """Writes the user setting json for the specified user and topic id

     Writes the user setting json for the specified user and topic id

    Args:
        user_id (Union[Unset, str]):
        topic_id (Union[Unset, str]):
        body (PostusersettingsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            user_id=user_id,
            topic_id=topic_id,
        )
    ).parsed
