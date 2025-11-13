from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.logdisplayslog_display_idaction_body import LogdisplayslogDisplayIdactionBody
from ...types import Response


def _get_kwargs(
    log_display_id: str,
    *,
    body: LogdisplayslogDisplayIdactionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/logdisplays/{log_display_id}/action",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> str | None:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[str]:
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
    body: LogdisplayslogDisplayIdactionBody,
) -> Response[str]:
    """Write a LogDisplay action

     Write a LogDisplay action.<p>The Log Display ActionId has to be passed in the path url and the Log
    Display Action has to be passed in JSON format in the body of the post request following this
    specification: https://fewsdocs.deltares.nl/webservices/rest-
    api/v1/schemas/pirest/pi_rest_logdisplays_action_post.json

    Args:
        log_display_id (str):
        body (LogdisplayslogDisplayIdactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        log_display_id=log_display_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    log_display_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: LogdisplayslogDisplayIdactionBody,
) -> str | None:
    """Write a LogDisplay action

     Write a LogDisplay action.<p>The Log Display ActionId has to be passed in the path url and the Log
    Display Action has to be passed in JSON format in the body of the post request following this
    specification: https://fewsdocs.deltares.nl/webservices/rest-
    api/v1/schemas/pirest/pi_rest_logdisplays_action_post.json

    Args:
        log_display_id (str):
        body (LogdisplayslogDisplayIdactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        log_display_id=log_display_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    log_display_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: LogdisplayslogDisplayIdactionBody,
) -> Response[str]:
    """Write a LogDisplay action

     Write a LogDisplay action.<p>The Log Display ActionId has to be passed in the path url and the Log
    Display Action has to be passed in JSON format in the body of the post request following this
    specification: https://fewsdocs.deltares.nl/webservices/rest-
    api/v1/schemas/pirest/pi_rest_logdisplays_action_post.json

    Args:
        log_display_id (str):
        body (LogdisplayslogDisplayIdactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        log_display_id=log_display_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    log_display_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: LogdisplayslogDisplayIdactionBody,
) -> str | None:
    """Write a LogDisplay action

     Write a LogDisplay action.<p>The Log Display ActionId has to be passed in the path url and the Log
    Display Action has to be passed in JSON format in the body of the post request following this
    specification: https://fewsdocs.deltares.nl/webservices/rest-
    api/v1/schemas/pirest/pi_rest_logdisplays_action_post.json

    Args:
        log_display_id (str):
        body (LogdisplayslogDisplayIdactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            log_display_id=log_display_id,
            client=client,
            body=body,
        )
    ).parsed
