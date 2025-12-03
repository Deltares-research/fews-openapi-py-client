from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ratingcurves_document_format import RatingcurvesDocumentFormat
from ...models.ratingcurves_only_headers import RatingcurvesOnlyHeaders
from ...models.ratingcurves_use_display_units import RatingcurvesUseDisplayUnits
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    location_ids: Union[Unset, list[str]] = UNSET,
    only_headers: Union[Unset, RatingcurvesOnlyHeaders] = UNSET,
    use_display_units: Union[Unset, RatingcurvesUseDisplayUnits] = UNSET,
    document_format: Union[Unset, RatingcurvesDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_location_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(location_ids, Unset):
        json_location_ids = location_ids

    params["locationIds"] = json_location_ids

    json_only_headers: Union[Unset, str] = UNSET
    if not isinstance(only_headers, Unset):
        json_only_headers = only_headers.value

    params["onlyHeaders"] = json_only_headers

    json_use_display_units: Union[Unset, str] = UNSET
    if not isinstance(use_display_units, Unset):
        json_use_display_units = use_display_units.value

    params["useDisplayUnits"] = json_use_display_units

    json_document_format: Union[Unset, str] = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ratingcurves",
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
    only_headers: Union[Unset, RatingcurvesOnlyHeaders] = UNSET,
    use_display_units: Union[Unset, RatingcurvesUseDisplayUnits] = UNSET,
    document_format: Union[Unset, RatingcurvesDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get all configured rating curves from the region config and optionally filter by locationIds

     Get all configured rating curves from the region config and optionally filter by locationIds. Since
    2022.02

    Args:
        location_ids (Union[Unset, list[str]]): The parameter can be repeated
        only_headers (Union[Unset, RatingcurvesOnlyHeaders]):
        use_display_units (Union[Unset, RatingcurvesUseDisplayUnits]):
        document_format (Union[Unset, RatingcurvesDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        location_ids=location_ids,
        only_headers=only_headers,
        use_display_units=use_display_units,
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
    only_headers: Union[Unset, RatingcurvesOnlyHeaders] = UNSET,
    use_display_units: Union[Unset, RatingcurvesUseDisplayUnits] = UNSET,
    document_format: Union[Unset, RatingcurvesDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get all configured rating curves from the region config and optionally filter by locationIds

     Get all configured rating curves from the region config and optionally filter by locationIds. Since
    2022.02

    Args:
        location_ids (Union[Unset, list[str]]): The parameter can be repeated
        only_headers (Union[Unset, RatingcurvesOnlyHeaders]):
        use_display_units (Union[Unset, RatingcurvesUseDisplayUnits]):
        document_format (Union[Unset, RatingcurvesDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        location_ids=location_ids,
        only_headers=only_headers,
        use_display_units=use_display_units,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
