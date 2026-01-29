from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ratingcurvesstagetodischarge_body import RatingcurvesstagetodischargeBody
from ...models.ratingcurvesstagetodischarge_document_format import RatingcurvesstagetodischargeDocumentFormat
from ...models.ratingcurvesstagetodischarge_use_display_units import RatingcurvesstagetodischargeUseDisplayUnits
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RatingcurvesstagetodischargeBody | Unset = UNSET,
    location_id: str,
    use_display_units: RatingcurvesstagetodischargeUseDisplayUnits | Unset = UNSET,
    document_format: RatingcurvesstagetodischargeDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["locationId"] = location_id

    json_use_display_units: str | Unset = UNSET
    if not isinstance(use_display_units, Unset):
        json_use_display_units = use_display_units.value

    params["useDisplayUnits"] = json_use_display_units

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ratingcurves/stagetodischarge",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
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
    body: RatingcurvesstagetodischargeBody | Unset = UNSET,
    location_id: str,
    use_display_units: RatingcurvesstagetodischargeUseDisplayUnits | Unset = UNSET,
    document_format: RatingcurvesstagetodischargeDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Converts stage values to discharge values using a rating curve at a specific location

     Converts stage values to discharge values using a rating curve at a specific location. The
    stageValues should be passed in the body of the POST request as a key value pair where the key is
    dischargeValue and the value is URL Encoded JSON that conforms to the
    pi_rest_ratingcurves_stage.json schema: https://fewsdocs.deltares.nl/webservices/rest-
    api/v1/schemas/pirest/pi_rest_ratingcurves_stage.json. Since 2022.02. Also available in readonly
    mode.

    Args:
        location_id (str):
        use_display_units (RatingcurvesstagetodischargeUseDisplayUnits | Unset):
        document_format (RatingcurvesstagetodischargeDocumentFormat | Unset):
        document_version (str | Unset):
        body (RatingcurvesstagetodischargeBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        location_id=location_id,
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
    client: AuthenticatedClient | Client,
    body: RatingcurvesstagetodischargeBody | Unset = UNSET,
    location_id: str,
    use_display_units: RatingcurvesstagetodischargeUseDisplayUnits | Unset = UNSET,
    document_format: RatingcurvesstagetodischargeDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Converts stage values to discharge values using a rating curve at a specific location

     Converts stage values to discharge values using a rating curve at a specific location. The
    stageValues should be passed in the body of the POST request as a key value pair where the key is
    dischargeValue and the value is URL Encoded JSON that conforms to the
    pi_rest_ratingcurves_stage.json schema: https://fewsdocs.deltares.nl/webservices/rest-
    api/v1/schemas/pirest/pi_rest_ratingcurves_stage.json. Since 2022.02. Also available in readonly
    mode.

    Args:
        location_id (str):
        use_display_units (RatingcurvesstagetodischargeUseDisplayUnits | Unset):
        document_format (RatingcurvesstagetodischargeDocumentFormat | Unset):
        document_version (str | Unset):
        body (RatingcurvesstagetodischargeBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        location_id=location_id,
        use_display_units=use_display_units,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
