import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.timeseriesintervalstatistics_document_format import TimeseriesintervalstatisticsDocumentFormat
from ...models.timeseriesintervalstatistics_interval import TimeseriesintervalstatisticsInterval
from ...models.timeseriesintervalstatistics_time_series_type import TimeseriesintervalstatisticsTimeSeriesType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    interval: TimeseriesintervalstatisticsInterval | Unset = UNSET,
    statistics: list[str] | Unset = UNSET,
    filter_id: str | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    parameter_ids: list[str] | Unset = UNSET,
    module_instance_ids: list[str] | Unset = UNSET,
    qualifier_ids: list[str] | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    ensemble_id: str | Unset = UNSET,
    ensemble_member_id: str | Unset = UNSET,
    time_step_id: str | Unset = UNSET,
    export_id_map: str | Unset = UNSET,
    threshold_value: str | Unset = UNSET,
    time_series_type: TimeseriesintervalstatisticsTimeSeriesType | Unset = UNSET,
    document_format: TimeseriesintervalstatisticsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_interval: str | Unset = UNSET
    if not isinstance(interval, Unset):
        json_interval = interval.value

    params["interval"] = json_interval

    json_statistics: list[str] | Unset = UNSET
    if not isinstance(statistics, Unset):
        json_statistics = statistics

    params["statistics"] = json_statistics

    params["filterId"] = filter_id

    json_location_ids: list[str] | Unset = UNSET
    if not isinstance(location_ids, Unset):
        json_location_ids = location_ids

    params["locationIds"] = json_location_ids

    json_parameter_ids: list[str] | Unset = UNSET
    if not isinstance(parameter_ids, Unset):
        json_parameter_ids = parameter_ids

    params["parameterIds"] = json_parameter_ids

    json_module_instance_ids: list[str] | Unset = UNSET
    if not isinstance(module_instance_ids, Unset):
        json_module_instance_ids = module_instance_ids

    params["moduleInstanceIds"] = json_module_instance_ids

    json_qualifier_ids: list[str] | Unset = UNSET
    if not isinstance(qualifier_ids, Unset):
        json_qualifier_ids = qualifier_ids

    params["qualifierIds"] = json_qualifier_ids

    json_start_time: str | Unset = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: str | Unset = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params["ensembleId"] = ensemble_id

    params["ensembleMemberId"] = ensemble_member_id

    params["timeStepId"] = time_step_id

    params["exportIdMap"] = export_id_map

    params["thresholdValue"] = threshold_value

    json_time_series_type: str | Unset = UNSET
    if not isinstance(time_series_type, Unset):
        json_time_series_type = time_series_type.value

    params["timeSeriesType"] = json_time_series_type

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/timeseries/intervalstatistics",
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
    interval: TimeseriesintervalstatisticsInterval | Unset = UNSET,
    statistics: list[str] | Unset = UNSET,
    filter_id: str | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    parameter_ids: list[str] | Unset = UNSET,
    module_instance_ids: list[str] | Unset = UNSET,
    qualifier_ids: list[str] | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    ensemble_id: str | Unset = UNSET,
    ensemble_member_id: str | Unset = UNSET,
    time_step_id: str | Unset = UNSET,
    export_id_map: str | Unset = UNSET,
    threshold_value: str | Unset = UNSET,
    time_series_type: TimeseriesintervalstatisticsTimeSeriesType | Unset = UNSET,
    document_format: TimeseriesintervalstatisticsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get interval statistics

     Get interval statistics<p>Max. of 500 columns of data.

    Args:
        interval (TimeseriesintervalstatisticsInterval | Unset):
        statistics (list[str] | Unset): The parameter can be repeated
        filter_id (str | Unset):
        location_ids (list[str] | Unset): The parameter can be repeated
        parameter_ids (list[str] | Unset): The parameter can be repeated
        module_instance_ids (list[str] | Unset): The parameter can be repeated
        qualifier_ids (list[str] | Unset): The parameter can be repeated
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        ensemble_id (str | Unset):
        ensemble_member_id (str | Unset):
        time_step_id (str | Unset):
        export_id_map (str | Unset):
        threshold_value (str | Unset):
        time_series_type (TimeseriesintervalstatisticsTimeSeriesType | Unset):
        document_format (TimeseriesintervalstatisticsDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        interval=interval,
        statistics=statistics,
        filter_id=filter_id,
        location_ids=location_ids,
        parameter_ids=parameter_ids,
        module_instance_ids=module_instance_ids,
        qualifier_ids=qualifier_ids,
        start_time=start_time,
        end_time=end_time,
        ensemble_id=ensemble_id,
        ensemble_member_id=ensemble_member_id,
        time_step_id=time_step_id,
        export_id_map=export_id_map,
        threshold_value=threshold_value,
        time_series_type=time_series_type,
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
    interval: TimeseriesintervalstatisticsInterval | Unset = UNSET,
    statistics: list[str] | Unset = UNSET,
    filter_id: str | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    parameter_ids: list[str] | Unset = UNSET,
    module_instance_ids: list[str] | Unset = UNSET,
    qualifier_ids: list[str] | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    ensemble_id: str | Unset = UNSET,
    ensemble_member_id: str | Unset = UNSET,
    time_step_id: str | Unset = UNSET,
    export_id_map: str | Unset = UNSET,
    threshold_value: str | Unset = UNSET,
    time_series_type: TimeseriesintervalstatisticsTimeSeriesType | Unset = UNSET,
    document_format: TimeseriesintervalstatisticsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get interval statistics

     Get interval statistics<p>Max. of 500 columns of data.

    Args:
        interval (TimeseriesintervalstatisticsInterval | Unset):
        statistics (list[str] | Unset): The parameter can be repeated
        filter_id (str | Unset):
        location_ids (list[str] | Unset): The parameter can be repeated
        parameter_ids (list[str] | Unset): The parameter can be repeated
        module_instance_ids (list[str] | Unset): The parameter can be repeated
        qualifier_ids (list[str] | Unset): The parameter can be repeated
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        ensemble_id (str | Unset):
        ensemble_member_id (str | Unset):
        time_step_id (str | Unset):
        export_id_map (str | Unset):
        threshold_value (str | Unset):
        time_series_type (TimeseriesintervalstatisticsTimeSeriesType | Unset):
        document_format (TimeseriesintervalstatisticsDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        interval=interval,
        statistics=statistics,
        filter_id=filter_id,
        location_ids=location_ids,
        parameter_ids=parameter_ids,
        module_instance_ids=module_instance_ids,
        qualifier_ids=qualifier_ids,
        start_time=start_time,
        end_time=end_time,
        ensemble_id=ensemble_id,
        ensemble_member_id=ensemble_member_id,
        time_step_id=time_step_id,
        export_id_map=export_id_map,
        threshold_value=threshold_value,
        time_series_type=time_series_type,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
