from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ensemblesmembers_document_format import EnsemblesmembersDocumentFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ensemble_ids: list[str],
    document_format: Union[Unset, EnsemblesmembersDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_ensemble_ids = ensemble_ids

    params["ensembleIds"] = json_ensemble_ids

    json_document_format: Union[Unset, str] = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ensembles/members",
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
    ensemble_ids: list[str],
    document_format: Union[Unset, EnsemblesmembersDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get all ensemble member ids for one or more ensemble Ids

     Get all ensemble member ids for one or more ensemble Ids. The available member ids depend on an up-
    to-date index. This is run once a day on a forecasting shell server.

    Args:
        ensemble_ids (list[str]): The parameter can be repeated
        document_format (Union[Unset, EnsemblesmembersDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ensemble_ids=ensemble_ids,
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
    ensemble_ids: list[str],
    document_format: Union[Unset, EnsemblesmembersDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get all ensemble member ids for one or more ensemble Ids

     Get all ensemble member ids for one or more ensemble Ids. The available member ids depend on an up-
    to-date index. This is run once a day on a forecasting shell server.

    Args:
        ensemble_ids (list[str]): The parameter can be repeated
        document_format (Union[Unset, EnsemblesmembersDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        ensemble_ids=ensemble_ids,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
