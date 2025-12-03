from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archiveparameters_document_format import ArchiveparametersDocumentFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    location_ids: Union[Unset, list[str]] = UNSET,
    module_instance_ids: Union[Unset, list[str]] = UNSET,
    area_ids: Union[Unset, list[str]] = UNSET,
    source_ids: Union[Unset, list[str]] = UNSET,
    document_format: Union[Unset, ArchiveparametersDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_location_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(location_ids, Unset):
        json_location_ids = location_ids

    params["locationIds"] = json_location_ids

    json_module_instance_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(module_instance_ids, Unset):
        json_module_instance_ids = module_instance_ids

    params["moduleInstanceIds"] = json_module_instance_ids

    json_area_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(area_ids, Unset):
        json_area_ids = area_ids

    params["areaIds"] = json_area_ids

    json_source_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(source_ids, Unset):
        json_source_ids = source_ids

    params["sourceIds"] = json_source_ids

    json_document_format: Union[Unset, str] = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/archive/parameters",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    location_ids: Union[Unset, list[str]] = UNSET,
    module_instance_ids: Union[Unset, list[str]] = UNSET,
    area_ids: Union[Unset, list[str]] = UNSET,
    source_ids: Union[Unset, list[str]] = UNSET,
    document_format: Union[Unset, ArchiveparametersDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get parameters that are available in the archive

     Get parameters that are available in the archive. Optionally the parameters can be filtered by one
    or more location ids or archive attributes. Archive attributes can be added in the following format:
    attribute(key)=value. Attributes are passed by passing the key as an argument to the attribute()
    parameter and the value as parameter value. For example attribute(storageId)=storageA.

    Args:
        location_ids (Union[Unset, list[str]]): The parameter can be repeated
        module_instance_ids (Union[Unset, list[str]]): The parameter can be repeated
        area_ids (Union[Unset, list[str]]): The parameter can be repeated
        source_ids (Union[Unset, list[str]]): The parameter can be repeated
        document_format (Union[Unset, ArchiveparametersDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        location_ids=location_ids,
        module_instance_ids=module_instance_ids,
        area_ids=area_ids,
        source_ids=source_ids,
        document_format=document_format,
        document_version=document_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    location_ids: Union[Unset, list[str]] = UNSET,
    module_instance_ids: Union[Unset, list[str]] = UNSET,
    area_ids: Union[Unset, list[str]] = UNSET,
    source_ids: Union[Unset, list[str]] = UNSET,
    document_format: Union[Unset, ArchiveparametersDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get parameters that are available in the archive

     Get parameters that are available in the archive. Optionally the parameters can be filtered by one
    or more location ids or archive attributes. Archive attributes can be added in the following format:
    attribute(key)=value. Attributes are passed by passing the key as an argument to the attribute()
    parameter and the value as parameter value. For example attribute(storageId)=storageA.

    Args:
        location_ids (Union[Unset, list[str]]): The parameter can be repeated
        module_instance_ids (Union[Unset, list[str]]): The parameter can be repeated
        area_ids (Union[Unset, list[str]]): The parameter can be repeated
        source_ids (Union[Unset, list[str]]): The parameter can be repeated
        document_format (Union[Unset, ArchiveparametersDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        location_ids=location_ids,
        module_instance_ids=module_instance_ids,
        area_ids=area_ids,
        source_ids=source_ids,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
