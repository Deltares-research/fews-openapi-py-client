from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webocconfigcomponentsettings_document_format import WebocconfigcomponentsettingsDocumentFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    component_settings_id: Union[Unset, str] = UNSET,
    document_format: Union[Unset, WebocconfigcomponentsettingsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["componentSettingsId"] = component_settings_id

    json_document_format: Union[Unset, str] = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/weboc/config/componentsettings",
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
    component_settings_id: Union[Unset, str] = UNSET,
    document_format: Union[Unset, WebocconfigcomponentsettingsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get the Web OC Component settings configuration

     Get the Web OC Component settings configuration

    Args:
        component_settings_id (Union[Unset, str]):  Example: myComponentId.
        document_format (Union[Unset, WebocconfigcomponentsettingsDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        component_settings_id=component_settings_id,
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
    component_settings_id: Union[Unset, str] = UNSET,
    document_format: Union[Unset, WebocconfigcomponentsettingsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get the Web OC Component settings configuration

     Get the Web OC Component settings configuration

    Args:
        component_settings_id (Union[Unset, str]):  Example: myComponentId.
        document_format (Union[Unset, WebocconfigcomponentsettingsDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        component_settings_id=component_settings_id,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
