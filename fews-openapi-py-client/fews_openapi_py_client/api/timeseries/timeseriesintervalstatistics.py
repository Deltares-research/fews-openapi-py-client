import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.timeseriesintervalstatistics_document_format import TimeseriesintervalstatisticsDocumentFormat
from ...models.timeseriesintervalstatistics_interval import TimeseriesintervalstatisticsInterval
from ...models.timeseriesintervalstatistics_time_series_type import TimeseriesintervalstatisticsTimeSeriesType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    interval: Union[Unset, TimeseriesintervalstatisticsInterval] = UNSET,
    statistics: Union[Unset, list[str]] = UNSET,
    filter_id: Union[Unset, str] = UNSET,
    location_ids: Union[Unset, list[str]] = UNSET,
    parameter_ids: Union[Unset, list[str]] = UNSET,
    module_instance_ids: Union[Unset, list[str]] = UNSET,
    qualifier_ids: Union[Unset, list[str]] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    ensemble_id: Union[Unset, str] = UNSET,
    ensemble_member_id: Union[Unset, str] = UNSET,
    time_step_id: Union[Unset, str] = UNSET,
    export_id_map: Union[Unset, str] = UNSET,
    threshold_value: Union[Unset, str] = UNSET,
    time_series_type: Union[Unset, TimeseriesintervalstatisticsTimeSeriesType] = UNSET,
    document_format: Union[Unset, TimeseriesintervalstatisticsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_interval: Union[Unset, str] = UNSET
    if not isinstance(interval, Unset):
        json_interval = interval.value

    params["interval"] = json_interval

    json_statistics: Union[Unset, list[str]] = UNSET
    if not isinstance(statistics, Unset):
        json_statistics = statistics

    params["statistics"] = json_statistics

    params["filterId"] = filter_id

    json_location_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(location_ids, Unset):
        json_location_ids = location_ids

    params["locationIds"] = json_location_ids

    json_parameter_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(parameter_ids, Unset):
        json_parameter_ids = parameter_ids

    params["parameterIds"] = json_parameter_ids

    json_module_instance_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(module_instance_ids, Unset):
        json_module_instance_ids = module_instance_ids

    params["moduleInstanceIds"] = json_module_instance_ids

    json_qualifier_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(qualifier_ids, Unset):
        json_qualifier_ids = qualifier_ids

    params["qualifierIds"] = json_qualifier_ids

    json_start_time: Union[Unset, str] = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: Union[Unset, str] = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params["ensembleId"] = ensemble_id

    params["ensembleMemberId"] = ensemble_member_id

    params["timeStepId"] = time_step_id

    params["exportIdMap"] = export_id_map

    params["thresholdValue"] = threshold_value

    json_time_series_type: Union[Unset, str] = UNSET
    if not isinstance(time_series_type, Unset):
        json_time_series_type = time_series_type.value

    params["timeSeriesType"] = json_time_series_type

    json_document_format: Union[Unset, str] = UNSET
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
    interval: Union[Unset, TimeseriesintervalstatisticsInterval] = UNSET,
    statistics: Union[Unset, list[str]] = UNSET,
    filter_id: Union[Unset, str] = UNSET,
    location_ids: Union[Unset, list[str]] = UNSET,
    parameter_ids: Union[Unset, list[str]] = UNSET,
    module_instance_ids: Union[Unset, list[str]] = UNSET,
    qualifier_ids: Union[Unset, list[str]] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    ensemble_id: Union[Unset, str] = UNSET,
    ensemble_member_id: Union[Unset, str] = UNSET,
    time_step_id: Union[Unset, str] = UNSET,
    export_id_map: Union[Unset, str] = UNSET,
    threshold_value: Union[Unset, str] = UNSET,
    time_series_type: Union[Unset, TimeseriesintervalstatisticsTimeSeriesType] = UNSET,
    document_format: Union[Unset, TimeseriesintervalstatisticsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get interval statistics

     Get interval statistics<p>Max. of 500 columns of data.

    Args:
        interval (Union[Unset, TimeseriesintervalstatisticsInterval]):
        statistics (Union[Unset, list[str]]): The parameter can be repeated
        filter_id (Union[Unset, str]):
        location_ids (Union[Unset, list[str]]): The parameter can be repeated
        parameter_ids (Union[Unset, list[str]]): The parameter can be repeated
        module_instance_ids (Union[Unset, list[str]]): The parameter can be repeated
        qualifier_ids (Union[Unset, list[str]]): The parameter can be repeated
        start_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        ensemble_id (Union[Unset, str]):
        ensemble_member_id (Union[Unset, str]):
        time_step_id (Union[Unset, str]):
        export_id_map (Union[Unset, str]):
        threshold_value (Union[Unset, str]):
        time_series_type (Union[Unset, TimeseriesintervalstatisticsTimeSeriesType]):
        document_format (Union[Unset, TimeseriesintervalstatisticsDocumentFormat]):
        document_version (Union[Unset, str]):

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
    client: Union[AuthenticatedClient, Client],
    interval: Union[Unset, TimeseriesintervalstatisticsInterval] = UNSET,
    statistics: Union[Unset, list[str]] = UNSET,
    filter_id: Union[Unset, str] = UNSET,
    location_ids: Union[Unset, list[str]] = UNSET,
    parameter_ids: Union[Unset, list[str]] = UNSET,
    module_instance_ids: Union[Unset, list[str]] = UNSET,
    qualifier_ids: Union[Unset, list[str]] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    ensemble_id: Union[Unset, str] = UNSET,
    ensemble_member_id: Union[Unset, str] = UNSET,
    time_step_id: Union[Unset, str] = UNSET,
    export_id_map: Union[Unset, str] = UNSET,
    threshold_value: Union[Unset, str] = UNSET,
    time_series_type: Union[Unset, TimeseriesintervalstatisticsTimeSeriesType] = UNSET,
    document_format: Union[Unset, TimeseriesintervalstatisticsDocumentFormat] = UNSET,
    document_version: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get interval statistics

     Get interval statistics<p>Max. of 500 columns of data.

    Args:
        interval (Union[Unset, TimeseriesintervalstatisticsInterval]):
        statistics (Union[Unset, list[str]]): The parameter can be repeated
        filter_id (Union[Unset, str]):
        location_ids (Union[Unset, list[str]]): The parameter can be repeated
        parameter_ids (Union[Unset, list[str]]): The parameter can be repeated
        module_instance_ids (Union[Unset, list[str]]): The parameter can be repeated
        qualifier_ids (Union[Unset, list[str]]): The parameter can be repeated
        start_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        ensemble_id (Union[Unset, str]):
        ensemble_member_id (Union[Unset, str]):
        time_step_id (Union[Unset, str]):
        export_id_map (Union[Unset, str]):
        threshold_value (Union[Unset, str]):
        time_series_type (Union[Unset, TimeseriesintervalstatisticsTimeSeriesType]):
        document_format (Union[Unset, TimeseriesintervalstatisticsDocumentFormat]):
        document_version (Union[Unset, str]):

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
