from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.posttimeseriesedit_body import PosttimeserieseditBody
from ...models.posttimeseriesedit_convert_datum import PosttimeserieseditConvertDatum
from ...models.posttimeseriesedit_use_display_units import PosttimeserieseditUseDisplayUnits
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PosttimeserieseditBody | Unset = UNSET,
    time_series_id: str,
    location_id: str,
    ensemble_id: str | Unset = UNSET,
    ensemble_member_id: str | Unset = UNSET,
    convert_datum: PosttimeserieseditConvertDatum | Unset = UNSET,
    use_display_units: PosttimeserieseditUseDisplayUnits | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["timeSeriesId"] = time_series_id

    params["locationId"] = location_id

    params["ensembleId"] = ensemble_id

    params["ensembleMemberId"] = ensemble_member_id

    json_convert_datum: str | Unset = UNSET
    if not isinstance(convert_datum, Unset):
        json_convert_datum = convert_datum.value

    params["convertDatum"] = json_convert_datum

    json_use_display_units: str | Unset = UNSET
    if not isinstance(use_display_units, Unset):
        json_use_display_units = use_display_units.value

    params["useDisplayUnits"] = json_use_display_units

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/timeseries/edit",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: PosttimeserieseditBody | Unset = UNSET,
    time_series_id: str,
    location_id: str,
    ensemble_id: str | Unset = UNSET,
    ensemble_member_id: str | Unset = UNSET,
    convert_datum: PosttimeserieseditConvertDatum | Unset = UNSET,
    use_display_units: PosttimeserieseditUseDisplayUnits | Unset = UNSET,
) -> Response[str]:
    """Update a time series that have been edited in timeseries pi json format

     Update a time series that have been edited in timeseries pi json format.<p>Only one timeseries can
    be updated at a time. The sent timeseries should be in pi json format without header information.
    The header is determine by the timeSeriesIndex in combination with a locationId and optionally a
    ensembleId and ensemlbleMemberId..

    Args:
        time_series_id (str):
        location_id (str):
        ensemble_id (str | Unset):
        ensemble_member_id (str | Unset):
        convert_datum (PosttimeserieseditConvertDatum | Unset):
        use_display_units (PosttimeserieseditUseDisplayUnits | Unset):
        body (PosttimeserieseditBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        body=body,
        time_series_id=time_series_id,
        location_id=location_id,
        ensemble_id=ensemble_id,
        ensemble_member_id=ensemble_member_id,
        convert_datum=convert_datum,
        use_display_units=use_display_units,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PosttimeserieseditBody | Unset = UNSET,
    time_series_id: str,
    location_id: str,
    ensemble_id: str | Unset = UNSET,
    ensemble_member_id: str | Unset = UNSET,
    convert_datum: PosttimeserieseditConvertDatum | Unset = UNSET,
    use_display_units: PosttimeserieseditUseDisplayUnits | Unset = UNSET,
) -> str | None:
    """Update a time series that have been edited in timeseries pi json format

     Update a time series that have been edited in timeseries pi json format.<p>Only one timeseries can
    be updated at a time. The sent timeseries should be in pi json format without header information.
    The header is determine by the timeSeriesIndex in combination with a locationId and optionally a
    ensembleId and ensemlbleMemberId..

    Args:
        time_series_id (str):
        location_id (str):
        ensemble_id (str | Unset):
        ensemble_member_id (str | Unset):
        convert_datum (PosttimeserieseditConvertDatum | Unset):
        use_display_units (PosttimeserieseditUseDisplayUnits | Unset):
        body (PosttimeserieseditBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        client=client,
        body=body,
        time_series_id=time_series_id,
        location_id=location_id,
        ensemble_id=ensemble_id,
        ensemble_member_id=ensemble_member_id,
        convert_datum=convert_datum,
        use_display_units=use_display_units,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PosttimeserieseditBody | Unset = UNSET,
    time_series_id: str,
    location_id: str,
    ensemble_id: str | Unset = UNSET,
    ensemble_member_id: str | Unset = UNSET,
    convert_datum: PosttimeserieseditConvertDatum | Unset = UNSET,
    use_display_units: PosttimeserieseditUseDisplayUnits | Unset = UNSET,
) -> Response[str]:
    """Update a time series that have been edited in timeseries pi json format

     Update a time series that have been edited in timeseries pi json format.<p>Only one timeseries can
    be updated at a time. The sent timeseries should be in pi json format without header information.
    The header is determine by the timeSeriesIndex in combination with a locationId and optionally a
    ensembleId and ensemlbleMemberId..

    Args:
        time_series_id (str):
        location_id (str):
        ensemble_id (str | Unset):
        ensemble_member_id (str | Unset):
        convert_datum (PosttimeserieseditConvertDatum | Unset):
        use_display_units (PosttimeserieseditUseDisplayUnits | Unset):
        body (PosttimeserieseditBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        body=body,
        time_series_id=time_series_id,
        location_id=location_id,
        ensemble_id=ensemble_id,
        ensemble_member_id=ensemble_member_id,
        convert_datum=convert_datum,
        use_display_units=use_display_units,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PosttimeserieseditBody | Unset = UNSET,
    time_series_id: str,
    location_id: str,
    ensemble_id: str | Unset = UNSET,
    ensemble_member_id: str | Unset = UNSET,
    convert_datum: PosttimeserieseditConvertDatum | Unset = UNSET,
    use_display_units: PosttimeserieseditUseDisplayUnits | Unset = UNSET,
) -> str | None:
    """Update a time series that have been edited in timeseries pi json format

     Update a time series that have been edited in timeseries pi json format.<p>Only one timeseries can
    be updated at a time. The sent timeseries should be in pi json format without header information.
    The header is determine by the timeSeriesIndex in combination with a locationId and optionally a
    ensembleId and ensemlbleMemberId..

    Args:
        time_series_id (str):
        location_id (str):
        ensemble_id (str | Unset):
        ensemble_member_id (str | Unset):
        convert_datum (PosttimeserieseditConvertDatum | Unset):
        use_display_units (PosttimeserieseditUseDisplayUnits | Unset):
        body (PosttimeserieseditBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            time_series_id=time_series_id,
            location_id=location_id,
            ensemble_id=ensemble_id,
            ensemble_member_id=ensemble_member_id,
            convert_datum=convert_datum,
            use_display_units=use_display_units,
        )
    ).parsed
