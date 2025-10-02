from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    relative_path: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["relativePath"] = relative_path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/archive/products/attributes/",
        "params": params,
    }

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
    relative_path: Union[Unset, str] = UNSET,
) -> Response[str]:
    """Add or update attributes to a product metadata

     Add or update attributes to a product metadata.xml. It's only possible to add attributes to one xml
    at a time.

    Args:
        relative_path (Union[Unset, str]):  Example: products-rws/2022/05/rivieren/10/product/weer
            beeld_maas/2022_05_10_T_09_00_00/KNMI_20220510085242/weerbeeld_maas.txt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        relative_path=relative_path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    relative_path: Union[Unset, str] = UNSET,
) -> Optional[str]:
    """Add or update attributes to a product metadata

     Add or update attributes to a product metadata.xml. It's only possible to add attributes to one xml
    at a time.

    Args:
        relative_path (Union[Unset, str]):  Example: products-rws/2022/05/rivieren/10/product/weer
            beeld_maas/2022_05_10_T_09_00_00/KNMI_20220510085242/weerbeeld_maas.txt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        client=client,
        relative_path=relative_path,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    relative_path: Union[Unset, str] = UNSET,
) -> Response[str]:
    """Add or update attributes to a product metadata

     Add or update attributes to a product metadata.xml. It's only possible to add attributes to one xml
    at a time.

    Args:
        relative_path (Union[Unset, str]):  Example: products-rws/2022/05/rivieren/10/product/weer
            beeld_maas/2022_05_10_T_09_00_00/KNMI_20220510085242/weerbeeld_maas.txt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        relative_path=relative_path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    relative_path: Union[Unset, str] = UNSET,
) -> Optional[str]:
    """Add or update attributes to a product metadata

     Add or update attributes to a product metadata.xml. It's only possible to add attributes to one xml
    at a time.

    Args:
        relative_path (Union[Unset, str]):  Example: products-rws/2022/05/rivieren/10/product/weer
            beeld_maas/2022_05_10_T_09_00_00/KNMI_20220510085242/weerbeeld_maas.txt.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            client=client,
            relative_path=relative_path,
        )
    ).parsed
