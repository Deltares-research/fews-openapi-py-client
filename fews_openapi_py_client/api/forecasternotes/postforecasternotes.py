from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postforecasternotes_body import PostforecasternotesBody
from ...types import Response


def _get_kwargs(
    *,
    body: PostforecasternotesBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/forecasternotes",
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
    body: PostforecasternotesBody,
) -> Response[str]:
    """Create or update a forecaster note

     Create or update a forecaster note.<p>The Forecaster Note has to be passed in JSON format in the
    body of the post request following this specification:
    https://fewsdocs.deltares.nl/webservices/rest-
    api/v1/schemas/pirest/pi_rest_forecaster_notes_post.json. To update an existing forecaster note, the
    id and taskRunId has to be passed. If permissions are enabled, it is only allowed to update your own
    forecaster note.

    Args:
        body (PostforecasternotesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostforecasternotesBody,
) -> Optional[str]:
    """Create or update a forecaster note

     Create or update a forecaster note.<p>The Forecaster Note has to be passed in JSON format in the
    body of the post request following this specification:
    https://fewsdocs.deltares.nl/webservices/rest-
    api/v1/schemas/pirest/pi_rest_forecaster_notes_post.json. To update an existing forecaster note, the
    id and taskRunId has to be passed. If permissions are enabled, it is only allowed to update your own
    forecaster note.

    Args:
        body (PostforecasternotesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostforecasternotesBody,
) -> Response[str]:
    """Create or update a forecaster note

     Create or update a forecaster note.<p>The Forecaster Note has to be passed in JSON format in the
    body of the post request following this specification:
    https://fewsdocs.deltares.nl/webservices/rest-
    api/v1/schemas/pirest/pi_rest_forecaster_notes_post.json. To update an existing forecaster note, the
    id and taskRunId has to be passed. If permissions are enabled, it is only allowed to update your own
    forecaster note.

    Args:
        body (PostforecasternotesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostforecasternotesBody,
) -> Optional[str]:
    """Create or update a forecaster note

     Create or update a forecaster note.<p>The Forecaster Note has to be passed in JSON format in the
    body of the post request following this specification:
    https://fewsdocs.deltares.nl/webservices/rest-
    api/v1/schemas/pirest/pi_rest_forecaster_notes_post.json. To update an existing forecaster note, the
    id and taskRunId has to be passed. If permissions are enabled, it is only allowed to update your own
    forecaster note.

    Args:
        body (PostforecasternotesBody):

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
        )
    ).parsed
