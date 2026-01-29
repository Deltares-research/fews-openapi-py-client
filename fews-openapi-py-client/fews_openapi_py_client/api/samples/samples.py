import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.samples_document_format import SamplesDocumentFormat
from ...models.samples_filter_time_series_within_sample import SamplesFilterTimeSeriesWithinSample
from ...models.samples_omit_missing import SamplesOmitMissing
from ...models.samples_only_headers import SamplesOnlyHeaders
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_id: str | Unset = UNSET,
    sample_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    parameter_ids: list[str] | Unset = UNSET,
    module_instance_ids: list[str] | Unset = UNSET,
    qualifier_ids: list[str] | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    start_creation_time: datetime.datetime | Unset = UNSET,
    end_creation_time: datetime.datetime | Unset = UNSET,
    omit_missing: SamplesOmitMissing | Unset = UNSET,
    only_headers: SamplesOnlyHeaders | Unset = UNSET,
    filter_time_series_within_sample: SamplesFilterTimeSeriesWithinSample | Unset = UNSET,
    document_format: SamplesDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["filterId"] = filter_id

    json_sample_ids: list[str] | Unset = UNSET
    if not isinstance(sample_ids, Unset):
        json_sample_ids = sample_ids

    params["sampleIds"] = json_sample_ids

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

    json_start_creation_time: str | Unset = UNSET
    if not isinstance(start_creation_time, Unset):
        json_start_creation_time = start_creation_time.isoformat()
    params["startCreationTime"] = json_start_creation_time

    json_end_creation_time: str | Unset = UNSET
    if not isinstance(end_creation_time, Unset):
        json_end_creation_time = end_creation_time.isoformat()
    params["endCreationTime"] = json_end_creation_time

    json_omit_missing: str | Unset = UNSET
    if not isinstance(omit_missing, Unset):
        json_omit_missing = omit_missing.value

    params["omitMissing"] = json_omit_missing

    json_only_headers: str | Unset = UNSET
    if not isinstance(only_headers, Unset):
        json_only_headers = only_headers.value

    params["onlyHeaders"] = json_only_headers

    json_filter_time_series_within_sample: str | Unset = UNSET
    if not isinstance(filter_time_series_within_sample, Unset):
        json_filter_time_series_within_sample = filter_time_series_within_sample.value

    params["filterTimeSeriesWithinSample"] = json_filter_time_series_within_sample

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/samples",
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
    filter_id: str | Unset = UNSET,
    sample_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    parameter_ids: list[str] | Unset = UNSET,
    module_instance_ids: list[str] | Unset = UNSET,
    qualifier_ids: list[str] | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    start_creation_time: datetime.datetime | Unset = UNSET,
    end_creation_time: datetime.datetime | Unset = UNSET,
    omit_missing: SamplesOmitMissing | Unset = UNSET,
    only_headers: SamplesOnlyHeaders | Unset = UNSET,
    filter_time_series_within_sample: SamplesFilterTimeSeriesWithinSample | Unset = UNSET,
    document_format: SamplesDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get samples filtered by parameters like filterId, sampleId, parameterId and creation time of a
    sample

     Get samples filtered by parameters like filterId, sampleId, parameterId and creation time of a
    sample.

    Args:
        filter_id (str | Unset):
        sample_ids (list[str] | Unset): The parameter can be repeated
        location_ids (list[str] | Unset): The parameter can be repeated
        parameter_ids (list[str] | Unset): The parameter can be repeated
        module_instance_ids (list[str] | Unset): The parameter can be repeated
        qualifier_ids (list[str] | Unset): The parameter can be repeated
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        start_creation_time (datetime.datetime | Unset): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        end_creation_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        omit_missing (SamplesOmitMissing | Unset):
        only_headers (SamplesOnlyHeaders | Unset):
        filter_time_series_within_sample (SamplesFilterTimeSeriesWithinSample | Unset):
        document_format (SamplesDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        filter_id=filter_id,
        sample_ids=sample_ids,
        location_ids=location_ids,
        parameter_ids=parameter_ids,
        module_instance_ids=module_instance_ids,
        qualifier_ids=qualifier_ids,
        start_time=start_time,
        end_time=end_time,
        start_creation_time=start_creation_time,
        end_creation_time=end_creation_time,
        omit_missing=omit_missing,
        only_headers=only_headers,
        filter_time_series_within_sample=filter_time_series_within_sample,
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
    filter_id: str | Unset = UNSET,
    sample_ids: list[str] | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    parameter_ids: list[str] | Unset = UNSET,
    module_instance_ids: list[str] | Unset = UNSET,
    qualifier_ids: list[str] | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    start_creation_time: datetime.datetime | Unset = UNSET,
    end_creation_time: datetime.datetime | Unset = UNSET,
    omit_missing: SamplesOmitMissing | Unset = UNSET,
    only_headers: SamplesOnlyHeaders | Unset = UNSET,
    filter_time_series_within_sample: SamplesFilterTimeSeriesWithinSample | Unset = UNSET,
    document_format: SamplesDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get samples filtered by parameters like filterId, sampleId, parameterId and creation time of a
    sample

     Get samples filtered by parameters like filterId, sampleId, parameterId and creation time of a
    sample.

    Args:
        filter_id (str | Unset):
        sample_ids (list[str] | Unset): The parameter can be repeated
        location_ids (list[str] | Unset): The parameter can be repeated
        parameter_ids (list[str] | Unset): The parameter can be repeated
        module_instance_ids (list[str] | Unset): The parameter can be repeated
        qualifier_ids (list[str] | Unset): The parameter can be repeated
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        start_creation_time (datetime.datetime | Unset): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        end_creation_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        omit_missing (SamplesOmitMissing | Unset):
        only_headers (SamplesOnlyHeaders | Unset):
        filter_time_series_within_sample (SamplesFilterTimeSeriesWithinSample | Unset):
        document_format (SamplesDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        filter_id=filter_id,
        sample_ids=sample_ids,
        location_ids=location_ids,
        parameter_ids=parameter_ids,
        module_instance_ids=module_instance_ids,
        qualifier_ids=qualifier_ids,
        start_time=start_time,
        end_time=end_time,
        start_creation_time=start_creation_time,
        end_creation_time=end_creation_time,
        omit_missing=omit_missing,
        only_headers=only_headers,
        filter_time_series_within_sample=filter_time_series_within_sample,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
