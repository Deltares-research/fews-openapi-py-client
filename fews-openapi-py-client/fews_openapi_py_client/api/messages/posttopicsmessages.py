from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.posttopicsmessages_json_body import PosttopicsmessagesJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    topic: str,
    *,
    body: PosttopicsmessagesJsonBody | Any | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/topics/{topic}/messages".format(
            topic=quote(str(topic), safe=""),
        ),
    }

    if isinstance(body, PosttopicsmessagesJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, Any):
        if not isinstance(body, Unset):
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
    topic: str,
    *,
    client: AuthenticatedClient | Client,
    body: PosttopicsmessagesJsonBody | Any | Unset = UNSET,
) -> Response[Any]:
    """Send messages to the specified topic name

     Send messages to the specified topic name. Typically used to send email messages. Only allowed with
    authentication and permissions enabled and using mailjet as implementation. The json response needs
    to be checked for any errors.

    Args:
        topic (str):
        body (PosttopicsmessagesJsonBody | Unset):
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        topic=topic,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    topic: str,
    *,
    client: AuthenticatedClient | Client,
    body: PosttopicsmessagesJsonBody | Any | Unset = UNSET,
) -> Response[Any]:
    """Send messages to the specified topic name

     Send messages to the specified topic name. Typically used to send email messages. Only allowed with
    authentication and permissions enabled and using mailjet as implementation. The json response needs
    to be checked for any errors.

    Args:
        topic (str):
        body (PosttopicsmessagesJsonBody | Unset):
        body (Any | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        topic=topic,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
