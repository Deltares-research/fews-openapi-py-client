from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.locations_document_format import LocationsDocumentFormat
from ...models.locations_include_icon_names import LocationsIncludeIconNames
from ...models.locations_include_location_relations import LocationsIncludeLocationRelations
from ...models.locations_include_time_dependency import LocationsIncludeTimeDependency
from ...models.locations_show_attributes import LocationsShowAttributes
from ...models.locations_show_parent_locations import LocationsShowParentLocations
from ...models.locations_show_thresholds import LocationsShowThresholds
from ...models.locations_show_time_series_info import LocationsShowTimeSeriesInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_id: str | Unset = UNSET,
    parameter_ids: str | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    show_time_series_info: LocationsShowTimeSeriesInfo | Unset = UNSET,
    parameter_group_id: str | Unset = UNSET,
    show_attributes: LocationsShowAttributes | Unset = UNSET,
    attribute_ids: list[str] | Unset = UNSET,
    show_parent_locations: LocationsShowParentLocations | Unset = UNSET,
    show_thresholds: LocationsShowThresholds | Unset = UNSET,
    include_icon_names: LocationsIncludeIconNames | Unset = UNSET,
    include_location_relations: LocationsIncludeLocationRelations | Unset = UNSET,
    include_time_dependency: LocationsIncludeTimeDependency | Unset = UNSET,
    document_format: LocationsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["filterId"] = filter_id

    params["parameterIds"] = parameter_ids

    json_location_ids: list[str] | Unset = UNSET
    if not isinstance(location_ids, Unset):
        json_location_ids = location_ids

    params["locationIds"] = json_location_ids

    json_show_time_series_info: str | Unset = UNSET
    if not isinstance(show_time_series_info, Unset):
        json_show_time_series_info = show_time_series_info.value

    params["showTimeSeriesInfo"] = json_show_time_series_info

    params["parameterGroupId"] = parameter_group_id

    json_show_attributes: str | Unset = UNSET
    if not isinstance(show_attributes, Unset):
        json_show_attributes = show_attributes.value

    params["showAttributes"] = json_show_attributes

    json_attribute_ids: list[str] | Unset = UNSET
    if not isinstance(attribute_ids, Unset):
        json_attribute_ids = attribute_ids

    params["attributeIds"] = json_attribute_ids

    json_show_parent_locations: str | Unset = UNSET
    if not isinstance(show_parent_locations, Unset):
        json_show_parent_locations = show_parent_locations.value

    params["showParentLocations"] = json_show_parent_locations

    json_show_thresholds: str | Unset = UNSET
    if not isinstance(show_thresholds, Unset):
        json_show_thresholds = show_thresholds.value

    params["showThresholds"] = json_show_thresholds

    json_include_icon_names: str | Unset = UNSET
    if not isinstance(include_icon_names, Unset):
        json_include_icon_names = include_icon_names.value

    params["includeIconNames"] = json_include_icon_names

    json_include_location_relations: str | Unset = UNSET
    if not isinstance(include_location_relations, Unset):
        json_include_location_relations = include_location_relations.value

    params["includeLocationRelations"] = json_include_location_relations

    json_include_time_dependency: str | Unset = UNSET
    if not isinstance(include_time_dependency, Unset):
        json_include_time_dependency = include_time_dependency.value

    params["includeTimeDependency"] = json_include_time_dependency

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/locations",
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
    parameter_ids: str | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    show_time_series_info: LocationsShowTimeSeriesInfo | Unset = UNSET,
    parameter_group_id: str | Unset = UNSET,
    show_attributes: LocationsShowAttributes | Unset = UNSET,
    attribute_ids: list[str] | Unset = UNSET,
    show_parent_locations: LocationsShowParentLocations | Unset = UNSET,
    show_thresholds: LocationsShowThresholds | Unset = UNSET,
    include_icon_names: LocationsIncludeIconNames | Unset = UNSET,
    include_location_relations: LocationsIncludeLocationRelations | Unset = UNSET,
    include_time_dependency: LocationsIncludeTimeDependency | Unset = UNSET,
    document_format: LocationsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get locations that are available for the 'filterId' argument

     Get locations that are available for the 'filterId' argument. Locations are also returned if no time
    series are available for a location in the filter. If not filterId is passed then all locations
    configured in the pre-defined filter will be returned.

    Args:
        filter_id (str | Unset):
        parameter_ids (str | Unset):
        location_ids (list[str] | Unset): The parameter can be repeated
        show_time_series_info (LocationsShowTimeSeriesInfo | Unset):
        parameter_group_id (str | Unset):
        show_attributes (LocationsShowAttributes | Unset):
        attribute_ids (list[str] | Unset): The parameter can be repeated
        show_parent_locations (LocationsShowParentLocations | Unset):
        show_thresholds (LocationsShowThresholds | Unset):
        include_icon_names (LocationsIncludeIconNames | Unset):
        include_location_relations (LocationsIncludeLocationRelations | Unset):
        include_time_dependency (LocationsIncludeTimeDependency | Unset):
        document_format (LocationsDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        filter_id=filter_id,
        parameter_ids=parameter_ids,
        location_ids=location_ids,
        show_time_series_info=show_time_series_info,
        parameter_group_id=parameter_group_id,
        show_attributes=show_attributes,
        attribute_ids=attribute_ids,
        show_parent_locations=show_parent_locations,
        show_thresholds=show_thresholds,
        include_icon_names=include_icon_names,
        include_location_relations=include_location_relations,
        include_time_dependency=include_time_dependency,
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
    parameter_ids: str | Unset = UNSET,
    location_ids: list[str] | Unset = UNSET,
    show_time_series_info: LocationsShowTimeSeriesInfo | Unset = UNSET,
    parameter_group_id: str | Unset = UNSET,
    show_attributes: LocationsShowAttributes | Unset = UNSET,
    attribute_ids: list[str] | Unset = UNSET,
    show_parent_locations: LocationsShowParentLocations | Unset = UNSET,
    show_thresholds: LocationsShowThresholds | Unset = UNSET,
    include_icon_names: LocationsIncludeIconNames | Unset = UNSET,
    include_location_relations: LocationsIncludeLocationRelations | Unset = UNSET,
    include_time_dependency: LocationsIncludeTimeDependency | Unset = UNSET,
    document_format: LocationsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get locations that are available for the 'filterId' argument

     Get locations that are available for the 'filterId' argument. Locations are also returned if no time
    series are available for a location in the filter. If not filterId is passed then all locations
    configured in the pre-defined filter will be returned.

    Args:
        filter_id (str | Unset):
        parameter_ids (str | Unset):
        location_ids (list[str] | Unset): The parameter can be repeated
        show_time_series_info (LocationsShowTimeSeriesInfo | Unset):
        parameter_group_id (str | Unset):
        show_attributes (LocationsShowAttributes | Unset):
        attribute_ids (list[str] | Unset): The parameter can be repeated
        show_parent_locations (LocationsShowParentLocations | Unset):
        show_thresholds (LocationsShowThresholds | Unset):
        include_icon_names (LocationsIncludeIconNames | Unset):
        include_location_relations (LocationsIncludeLocationRelations | Unset):
        include_time_dependency (LocationsIncludeTimeDependency | Unset):
        document_format (LocationsDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        filter_id=filter_id,
        parameter_ids=parameter_ids,
        location_ids=location_ids,
        show_time_series_info=show_time_series_info,
        parameter_group_id=parameter_group_id,
        show_attributes=show_attributes,
        attribute_ids=attribute_ids,
        show_parent_locations=show_parent_locations,
        show_thresholds=show_thresholds,
        include_icon_names=include_icon_names,
        include_location_relations=include_location_relations,
        include_time_dependency=include_time_dependency,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
