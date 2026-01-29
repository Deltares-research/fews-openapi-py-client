from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.systemtime_document_format import SystemtimeDocumentFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    document_format: SystemtimeDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/systemtime",
        "params": params,
    }

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
    document_format: SystemtimeDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[str]:
    """Get the system time of the Web Service

     Get the system time of the Web Service. For embedded tomcat the system time that is set in the
    Operator Client or a Stand Alone will be given. For the REST service the clock time is given unless
    a cardinalTimeStep was configured in the WebServices.xml general section. The system time is the
    time that matches the cardinal timestep that is closest to the clock time (always before or at the
    clock time, not after). In  Since 2022.02

    Args:
        document_format (SystemtimeDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        document_format=document_format,
        document_version=document_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    document_format: SystemtimeDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> str | None:
    """Get the system time of the Web Service

     Get the system time of the Web Service. For embedded tomcat the system time that is set in the
    Operator Client or a Stand Alone will be given. For the REST service the clock time is given unless
    a cardinalTimeStep was configured in the WebServices.xml general section. The system time is the
    time that matches the cardinal timestep that is closest to the clock time (always before or at the
    clock time, not after). In  Since 2022.02

    Args:
        document_format (SystemtimeDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        client=client,
        document_format=document_format,
        document_version=document_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    document_format: SystemtimeDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[str]:
    """Get the system time of the Web Service

     Get the system time of the Web Service. For embedded tomcat the system time that is set in the
    Operator Client or a Stand Alone will be given. For the REST service the clock time is given unless
    a cardinalTimeStep was configured in the WebServices.xml general section. The system time is the
    time that matches the cardinal timestep that is closest to the clock time (always before or at the
    clock time, not after). In  Since 2022.02

    Args:
        document_format (SystemtimeDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    document_format: SystemtimeDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> str | None:
    """Get the system time of the Web Service

     Get the system time of the Web Service. For embedded tomcat the system time that is set in the
    Operator Client or a Stand Alone will be given. For the REST service the clock time is given unless
    a cardinalTimeStep was configured in the WebServices.xml general section. The system time is the
    time that matches the cardinal timestep that is closest to the clock time (always before or at the
    clock time, not after). In  Since 2022.02

    Args:
        document_format (SystemtimeDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            client=client,
            document_format=document_format,
            document_version=document_version,
        )
    ).parsed
