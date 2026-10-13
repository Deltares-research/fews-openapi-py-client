from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archiveproductsstatus_document_format import ArchiveproductsstatusDocumentFormat
from ...models.archiveproductsstatus_product_status import ArchiveproductsstatusProductStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    relative_path: str | Unset = UNSET,
    document_format: ArchiveproductsstatusDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["relativePath"] = relative_path

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/archive/products/status/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ArchiveproductsstatusProductStatus | None:
    if response.status_code == 200:
        response_200 = ArchiveproductsstatusProductStatus.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ArchiveproductsstatusProductStatus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    relative_path: str | Unset = UNSET,
    document_format: ArchiveproductsstatusDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[ArchiveproductsstatusProductStatus]:
    """Return the status of a specific product in the archive

     Return the status of a specific product in the archive. The relative path in the archive will be
    used as the id.

    Args:
        relative_path (str | Unset):  Example: products-rws/2022/05/rivieren/10/product/weerbeeld_
            maas/2022_05_10_T_09_00_00/KNMI_20220510085242/weerbeeld_maas.txt.
        document_format (ArchiveproductsstatusDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveproductsstatusProductStatus]
    """

    kwargs = _get_kwargs(
        relative_path=relative_path,
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
    relative_path: str | Unset = UNSET,
    document_format: ArchiveproductsstatusDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> ArchiveproductsstatusProductStatus | None:
    """Return the status of a specific product in the archive

     Return the status of a specific product in the archive. The relative path in the archive will be
    used as the id.

    Args:
        relative_path (str | Unset):  Example: products-rws/2022/05/rivieren/10/product/weerbeeld_
            maas/2022_05_10_T_09_00_00/KNMI_20220510085242/weerbeeld_maas.txt.
        document_format (ArchiveproductsstatusDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveproductsstatusProductStatus
    """

    return sync_detailed(
        client=client,
        relative_path=relative_path,
        document_format=document_format,
        document_version=document_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    relative_path: str | Unset = UNSET,
    document_format: ArchiveproductsstatusDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[ArchiveproductsstatusProductStatus]:
    """Return the status of a specific product in the archive

     Return the status of a specific product in the archive. The relative path in the archive will be
    used as the id.

    Args:
        relative_path (str | Unset):  Example: products-rws/2022/05/rivieren/10/product/weerbeeld_
            maas/2022_05_10_T_09_00_00/KNMI_20220510085242/weerbeeld_maas.txt.
        document_format (ArchiveproductsstatusDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveproductsstatusProductStatus]
    """

    kwargs = _get_kwargs(
        relative_path=relative_path,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    relative_path: str | Unset = UNSET,
    document_format: ArchiveproductsstatusDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> ArchiveproductsstatusProductStatus | None:
    """Return the status of a specific product in the archive

     Return the status of a specific product in the archive. The relative path in the archive will be
    used as the id.

    Args:
        relative_path (str | Unset):  Example: products-rws/2022/05/rivieren/10/product/weerbeeld_
            maas/2022_05_10_T_09_00_00/KNMI_20220510085242/weerbeeld_maas.txt.
        document_format (ArchiveproductsstatusDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveproductsstatusProductStatus
    """

    return (
        await asyncio_detailed(
            client=client,
            relative_path=relative_path,
            document_format=document_format,
            document_version=document_version,
        )
    ).parsed
