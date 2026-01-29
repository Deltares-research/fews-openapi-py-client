import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.modifiers_document_format import ModifiersDocumentFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_time_modifiers: datetime.datetime | Unset = UNSET,
    end_time_modifiers: datetime.datetime | Unset = UNSET,
    modifier_type: str | Unset = UNSET,
    document_format: ModifiersDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_time_modifiers: str | Unset = UNSET
    if not isinstance(start_time_modifiers, Unset):
        json_start_time_modifiers = start_time_modifiers.isoformat()
    params["startTimeModifiers"] = json_start_time_modifiers

    json_end_time_modifiers: str | Unset = UNSET
    if not isinstance(end_time_modifiers, Unset):
        json_end_time_modifiers = end_time_modifiers.isoformat()
    params["endTimeModifiers"] = json_end_time_modifiers

    params["modifierType"] = modifier_type

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/modifiers",
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
    start_time_modifiers: datetime.datetime | Unset = UNSET,
    end_time_modifiers: datetime.datetime | Unset = UNSET,
    modifier_type: str | Unset = UNSET,
    document_format: ModifiersDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get modifiers filtered by parameters like start time, end time and modifier type

     Get modifiers filtered by parameters like start time, end time and modifier type.

    Args:
        start_time_modifiers (datetime.datetime | Unset): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        end_time_modifiers (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        modifier_type (str | Unset):
        document_format (ModifiersDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        start_time_modifiers=start_time_modifiers,
        end_time_modifiers=end_time_modifiers,
        modifier_type=modifier_type,
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
    start_time_modifiers: datetime.datetime | Unset = UNSET,
    end_time_modifiers: datetime.datetime | Unset = UNSET,
    modifier_type: str | Unset = UNSET,
    document_format: ModifiersDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get modifiers filtered by parameters like start time, end time and modifier type

     Get modifiers filtered by parameters like start time, end time and modifier type.

    Args:
        start_time_modifiers (datetime.datetime | Unset): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        end_time_modifiers (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        modifier_type (str | Unset):
        document_format (ModifiersDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        start_time_modifiers=start_time_modifiers,
        end_time_modifiers=end_time_modifiers,
        modifier_type=modifier_type,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
