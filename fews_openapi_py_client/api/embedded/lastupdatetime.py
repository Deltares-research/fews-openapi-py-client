from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.lastupdatetime_document_format import LastupdatetimeDocumentFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    document_format: Union[Unset, LastupdatetimeDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_document_format: Union[Unset, str] = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/lastupdatetime",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[str]:
    if response.status_code == 200:
        response_200 = response.text
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
    document_format: Union[Unset, LastupdatetimeDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[str]:
    """Get the last time the timeseries were updated in the Operator Client or a Stand Alone

     Get the last time the timeseries were updated in the Operator Client or a Stand Alone. It returns
    the last time the main time series dialog loaded time series. Time series dialog will only reload
    the time series when displayed time series are changed in the database or the user selected
    something different. The method was implemented for a very specific use case and is not recommended
    to be used anymore. Since 2022.02

    Args:
        document_format (Union[Unset, LastupdatetimeDocumentFormat]):
        document_version (Union[Unset, str]):

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
    client: Union[AuthenticatedClient, Client],
    document_format: Union[Unset, LastupdatetimeDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Optional[str]:
    """Get the last time the timeseries were updated in the Operator Client or a Stand Alone

     Get the last time the timeseries were updated in the Operator Client or a Stand Alone. It returns
    the last time the main time series dialog loaded time series. Time series dialog will only reload
    the time series when displayed time series are changed in the database or the user selected
    something different. The method was implemented for a very specific use case and is not recommended
    to be used anymore. Since 2022.02

    Args:
        document_format (Union[Unset, LastupdatetimeDocumentFormat]):
        document_version (Union[Unset, str]):

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
    client: Union[AuthenticatedClient, Client],
    document_format: Union[Unset, LastupdatetimeDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[str]:
    """Get the last time the timeseries were updated in the Operator Client or a Stand Alone

     Get the last time the timeseries were updated in the Operator Client or a Stand Alone. It returns
    the last time the main time series dialog loaded time series. Time series dialog will only reload
    the time series when displayed time series are changed in the database or the user selected
    something different. The method was implemented for a very specific use case and is not recommended
    to be used anymore. Since 2022.02

    Args:
        document_format (Union[Unset, LastupdatetimeDocumentFormat]):
        document_version (Union[Unset, str]):

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
    client: Union[AuthenticatedClient, Client],
    document_format: Union[Unset, LastupdatetimeDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Optional[str]:
    """Get the last time the timeseries were updated in the Operator Client or a Stand Alone

     Get the last time the timeseries were updated in the Operator Client or a Stand Alone. It returns
    the last time the main time series dialog loaded time series. Time series dialog will only reload
    the time series when displayed time series are changed in the database or the user selected
    something different. The method was implemented for a very specific use case and is not recommended
    to be used anymore. Since 2022.02

    Args:
        document_format (Union[Unset, LastupdatetimeDocumentFormat]):
        document_version (Union[Unset, str]):

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
