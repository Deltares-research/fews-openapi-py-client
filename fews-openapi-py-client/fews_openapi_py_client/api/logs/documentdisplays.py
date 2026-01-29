from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.documentdisplays_document_format import DocumentdisplaysDocumentFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    display_id: str | Unset = UNSET,
    document_format: DocumentdisplaysDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["displayId"] = display_id

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/documentdisplays",
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
    display_id: str | Unset = UNSET,
    document_format: DocumentdisplaysDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get the document displays configuration in JSON format

     Get the document displays configuration in JSON format.

    Args:
        display_id (str | Unset):
        document_format (DocumentdisplaysDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        display_id=display_id,
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
    display_id: str | Unset = UNSET,
    document_format: DocumentdisplaysDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get the document displays configuration in JSON format

     Get the document displays configuration in JSON format.

    Args:
        display_id (str | Unset):
        document_format (DocumentdisplaysDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        display_id=display_id,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
