import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postarchiveproducts_body import PostarchiveproductsBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostarchiveproductsBody,
    time_zero: Unset | datetime.datetime = UNSET,
    area_id: Unset | str = UNSET,
    source_id: Unset | str = UNSET,
    sub_folder: Unset | str = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_time_zero: Unset | str = UNSET
    if not isinstance(time_zero, Unset):
        json_time_zero = time_zero.isoformat()
    params["timeZero"] = json_time_zero

    params["areaId"] = area_id

    params["sourceId"] = source_id

    params["subFolder"] = sub_folder

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/archive/products",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

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
    *,
    client: AuthenticatedClient | Client,
    body: PostarchiveproductsBody,
    time_zero: Unset | datetime.datetime = UNSET,
    area_id: Unset | str = UNSET,
    source_id: Unset | str = UNSET,
    sub_folder: Unset | str = UNSET,
) -> Response[str]:
    """upload new products to the archive

     upload new products to the archive. The multipart/form-data encoding has to be used. The
    metaData.xml will be automatically generated. It is only possible to upload a single product file
    each time this endpoint is used.

    Args:
        time_zero (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        area_id (Union[Unset, str]):
        source_id (Union[Unset, str]):
        sub_folder (Union[Unset, str]):
        body (PostarchiveproductsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        body=body,
        time_zero=time_zero,
        area_id=area_id,
        source_id=source_id,
        sub_folder=sub_folder,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PostarchiveproductsBody,
    time_zero: Unset | datetime.datetime = UNSET,
    area_id: Unset | str = UNSET,
    source_id: Unset | str = UNSET,
    sub_folder: Unset | str = UNSET,
) -> str | None:
    """upload new products to the archive

     upload new products to the archive. The multipart/form-data encoding has to be used. The
    metaData.xml will be automatically generated. It is only possible to upload a single product file
    each time this endpoint is used.

    Args:
        time_zero (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        area_id (Union[Unset, str]):
        source_id (Union[Unset, str]):
        sub_folder (Union[Unset, str]):
        body (PostarchiveproductsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        client=client,
        body=body,
        time_zero=time_zero,
        area_id=area_id,
        source_id=source_id,
        sub_folder=sub_folder,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostarchiveproductsBody,
    time_zero: Unset | datetime.datetime = UNSET,
    area_id: Unset | str = UNSET,
    source_id: Unset | str = UNSET,
    sub_folder: Unset | str = UNSET,
) -> Response[str]:
    """upload new products to the archive

     upload new products to the archive. The multipart/form-data encoding has to be used. The
    metaData.xml will be automatically generated. It is only possible to upload a single product file
    each time this endpoint is used.

    Args:
        time_zero (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        area_id (Union[Unset, str]):
        source_id (Union[Unset, str]):
        sub_folder (Union[Unset, str]):
        body (PostarchiveproductsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        body=body,
        time_zero=time_zero,
        area_id=area_id,
        source_id=source_id,
        sub_folder=sub_folder,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostarchiveproductsBody,
    time_zero: Unset | datetime.datetime = UNSET,
    area_id: Unset | str = UNSET,
    source_id: Unset | str = UNSET,
    sub_folder: Unset | str = UNSET,
) -> str | None:
    """upload new products to the archive

     upload new products to the archive. The multipart/form-data encoding has to be used. The
    metaData.xml will be automatically generated. It is only possible to upload a single product file
    each time this endpoint is used.

    Args:
        time_zero (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        area_id (Union[Unset, str]):
        source_id (Union[Unset, str]):
        sub_folder (Union[Unset, str]):
        body (PostarchiveproductsBody):

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
            time_zero=time_zero,
            area_id=area_id,
            source_id=source_id,
            sub_folder=sub_folder,
        )
    ).parsed
