from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archiveattributes_document_format import ArchiveattributesDocumentFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    parameter_ids: Unset | str = UNSET,
    location_ids: Unset | str = UNSET,
    module_instance_ids: Unset | list[str] = UNSET,
    area_ids: Unset | list[str] = UNSET,
    source_ids: Unset | list[str] = UNSET,
    attributes: Unset | list[str] = UNSET,
    document_format: Unset | ArchiveattributesDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["parameterIds"] = parameter_ids

    params["locationIds"] = location_ids

    json_module_instance_ids: Unset | list[str] = UNSET
    if not isinstance(module_instance_ids, Unset):
        json_module_instance_ids = module_instance_ids

    params["moduleInstanceIds"] = json_module_instance_ids

    json_area_ids: Unset | list[str] = UNSET
    if not isinstance(area_ids, Unset):
        json_area_ids = area_ids

    params["areaIds"] = json_area_ids

    json_source_ids: Unset | list[str] = UNSET
    if not isinstance(source_ids, Unset):
        json_source_ids = source_ids

    params["sourceIds"] = json_source_ids

    json_attributes: Unset | list[str] = UNSET
    if not isinstance(attributes, Unset):
        json_attributes = attributes

    params["attributes"] = json_attributes

    json_document_format: Unset | str = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/archive/attributes",
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
    parameter_ids: Unset | str = UNSET,
    location_ids: Unset | str = UNSET,
    module_instance_ids: Unset | list[str] = UNSET,
    area_ids: Unset | list[str] = UNSET,
    source_ids: Unset | list[str] = UNSET,
    attributes: Unset | list[str] = UNSET,
    document_format: Unset | ArchiveattributesDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[Any]:
    """Get attributes with their values that are available in the archive

     Get attributes with their values that are available in the archive. Optionally the attributes can be
    filtered by one or more attribute keys, a parameter ids or a location id.

    Args:
        parameter_ids (Union[Unset, str]):
        location_ids (Union[Unset, str]):
        module_instance_ids (Union[Unset, list[str]]): The parameter can be repeated
        area_ids (Union[Unset, list[str]]): The parameter can be repeated
        source_ids (Union[Unset, list[str]]): The parameter can be repeated
        attributes (Union[Unset, list[str]]): The parameter can be repeated
        document_format (Union[Unset, ArchiveattributesDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        parameter_ids=parameter_ids,
        location_ids=location_ids,
        module_instance_ids=module_instance_ids,
        area_ids=area_ids,
        source_ids=source_ids,
        attributes=attributes,
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
    parameter_ids: Unset | str = UNSET,
    location_ids: Unset | str = UNSET,
    module_instance_ids: Unset | list[str] = UNSET,
    area_ids: Unset | list[str] = UNSET,
    source_ids: Unset | list[str] = UNSET,
    attributes: Unset | list[str] = UNSET,
    document_format: Unset | ArchiveattributesDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[Any]:
    """Get attributes with their values that are available in the archive

     Get attributes with their values that are available in the archive. Optionally the attributes can be
    filtered by one or more attribute keys, a parameter ids or a location id.

    Args:
        parameter_ids (Union[Unset, str]):
        location_ids (Union[Unset, str]):
        module_instance_ids (Union[Unset, list[str]]): The parameter can be repeated
        area_ids (Union[Unset, list[str]]): The parameter can be repeated
        source_ids (Union[Unset, list[str]]): The parameter can be repeated
        attributes (Union[Unset, list[str]]): The parameter can be repeated
        document_format (Union[Unset, ArchiveattributesDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        parameter_ids=parameter_ids,
        location_ids=location_ids,
        module_instance_ids=module_instance_ids,
        area_ids=area_ids,
        source_ids=source_ids,
        attributes=attributes,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
