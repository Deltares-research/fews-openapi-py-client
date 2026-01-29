from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.parameters_document_format import ParametersDocumentFormat
from ...models.parameters_show_attributes import ParametersShowAttributes
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_id: str | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    show_attributes: ParametersShowAttributes | Unset = UNSET,
    document_format: ParametersDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["filterId"] = filter_id

    json_location_ids: list[str] | Unset = UNSET
    if not isinstance(location_ids, Unset):
        json_location_ids = location_ids

    params["locationIds"] = json_location_ids

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
        "url": "/parameters",
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
    filter_id: str | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    show_attributes: ParametersShowAttributes | Unset = UNSET,
    document_format: ParametersDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get parameters that are available for the 'filterId' argument

     Get parameters that are available for the 'filterId' argument. Parameters are also returned if no
    time series are available for a parameter in the filter. If no filterId is passed then all
    parameters configured in the pre-defined filter will be returned.

    Args:
        filter_id (str | Unset):
        location_ids (list[str] | Unset): The parameter can be repeated
        show_attributes (ParametersShowAttributes | Unset):
        document_format (ParametersDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        filter_id=filter_id,
        location_ids=location_ids,
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
    filter_id: str | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    show_attributes: ParametersShowAttributes | Unset = UNSET,
    document_format: ParametersDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get parameters that are available for the 'filterId' argument

     Get parameters that are available for the 'filterId' argument. Parameters are also returned if no
    time series are available for a parameter in the filter. If no filterId is passed then all
    parameters configured in the pre-defined filter will be returned.

    Args:
        filter_id (str | Unset):
        location_ids (list[str] | Unset): The parameter can be repeated
        show_attributes (ParametersShowAttributes | Unset):
        document_format (ParametersDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        filter_id=filter_id,
        location_ids=location_ids,
        show_attributes=show_attributes,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
