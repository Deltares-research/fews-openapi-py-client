from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.posttimeseries_body import PosttimeseriesBody
from ...models.posttimeseries_convert_datum import PosttimeseriesConvertDatum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PosttimeseriesBody,
    filter_id: Union[Unset, str] = UNSET,
    convert_datum: Union[Unset, PosttimeseriesConvertDatum] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["filterId"] = filter_id

    json_convert_datum: Union[Unset, str] = UNSET
    if not isinstance(convert_datum, Unset):
        json_convert_datum = convert_datum.value

    params["convertDatum"] = json_convert_datum

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/timeseries",
        "params": params,
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
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
    body: PosttimeseriesBody,
    filter_id: Union[Unset, str] = UNSET,
    convert_datum: Union[Unset, PosttimeseriesConvertDatum] = UNSET,
) -> Response[Any]:
    r"""Timeseries will be written that are part of the timeseries sets defined by the filters

     Timeseries will be written that are part of the timeseries sets defined by the filters. The
    application/x-www-form-urlencoded encoding has to be used. Readonly mode has to be disable in the
    FewsPiService.properties to allow this functionality.<p>The timeseries you post to the rest service
    should match one of the time series sets in the default filter or one of its sub filters. To make
    sure you only write time series for a specific filter, you can pass a filterId with the POST
    request. Only timeseries that have timeseries sets that are configured in that filter (or one of its
    sub filters) will be accepted. If no filterId is used, all time series will be accepted that are
    configured in the default filter. Writing the time series works similar to importing time series
    using the pi.xml format using the \"PI\" import type. See also: <a target='_new'
    href='https://publicwiki.deltares.nl/x/uIGE'>Delft-Fews Published Interface timeseries Format (PI)
    Import</a>

    The 'convertDatum' argument is to allow timeseries that support a datum to have their values
    converted to a value relative to the location height. If values are already relative to location
    then enter FALSE or omit.

    In case a time series already exists in the database, the time series will be overwritten by the
    ones that are posted. For forecast time series with different forecastDates a new time series will
    be added. The latter can be achieved by providing a forecastDate element in the POST request, e.g.
    <forecastDate date=\"2013-01-01\" time=\"00:00:00\"/>.

    Args:
        filter_id (Union[Unset, str]):
        convert_datum (Union[Unset, PosttimeseriesConvertDatum]):
        body (PosttimeseriesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        filter_id=filter_id,
        convert_datum=convert_datum,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PosttimeseriesBody,
    filter_id: Union[Unset, str] = UNSET,
    convert_datum: Union[Unset, PosttimeseriesConvertDatum] = UNSET,
) -> Response[Any]:
    r"""Timeseries will be written that are part of the timeseries sets defined by the filters

     Timeseries will be written that are part of the timeseries sets defined by the filters. The
    application/x-www-form-urlencoded encoding has to be used. Readonly mode has to be disable in the
    FewsPiService.properties to allow this functionality.<p>The timeseries you post to the rest service
    should match one of the time series sets in the default filter or one of its sub filters. To make
    sure you only write time series for a specific filter, you can pass a filterId with the POST
    request. Only timeseries that have timeseries sets that are configured in that filter (or one of its
    sub filters) will be accepted. If no filterId is used, all time series will be accepted that are
    configured in the default filter. Writing the time series works similar to importing time series
    using the pi.xml format using the \"PI\" import type. See also: <a target='_new'
    href='https://publicwiki.deltares.nl/x/uIGE'>Delft-Fews Published Interface timeseries Format (PI)
    Import</a>

    The 'convertDatum' argument is to allow timeseries that support a datum to have their values
    converted to a value relative to the location height. If values are already relative to location
    then enter FALSE or omit.

    In case a time series already exists in the database, the time series will be overwritten by the
    ones that are posted. For forecast time series with different forecastDates a new time series will
    be added. The latter can be achieved by providing a forecastDate element in the POST request, e.g.
    <forecastDate date=\"2013-01-01\" time=\"00:00:00\"/>.

    Args:
        filter_id (Union[Unset, str]):
        convert_datum (Union[Unset, PosttimeseriesConvertDatum]):
        body (PosttimeseriesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        filter_id=filter_id,
        convert_datum=convert_datum,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
