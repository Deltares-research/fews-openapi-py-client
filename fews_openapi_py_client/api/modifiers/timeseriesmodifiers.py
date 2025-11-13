import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.timeseriesmodifiers_document_format import TimeseriesmodifiersDocumentFormat
from ...models.timeseriesmodifiers_only_active_modifiers import TimeseriesmodifiersOnlyActiveModifiers
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_time_modifiers: Unset | datetime.datetime = UNSET,
    end_time_modifiers: Unset | datetime.datetime = UNSET,
    modifier_type: Unset | str = UNSET,
    user_id: Unset | str = UNSET,
    location_ids: Unset | list[str] = UNSET,
    module_instance_ids: Unset | list[str] = UNSET,
    only_active_modifiers: Unset | TimeseriesmodifiersOnlyActiveModifiers = UNSET,
    user_defined_modifier_description: Unset | str = UNSET,
    document_format: Unset | TimeseriesmodifiersDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_start_time_modifiers: Unset | str = UNSET
    if not isinstance(start_time_modifiers, Unset):
        json_start_time_modifiers = start_time_modifiers.isoformat()
    params["startTimeModifiers"] = json_start_time_modifiers

    json_end_time_modifiers: Unset | str = UNSET
    if not isinstance(end_time_modifiers, Unset):
        json_end_time_modifiers = end_time_modifiers.isoformat()
    params["endTimeModifiers"] = json_end_time_modifiers

    params["modifierType"] = modifier_type

    params["userId"] = user_id

    json_location_ids: Unset | list[str] = UNSET
    if not isinstance(location_ids, Unset):
        json_location_ids = location_ids

    params["locationIds"] = json_location_ids

    json_module_instance_ids: Unset | list[str] = UNSET
    if not isinstance(module_instance_ids, Unset):
        json_module_instance_ids = module_instance_ids

    params["moduleInstanceIds"] = json_module_instance_ids

    json_only_active_modifiers: Unset | str = UNSET
    if not isinstance(only_active_modifiers, Unset):
        json_only_active_modifiers = only_active_modifiers.value

    params["onlyActiveModifiers"] = json_only_active_modifiers

    params["userDefinedModifierDescription"] = user_defined_modifier_description

    json_document_format: Unset | str = UNSET
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
    start_time_modifiers: Unset | datetime.datetime = UNSET,
    end_time_modifiers: Unset | datetime.datetime = UNSET,
    modifier_type: Unset | str = UNSET,
    user_id: Unset | str = UNSET,
    location_ids: Unset | list[str] = UNSET,
    module_instance_ids: Unset | list[str] = UNSET,
    only_active_modifiers: Unset | TimeseriesmodifiersOnlyActiveModifiers = UNSET,
    user_defined_modifier_description: Unset | str = UNSET,
    document_format: Unset | TimeseriesmodifiersDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[Any]:
    """Get timeseries modifiers filtered by parameters like start time, end time and modifier type

     Get timeseries modifiers filtered by parameters like start time, end time and modifier type.

    Args:
        start_time_modifiers (Union[Unset, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_time_modifiers (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        modifier_type (Union[Unset, str]):
        user_id (Union[Unset, str]):
        location_ids (Union[Unset, list[str]]): The parameter can be repeated
        module_instance_ids (Union[Unset, list[str]]): The parameter can be repeated
        only_active_modifiers (Union[Unset, TimeseriesmodifiersOnlyActiveModifiers]):
        user_defined_modifier_description (Union[Unset, str]):
        document_format (Union[Unset, TimeseriesmodifiersDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        start_time_modifiers=start_time_modifiers,
        end_time_modifiers=end_time_modifiers,
        modifier_type=modifier_type,
        user_id=user_id,
        location_ids=location_ids,
        module_instance_ids=module_instance_ids,
        only_active_modifiers=only_active_modifiers,
        user_defined_modifier_description=user_defined_modifier_description,
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
    start_time_modifiers: Unset | datetime.datetime = UNSET,
    end_time_modifiers: Unset | datetime.datetime = UNSET,
    modifier_type: Unset | str = UNSET,
    user_id: Unset | str = UNSET,
    location_ids: Unset | list[str] = UNSET,
    module_instance_ids: Unset | list[str] = UNSET,
    only_active_modifiers: Unset | TimeseriesmodifiersOnlyActiveModifiers = UNSET,
    user_defined_modifier_description: Unset | str = UNSET,
    document_format: Unset | TimeseriesmodifiersDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[Any]:
    """Get timeseries modifiers filtered by parameters like start time, end time and modifier type

     Get timeseries modifiers filtered by parameters like start time, end time and modifier type.

    Args:
        start_time_modifiers (Union[Unset, datetime.datetime]): Date-time string that adheres to
            RFC 3339. Example: 2020-03-18T15:00:00Z.
        end_time_modifiers (Union[Unset, datetime.datetime]): Date-time string that adheres to RFC
            3339. Example: 2020-03-18T15:00:00Z.
        modifier_type (Union[Unset, str]):
        user_id (Union[Unset, str]):
        location_ids (Union[Unset, list[str]]): The parameter can be repeated
        module_instance_ids (Union[Unset, list[str]]): The parameter can be repeated
        only_active_modifiers (Union[Unset, TimeseriesmodifiersOnlyActiveModifiers]):
        user_defined_modifier_description (Union[Unset, str]):
        document_format (Union[Unset, TimeseriesmodifiersDocumentFormat]):
        document_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        start_time_modifiers=start_time_modifiers,
        end_time_modifiers=end_time_modifiers,
        modifier_type=modifier_type,
        user_id=user_id,
        location_ids=location_ids,
        module_instance_ids=module_instance_ids,
        only_active_modifiers=only_active_modifiers,
        user_defined_modifier_description=user_defined_modifier_description,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
