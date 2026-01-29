from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archivelocations_document_format import ArchivelocationsDocumentFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    parameter_ids: list[str] | Unset = UNSET,
    module_instance_ids: list[str] | Unset = UNSET,
    area_ids: list[str] | Unset = UNSET,
    source_ids: list[str] | Unset = UNSET,
    document_format: ArchivelocationsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_parameter_ids: list[str] | Unset = UNSET
    if not isinstance(parameter_ids, Unset):
        json_parameter_ids = parameter_ids

    params["parameterIds"] = json_parameter_ids

    json_module_instance_ids: list[str] | Unset = UNSET
    if not isinstance(module_instance_ids, Unset):
        json_module_instance_ids = module_instance_ids

    params["moduleInstanceIds"] = json_module_instance_ids

    json_area_ids: list[str] | Unset = UNSET
    if not isinstance(area_ids, Unset):
        json_area_ids = area_ids

    params["areaIds"] = json_area_ids

    json_source_ids: list[str] | Unset = UNSET
    if not isinstance(source_ids, Unset):
        json_source_ids = source_ids

    params["sourceIds"] = json_source_ids

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/archive/locations",
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
    parameter_ids: list[str] | Unset = UNSET,
    module_instance_ids: list[str] | Unset = UNSET,
    area_ids: list[str] | Unset = UNSET,
    source_ids: list[str] | Unset = UNSET,
    document_format: ArchivelocationsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get locations that are available in the archive

     Get locations that are available in the archive. Optionally the locations can be filtered by one or
    more parameter ids or archive attributes. Archive attributes can be added in the following format:
    attribute(key)=value. Attributes are passed by passing the key as an argument to the attribute()
    parameter and the value as parameter value. For example attribute(storageId)=storageA.

    Args:
        parameter_ids (list[str] | Unset): The parameter can be repeated
        module_instance_ids (list[str] | Unset): The parameter can be repeated
        area_ids (list[str] | Unset): The parameter can be repeated
        source_ids (list[str] | Unset): The parameter can be repeated
        document_format (ArchivelocationsDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        parameter_ids=parameter_ids,
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
    client: AuthenticatedClient | Client,
    parameter_ids: list[str] | Unset = UNSET,
    module_instance_ids: list[str] | Unset = UNSET,
    area_ids: list[str] | Unset = UNSET,
    source_ids: list[str] | Unset = UNSET,
    document_format: ArchivelocationsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get locations that are available in the archive

     Get locations that are available in the archive. Optionally the locations can be filtered by one or
    more parameter ids or archive attributes. Archive attributes can be added in the following format:
    attribute(key)=value. Attributes are passed by passing the key as an argument to the attribute()
    parameter and the value as parameter value. For example attribute(storageId)=storageA.

    Args:
        parameter_ids (list[str] | Unset): The parameter can be repeated
        module_instance_ids (list[str] | Unset): The parameter can be repeated
        area_ids (list[str] | Unset): The parameter can be repeated
        source_ids (list[str] | Unset): The parameter can be repeated
        document_format (ArchivelocationsDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        parameter_ids=parameter_ids,
        module_instance_ids=module_instance_ids,
        area_ids=area_ids,
        source_ids=source_ids,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
