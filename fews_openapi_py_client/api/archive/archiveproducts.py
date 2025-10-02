import datetime
from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archiveproducts_document_format import ArchiveproductsDocumentFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    source_id: Union[Unset, str] = UNSET,
    area_id: Union[Unset, str] = UNSET,
    product_count: Union[Unset, str] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    start_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    end_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    product_file_name: Union[Unset, datetime.datetime] = UNSET,
    document_format: Union[Unset, ArchiveproductsDocumentFormat] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["sourceId"] = source_id

    params["areaId"] = area_id

    params["productCount"] = product_count

    json_start_time: Union[Unset, str] = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: Union[Unset, str] = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    json_start_forecast_time: Union[Unset, str] = UNSET
    if not isinstance(start_forecast_time, Unset):
        json_start_forecast_time = start_forecast_time.isoformat()
    params["startForecastTime"] = json_start_forecast_time

    json_end_forecast_time: Union[Unset, str] = UNSET
    if not isinstance(end_forecast_time, Unset):
        json_end_forecast_time = end_forecast_time.isoformat()
    params["endForecastTime"] = json_end_forecast_time

    json_product_file_name: Union[Unset, str] = UNSET
    if not isinstance(product_file_name, Unset):
        json_product_file_name = product_file_name.isoformat()
    params["productFileName"] = json_product_file_name

    json_document_format: Union[Unset, str] = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/archive/products",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[str]:
    if response.status_code == 200:
        response_200 = cast(str, response.content)
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
    source_id: Union[Unset, str] = UNSET,
    area_id: Union[Unset, str] = UNSET,
    product_count: Union[Unset, str] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    start_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    end_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    product_file_name: Union[Unset, datetime.datetime] = UNSET,
    document_format: Union[Unset, ArchiveproductsDocumentFormat] = UNSET,
) -> Response[str]:
    """Returns a zip-file with the requested products or a binary file if only one file is requested, that
    are available in the archive filtered by the specified parameters

     Returns a zip-file with the requested products or a binary file if only one file is requested, that
    are available in the archive filtered by the specified parameters.

    Args:
        source_id (Union[Unset, str]):
        area_id (Union[Unset, str]):
        product_count (Union[Unset, str]):
        start_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        start_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        product_file_name (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        document_format (Union[Unset, ArchiveproductsDocumentFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        source_id=source_id,
        area_id=area_id,
        product_count=product_count,
        start_time=start_time,
        end_time=end_time,
        start_forecast_time=start_forecast_time,
        end_forecast_time=end_forecast_time,
        product_file_name=product_file_name,
        document_format=document_format,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    source_id: Union[Unset, str] = UNSET,
    area_id: Union[Unset, str] = UNSET,
    product_count: Union[Unset, str] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    start_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    end_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    product_file_name: Union[Unset, datetime.datetime] = UNSET,
    document_format: Union[Unset, ArchiveproductsDocumentFormat] = UNSET,
) -> Optional[str]:
    """Returns a zip-file with the requested products or a binary file if only one file is requested, that
    are available in the archive filtered by the specified parameters

     Returns a zip-file with the requested products or a binary file if only one file is requested, that
    are available in the archive filtered by the specified parameters.

    Args:
        source_id (Union[Unset, str]):
        area_id (Union[Unset, str]):
        product_count (Union[Unset, str]):
        start_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        start_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        product_file_name (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        document_format (Union[Unset, ArchiveproductsDocumentFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        client=client,
        source_id=source_id,
        area_id=area_id,
        product_count=product_count,
        start_time=start_time,
        end_time=end_time,
        start_forecast_time=start_forecast_time,
        end_forecast_time=end_forecast_time,
        product_file_name=product_file_name,
        document_format=document_format,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    source_id: Union[Unset, str] = UNSET,
    area_id: Union[Unset, str] = UNSET,
    product_count: Union[Unset, str] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    start_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    end_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    product_file_name: Union[Unset, datetime.datetime] = UNSET,
    document_format: Union[Unset, ArchiveproductsDocumentFormat] = UNSET,
) -> Response[str]:
    """Returns a zip-file with the requested products or a binary file if only one file is requested, that
    are available in the archive filtered by the specified parameters

     Returns a zip-file with the requested products or a binary file if only one file is requested, that
    are available in the archive filtered by the specified parameters.

    Args:
        source_id (Union[Unset, str]):
        area_id (Union[Unset, str]):
        product_count (Union[Unset, str]):
        start_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        start_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        product_file_name (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        document_format (Union[Unset, ArchiveproductsDocumentFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        source_id=source_id,
        area_id=area_id,
        product_count=product_count,
        start_time=start_time,
        end_time=end_time,
        start_forecast_time=start_forecast_time,
        end_forecast_time=end_forecast_time,
        product_file_name=product_file_name,
        document_format=document_format,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    source_id: Union[Unset, str] = UNSET,
    area_id: Union[Unset, str] = UNSET,
    product_count: Union[Unset, str] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    start_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    end_forecast_time: Union[Unset, datetime.datetime] = UNSET,
    product_file_name: Union[Unset, datetime.datetime] = UNSET,
    document_format: Union[Unset, ArchiveproductsDocumentFormat] = UNSET,
) -> Optional[str]:
    """Returns a zip-file with the requested products or a binary file if only one file is requested, that
    are available in the archive filtered by the specified parameters

     Returns a zip-file with the requested products or a binary file if only one file is requested, that
    are available in the archive filtered by the specified parameters.

    Args:
        source_id (Union[Unset, str]):
        area_id (Union[Unset, str]):
        product_count (Union[Unset, str]):
        start_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        start_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_forecast_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        product_file_name (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        document_format (Union[Unset, ArchiveproductsDocumentFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            client=client,
            source_id=source_id,
            area_id=area_id,
            product_count=product_count,
            start_time=start_time,
            end_time=end_time,
            start_forecast_time=start_forecast_time,
            end_forecast_time=end_forecast_time,
            product_file_name=product_file_name,
            document_format=document_format,
        )
    ).parsed
