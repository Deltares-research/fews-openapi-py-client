from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.filters_document_format import FiltersDocumentFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_id: Unset | str = UNSET,
    document_format: Unset | FiltersDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["filterId"] = filter_id

    json_document_format: Unset | str = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/filters",
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
    filter_id: Unset | str = UNSET,
    document_format: Unset | FiltersDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[Any]:
    """Get filters that are a subfilter of the default filter

     Get filters that are a subfilter of the default filter. An existing subfilter of the default filter
    id can be specified as well.

    Args:
        filter_id (Union[Unset, str]):
        document_format (Union[Unset, FiltersDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        filter_id=filter_id,
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
    filter_id: Unset | str = UNSET,
    document_format: Unset | FiltersDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[Any]:
    """Get filters that are a subfilter of the default filter

     Get filters that are a subfilter of the default filter. An existing subfilter of the default filter
    id can be specified as well.

    Args:
        filter_id (Union[Unset, str]):
        document_format (Union[Unset, FiltersDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        filter_id=filter_id,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
