from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.qualifiers_document_format import QualifiersDocumentFormat
from ...models.qualifiers_show_attributes import QualifiersShowAttributes
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    show_attributes: QualifiersShowAttributes | Unset = UNSET,
    document_format: QualifiersDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_show_attributes: str | Unset = UNSET
    if not isinstance(show_attributes, Unset):
        json_show_attributes = show_attributes.value

    params["showAttributes"] = json_show_attributes

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/qualifiers",
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
    show_attributes: QualifiersShowAttributes | Unset = UNSET,
    document_format: QualifiersDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get all configured qualifiers from the region config and optionally show all its attributes

     Get all configured qualifiers from the region config and optionally show all its attributes.

    Args:
        show_attributes (QualifiersShowAttributes | Unset):
        document_format (QualifiersDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        show_attributes=show_attributes,
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
    show_attributes: QualifiersShowAttributes | Unset = UNSET,
    document_format: QualifiersDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get all configured qualifiers from the region config and optionally show all its attributes

     Get all configured qualifiers from the region config and optionally show all its attributes.

    Args:
        show_attributes (QualifiersShowAttributes | Unset):
        document_format (QualifiersDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        show_attributes=show_attributes,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
