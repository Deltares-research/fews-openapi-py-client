from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lastrefreshtime_document_format import LastrefreshtimeDocumentFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    document_format: Unset | LastrefreshtimeDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_document_format: Unset | str = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/lastrefreshtime",
        "params": params,
    }

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
    *,
    client: AuthenticatedClient | Client,
    document_format: Unset | LastrefreshtimeDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[str]:
    """Get the last refresh time of the Web Service

     Get the last refresh time of the Web Service. Can be used to make sure indexes have been updated
    before making any requests. Typical example may be to retrieve a new forecast for which you are sure
    it is already available in the Delft-FEWS database. Before retrieving the new forecast keep
    requesting the last refresh time until you see a change in the last refresh time. This will make
    sure the indexes have been updated and the new forecast can be found with the WebServices. For this
    endpoint to work reliable in a setup with multiple web services and a load balancer, it is required
    that the client that connects to this endpoint is always directed to the same Web Service instance.

    Args:
        document_format (Union[Unset, LastrefreshtimeDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        document_format=document_format,
        document_version=document_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    document_format: Unset | LastrefreshtimeDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> str | None:
    """Get the last refresh time of the Web Service

     Get the last refresh time of the Web Service. Can be used to make sure indexes have been updated
    before making any requests. Typical example may be to retrieve a new forecast for which you are sure
    it is already available in the Delft-FEWS database. Before retrieving the new forecast keep
    requesting the last refresh time until you see a change in the last refresh time. This will make
    sure the indexes have been updated and the new forecast can be found with the WebServices. For this
    endpoint to work reliable in a setup with multiple web services and a load balancer, it is required
    that the client that connects to this endpoint is always directed to the same Web Service instance.

    Args:
        document_format (Union[Unset, LastrefreshtimeDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        client=client,
        document_format=document_format,
        document_version=document_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    document_format: Unset | LastrefreshtimeDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[str]:
    """Get the last refresh time of the Web Service

     Get the last refresh time of the Web Service. Can be used to make sure indexes have been updated
    before making any requests. Typical example may be to retrieve a new forecast for which you are sure
    it is already available in the Delft-FEWS database. Before retrieving the new forecast keep
    requesting the last refresh time until you see a change in the last refresh time. This will make
    sure the indexes have been updated and the new forecast can be found with the WebServices. For this
    endpoint to work reliable in a setup with multiple web services and a load balancer, it is required
    that the client that connects to this endpoint is always directed to the same Web Service instance.

    Args:
        document_format (Union[Unset, LastrefreshtimeDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    document_format: Unset | LastrefreshtimeDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> str | None:
    """Get the last refresh time of the Web Service

     Get the last refresh time of the Web Service. Can be used to make sure indexes have been updated
    before making any requests. Typical example may be to retrieve a new forecast for which you are sure
    it is already available in the Delft-FEWS database. Before retrieving the new forecast keep
    requesting the last refresh time until you see a change in the last refresh time. This will make
    sure the indexes have been updated and the new forecast can be found with the WebServices. For this
    endpoint to work reliable in a setup with multiple web services and a load balancer, it is required
    that the client that connects to this endpoint is always directed to the same Web Service instance.

    Args:
        document_format (Union[Unset, LastrefreshtimeDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            client=client,
            document_format=document_format,
            document_version=document_version,
        )
    ).parsed
