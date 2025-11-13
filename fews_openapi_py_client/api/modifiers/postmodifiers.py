from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postmodifiers_body import PostmodifiersBody
from ...models.postmodifiers_commit_modifiers import PostmodifiersCommitModifiers
from ...models.postmodifiers_delete_all_modifiers import PostmodifiersDeleteAllModifiers
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostmodifiersBody,
    commit_modifiers: Unset | PostmodifiersCommitModifiers = UNSET,
    delete_all_modifiers: Unset | PostmodifiersDeleteAllModifiers = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_commit_modifiers: Unset | str = UNSET
    if not isinstance(commit_modifiers, Unset):
        json_commit_modifiers = commit_modifiers.value

    params["commitModifiers"] = json_commit_modifiers

    json_delete_all_modifiers: Unset | str = UNSET
    if not isinstance(delete_all_modifiers, Unset):
        json_delete_all_modifiers = delete_all_modifiers.value

    params["deleteAllModifiers"] = json_delete_all_modifiers

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/modifiers",
        "params": params,
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
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
    body: PostmodifiersBody,
    commit_modifiers: Unset | PostmodifiersCommitModifiers = UNSET,
    delete_all_modifiers: Unset | PostmodifiersDeleteAllModifiers = UNSET,
) -> Response[Any]:
    """Write modifiers to the Delft-FEWS database

     Write modifiers to the Delft-FEWS database. The application/x-www-form-urlencoded encoding has to be
    used. Readonly mode has to be disabled in the FewsPiService.properties to allow this functionality.

    Args:
        commit_modifiers (Union[Unset, PostmodifiersCommitModifiers]):
        delete_all_modifiers (Union[Unset, PostmodifiersDeleteAllModifiers]):
        body (PostmodifiersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        commit_modifiers=commit_modifiers,
        delete_all_modifiers=delete_all_modifiers,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostmodifiersBody,
    commit_modifiers: Unset | PostmodifiersCommitModifiers = UNSET,
    delete_all_modifiers: Unset | PostmodifiersDeleteAllModifiers = UNSET,
) -> Response[Any]:
    """Write modifiers to the Delft-FEWS database

     Write modifiers to the Delft-FEWS database. The application/x-www-form-urlencoded encoding has to be
    used. Readonly mode has to be disabled in the FewsPiService.properties to allow this functionality.

    Args:
        commit_modifiers (Union[Unset, PostmodifiersCommitModifiers]):
        delete_all_modifiers (Union[Unset, PostmodifiersDeleteAllModifiers]):
        body (PostmodifiersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        commit_modifiers=commit_modifiers,
        delete_all_modifiers=delete_all_modifiers,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
