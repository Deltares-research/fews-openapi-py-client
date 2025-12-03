from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.posttimeseriesedit_body import PosttimeserieseditBody
from ...models.posttimeseriesedit_convert_datum import PosttimeserieseditConvertDatum
from ...models.posttimeseriesedit_use_display_units import PosttimeserieseditUseDisplayUnits
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PosttimeserieseditBody,
    time_series_id: str,
    location_id: str,
    ensemble_id: Union[Unset, str] = UNSET,
    ensemble_member_id: Union[Unset, str] = UNSET,
    convert_datum: Union[Unset, PosttimeserieseditConvertDatum] = UNSET,
    use_display_units: Union[Unset, PosttimeserieseditUseDisplayUnits] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["timeSeriesId"] = time_series_id

    params["locationId"] = location_id

    params["ensembleId"] = ensemble_id

    params["ensembleMemberId"] = ensemble_member_id

    json_convert_datum: Union[Unset, str] = UNSET
    if not isinstance(convert_datum, Unset):
        json_convert_datum = convert_datum.value

    params["convertDatum"] = json_convert_datum

    json_use_display_units: Union[Unset, str] = UNSET
    if not isinstance(use_display_units, Unset):
        json_use_display_units = use_display_units.value

    params["useDisplayUnits"] = json_use_display_units

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/timeseries/edit",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: PosttimeserieseditBody,
    time_series_id: str,
    location_id: str,
    ensemble_id: Union[Unset, str] = UNSET,
    ensemble_member_id: Union[Unset, str] = UNSET,
    convert_datum: Union[Unset, PosttimeserieseditConvertDatum] = UNSET,
    use_display_units: Union[Unset, PosttimeserieseditUseDisplayUnits] = UNSET,
) -> Response[str]:
    """Update a time series that have been edited in timeseries pi json format

     Update a time series that have been edited in timeseries pi json format.<p>Only one timeseries can
    be updated at a time. The sent timeseries should be in pi json format without header information.
    The header is determine by the timeSeriesIndex in combination with a locationId and optionally a
    ensembleId and ensemlbleMemberId..

    Args:
        time_series_id (str):
        location_id (str):
        ensemble_id (Union[Unset, str]):
        ensemble_member_id (Union[Unset, str]):
        convert_datum (Union[Unset, PosttimeserieseditConvertDatum]):
        use_display_units (Union[Unset, PosttimeserieseditUseDisplayUnits]):
        body (PosttimeserieseditBody):

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
    client: Union[AuthenticatedClient, Client],
    body: PosttimeserieseditBody,
    time_series_id: str,
    location_id: str,
    ensemble_id: Union[Unset, str] = UNSET,
    ensemble_member_id: Union[Unset, str] = UNSET,
    convert_datum: Union[Unset, PosttimeserieseditConvertDatum] = UNSET,
    use_display_units: Union[Unset, PosttimeserieseditUseDisplayUnits] = UNSET,
) -> Optional[str]:
    """Update a time series that have been edited in timeseries pi json format

     Update a time series that have been edited in timeseries pi json format.<p>Only one timeseries can
    be updated at a time. The sent timeseries should be in pi json format without header information.
    The header is determine by the timeSeriesIndex in combination with a locationId and optionally a
    ensembleId and ensemlbleMemberId..

    Args:
        time_series_id (str):
        location_id (str):
        ensemble_id (Union[Unset, str]):
        ensemble_member_id (Union[Unset, str]):
        convert_datum (Union[Unset, PosttimeserieseditConvertDatum]):
        use_display_units (Union[Unset, PosttimeserieseditUseDisplayUnits]):
        body (PosttimeserieseditBody):

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
    client: Union[AuthenticatedClient, Client],
    body: PosttimeserieseditBody,
    time_series_id: str,
    location_id: str,
    ensemble_id: Union[Unset, str] = UNSET,
    ensemble_member_id: Union[Unset, str] = UNSET,
    convert_datum: Union[Unset, PosttimeserieseditConvertDatum] = UNSET,
    use_display_units: Union[Unset, PosttimeserieseditUseDisplayUnits] = UNSET,
) -> Response[str]:
    """Update a time series that have been edited in timeseries pi json format

     Update a time series that have been edited in timeseries pi json format.<p>Only one timeseries can
    be updated at a time. The sent timeseries should be in pi json format without header information.
    The header is determine by the timeSeriesIndex in combination with a locationId and optionally a
    ensembleId and ensemlbleMemberId..

    Args:
        time_series_id (str):
        location_id (str):
        ensemble_id (Union[Unset, str]):
        ensemble_member_id (Union[Unset, str]):
        convert_datum (Union[Unset, PosttimeserieseditConvertDatum]):
        use_display_units (Union[Unset, PosttimeserieseditUseDisplayUnits]):
        body (PosttimeserieseditBody):

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
    client: Union[AuthenticatedClient, Client],
    body: PosttimeserieseditBody,
    time_series_id: str,
    location_id: str,
    ensemble_id: Union[Unset, str] = UNSET,
    ensemble_member_id: Union[Unset, str] = UNSET,
    convert_datum: Union[Unset, PosttimeserieseditConvertDatum] = UNSET,
    use_display_units: Union[Unset, PosttimeserieseditUseDisplayUnits] = UNSET,
) -> Optional[str]:
    """Update a time series that have been edited in timeseries pi json format

     Update a time series that have been edited in timeseries pi json format.<p>Only one timeseries can
    be updated at a time. The sent timeseries should be in pi json format without header information.
    The header is determine by the timeSeriesIndex in combination with a locationId and optionally a
    ensembleId and ensemlbleMemberId..

    Args:
        time_series_id (str):
        location_id (str):
        ensemble_id (Union[Unset, str]):
        ensemble_member_id (Union[Unset, str]):
        convert_datum (Union[Unset, PosttimeserieseditConvertDatum]):
        use_display_units (Union[Unset, PosttimeserieseditUseDisplayUnits]):
        body (PosttimeserieseditBody):

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
