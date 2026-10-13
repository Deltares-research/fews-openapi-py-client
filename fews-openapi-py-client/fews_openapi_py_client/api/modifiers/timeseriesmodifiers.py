import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.timeseriesmodifiers_active import TimeseriesmodifiersActive
from ...models.timeseriesmodifiers_document_format import TimeseriesmodifiersDocumentFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    modifier_type_id: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    module_instance_ids: list[str] | Unset = UNSET,
    active: TimeseriesmodifiersActive | Unset = UNSET,
    user_defined_modifier_description_key_value_pair: list[str] | Unset = UNSET,
    document_format: TimeseriesmodifiersDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_time: str | Unset = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: str | Unset = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params["modifierTypeId"] = modifier_type_id

    params["userId"] = user_id

    json_location_ids: list[str] | Unset = UNSET
    if not isinstance(location_ids, Unset):
        json_location_ids = location_ids

    params["locationIds"] = json_location_ids

    json_module_instance_ids: list[str] | Unset = UNSET
    if not isinstance(module_instance_ids, Unset):
        json_module_instance_ids = module_instance_ids

    params["moduleInstanceIds"] = json_module_instance_ids

    json_active: str | Unset = UNSET
    if not isinstance(active, Unset):
        json_active = active.value

    params["active"] = json_active

    json_user_defined_modifier_description_key_value_pair: list[str] | Unset = UNSET
    if not isinstance(user_defined_modifier_description_key_value_pair, Unset):
        json_user_defined_modifier_description_key_value_pair = user_defined_modifier_description_key_value_pair

    params["userDefinedModifierDescriptionKeyValuePair"] = json_user_defined_modifier_description_key_value_pair

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/timeseriesmodifiers",
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
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    modifier_type_id: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    module_instance_ids: list[str] | Unset = UNSET,
    active: TimeseriesmodifiersActive | Unset = UNSET,
    user_defined_modifier_description_key_value_pair: list[str] | Unset = UNSET,
    document_format: TimeseriesmodifiersDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get timeseries modifiers filtered by parameters like start time, end time and modifier type

     Get timeseries modifiers filtered by parameters like start time, end time and modifier type.

    Args:
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        modifier_type_id (str | Unset):
        user_id (str | Unset):
        location_ids (list[str] | Unset): The parameter can be repeated
        module_instance_ids (list[str] | Unset): The parameter can be repeated
        active (TimeseriesmodifiersActive | Unset):
        user_defined_modifier_description_key_value_pair (list[str] | Unset): The parameter can be
            repeated
        document_format (TimeseriesmodifiersDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        start_time=start_time,
        end_time=end_time,
        modifier_type_id=modifier_type_id,
        user_id=user_id,
        location_ids=location_ids,
        module_instance_ids=module_instance_ids,
        active=active,
        user_defined_modifier_description_key_value_pair=user_defined_modifier_description_key_value_pair,
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
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    modifier_type_id: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    module_instance_ids: list[str] | Unset = UNSET,
    active: TimeseriesmodifiersActive | Unset = UNSET,
    user_defined_modifier_description_key_value_pair: list[str] | Unset = UNSET,
    document_format: TimeseriesmodifiersDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get timeseries modifiers filtered by parameters like start time, end time and modifier type

     Get timeseries modifiers filtered by parameters like start time, end time and modifier type.

    Args:
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        modifier_type_id (str | Unset):
        user_id (str | Unset):
        location_ids (list[str] | Unset): The parameter can be repeated
        module_instance_ids (list[str] | Unset): The parameter can be repeated
        active (TimeseriesmodifiersActive | Unset):
        user_defined_modifier_description_key_value_pair (list[str] | Unset): The parameter can be
            repeated
        document_format (TimeseriesmodifiersDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        start_time=start_time,
        end_time=end_time,
        modifier_type_id=modifier_type_id,
        user_id=user_id,
        location_ids=location_ids,
        module_instance_ids=module_instance_ids,
        active=active,
        user_defined_modifier_description_key_value_pair=user_defined_modifier_description_key_value_pair,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
