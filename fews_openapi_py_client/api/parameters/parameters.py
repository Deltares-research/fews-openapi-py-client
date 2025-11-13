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
    filter_id: Unset | str = UNSET,
    show_attributes: Unset | ParametersShowAttributes = UNSET,
    document_format: Unset | ParametersDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["filterId"] = filter_id

    json_show_attributes: Unset | str = UNSET
    if not isinstance(show_attributes, Unset):
        json_show_attributes = show_attributes.value

    params["showAttributes"] = json_show_attributes

    json_document_format: Unset | str = UNSET
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
    filter_id: Unset | str = UNSET,
    show_attributes: Unset | ParametersShowAttributes = UNSET,
    document_format: Unset | ParametersDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[Any]:
    """Get parameters that are available for the 'filterId' argument

     Get parameters that are available for the 'filterId' argument. Parameters are also returned if no
    time series are available for a parameter in the filter. If no filterId is passed then all
    parameters configured in the pre-defined filter will be returned.

    Args:
        filter_id (Union[Unset, str]):
        show_attributes (Union[Unset, ParametersShowAttributes]):
        document_format (Union[Unset, ParametersDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        filter_id=filter_id,
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
    filter_id: Unset | str = UNSET,
    show_attributes: Unset | ParametersShowAttributes = UNSET,
    document_format: Unset | ParametersDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[Any]:
    """Get parameters that are available for the 'filterId' argument

     Get parameters that are available for the 'filterId' argument. Parameters are also returned if no
    time series are available for a parameter in the filter. If no filterId is passed then all
    parameters configured in the pre-defined filter will be returned.

    Args:
        filter_id (Union[Unset, str]):
        show_attributes (Union[Unset, ParametersShowAttributes]):
        document_format (Union[Unset, ParametersDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        filter_id=filter_id,
        show_attributes=show_attributes,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
