import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.correlation_document_format import CorrelationDocumentFormat
from ...models.correlation_regression_equation import CorrelationRegressionEquation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    time_series_id_yaxis: Unset | str = UNSET,
    time_series_id_xaxis: Unset | str = UNSET,
    start_time: Unset | datetime.datetime = UNSET,
    end_time: Unset | datetime.datetime = UNSET,
    regression_equation: Unset | CorrelationRegressionEquation = UNSET,
    upper_threshold: Unset | str = UNSET,
    lower_threshold: Unset | str = UNSET,
    document_format: Unset | CorrelationDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["timeSeriesIdYaxis"] = time_series_id_yaxis

    params["timeSeriesIdXaxis"] = time_series_id_xaxis

    json_start_time: Unset | str = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: Unset | str = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    json_regression_equation: Unset | str = UNSET
    if not isinstance(regression_equation, Unset):
        json_regression_equation = regression_equation.value

    params["regressionEquation"] = json_regression_equation

    params["upperThreshold"] = upper_threshold

    params["lowerThreshold"] = lower_threshold

    json_document_format: Unset | str = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/statistics/correlation",
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
    time_series_id_yaxis: Unset | str = UNSET,
    time_series_id_xaxis: Unset | str = UNSET,
    start_time: Unset | datetime.datetime = UNSET,
    end_time: Unset | datetime.datetime = UNSET,
    regression_equation: Unset | CorrelationRegressionEquation = UNSET,
    upper_threshold: Unset | str = UNSET,
    lower_threshold: Unset | str = UNSET,
    document_format: Unset | CorrelationDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[Any]:
    """Get the correlation between two time series

     Get the correlation between two time series

    Args:
        time_series_id_yaxis (Union[Unset, str]):  Example: myTimeSeriesId1.
        time_series_id_xaxis (Union[Unset, str]):  Example: timeSeriesIdXaxis.
        start_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-19T15:00:00Z.
        regression_equation (Union[Unset, CorrelationRegressionEquation]):  Example:
            2020-03-19T15:00:00Z.
        upper_threshold (Union[Unset, str]):  Example: 5.5.
        lower_threshold (Union[Unset, str]):  Example: 5.5.
        document_format (Union[Unset, CorrelationDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        time_series_id_yaxis=time_series_id_yaxis,
        time_series_id_xaxis=time_series_id_xaxis,
        start_time=start_time,
        end_time=end_time,
        regression_equation=regression_equation,
        upper_threshold=upper_threshold,
        lower_threshold=lower_threshold,
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
    time_series_id_yaxis: Unset | str = UNSET,
    time_series_id_xaxis: Unset | str = UNSET,
    start_time: Unset | datetime.datetime = UNSET,
    end_time: Unset | datetime.datetime = UNSET,
    regression_equation: Unset | CorrelationRegressionEquation = UNSET,
    upper_threshold: Unset | str = UNSET,
    lower_threshold: Unset | str = UNSET,
    document_format: Unset | CorrelationDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[Any]:
    """Get the correlation between two time series

     Get the correlation between two time series

    Args:
        time_series_id_yaxis (Union[Unset, str]):  Example: myTimeSeriesId1.
        time_series_id_xaxis (Union[Unset, str]):  Example: timeSeriesIdXaxis.
        start_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-19T15:00:00Z.
        regression_equation (Union[Unset, CorrelationRegressionEquation]):  Example:
            2020-03-19T15:00:00Z.
        upper_threshold (Union[Unset, str]):  Example: 5.5.
        lower_threshold (Union[Unset, str]):  Example: 5.5.
        document_format (Union[Unset, CorrelationDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        time_series_id_yaxis=time_series_id_yaxis,
        time_series_id_xaxis=time_series_id_xaxis,
        start_time=start_time,
        end_time=end_time,
        regression_equation=regression_equation,
        upper_threshold=upper_threshold,
        lower_threshold=lower_threshold,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
