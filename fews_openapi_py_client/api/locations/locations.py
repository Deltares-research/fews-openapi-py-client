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
from ...models.locations_show_time_series_infos import LocationsShowTimeSeriesInfos
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_id: Unset | str = UNSET,
    parameter_ids: Unset | str = UNSET,
    location_ids: Unset | list[str] = UNSET,
    parameter_group_id: Unset | str = UNSET,
    show_attributes: Unset | LocationsShowAttributes = UNSET,
    attribute_ids: Unset | list[str] = UNSET,
    show_parent_locations: Unset | LocationsShowParentLocations = UNSET,
    show_thresholds: Unset | LocationsShowThresholds = UNSET,
    show_time_series_infos: Unset | LocationsShowTimeSeriesInfos = UNSET,
    include_icon_names: Unset | LocationsIncludeIconNames = UNSET,
    include_location_relations: Unset | LocationsIncludeLocationRelations = UNSET,
    include_time_dependency: Unset | LocationsIncludeTimeDependency = UNSET,
    document_format: Unset | LocationsDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["filterId"] = filter_id

    params["parameterIds"] = parameter_ids

    json_location_ids: Unset | list[str] = UNSET
    if not isinstance(location_ids, Unset):
        json_location_ids = location_ids

    params["locationIds"] = json_location_ids

    params["parameterGroupId"] = parameter_group_id

    json_show_attributes: Unset | str = UNSET
    if not isinstance(show_attributes, Unset):
        json_show_attributes = show_attributes.value

    params["showAttributes"] = json_show_attributes

    json_attribute_ids: Unset | list[str] = UNSET
    if not isinstance(attribute_ids, Unset):
        json_attribute_ids = attribute_ids

    params["attributeIds"] = json_attribute_ids

    json_show_parent_locations: Unset | str = UNSET
    if not isinstance(show_parent_locations, Unset):
        json_show_parent_locations = show_parent_locations.value

    params["showParentLocations"] = json_show_parent_locations

    json_show_thresholds: Unset | str = UNSET
    if not isinstance(show_thresholds, Unset):
        json_show_thresholds = show_thresholds.value

    params["showThresholds"] = json_show_thresholds

    json_show_time_series_infos: Unset | str = UNSET
    if not isinstance(show_time_series_infos, Unset):
        json_show_time_series_infos = show_time_series_infos.value

    params["showTimeSeriesInfos"] = json_show_time_series_infos

    json_include_icon_names: Unset | str = UNSET
    if not isinstance(include_icon_names, Unset):
        json_include_icon_names = include_icon_names.value

    params["includeIconNames"] = json_include_icon_names

    json_include_location_relations: Unset | str = UNSET
    if not isinstance(include_location_relations, Unset):
        json_include_location_relations = include_location_relations.value

    params["includeLocationRelations"] = json_include_location_relations

    json_include_time_dependency: Unset | str = UNSET
    if not isinstance(include_time_dependency, Unset):
        json_include_time_dependency = include_time_dependency.value

    params["includeTimeDependency"] = json_include_time_dependency

    json_document_format: Unset | str = UNSET
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
    filter_id: Unset | str = UNSET,
    parameter_ids: Unset | str = UNSET,
    location_ids: Unset | list[str] = UNSET,
    parameter_group_id: Unset | str = UNSET,
    show_attributes: Unset | LocationsShowAttributes = UNSET,
    attribute_ids: Unset | list[str] = UNSET,
    show_parent_locations: Unset | LocationsShowParentLocations = UNSET,
    show_thresholds: Unset | LocationsShowThresholds = UNSET,
    show_time_series_infos: Unset | LocationsShowTimeSeriesInfos = UNSET,
    include_icon_names: Unset | LocationsIncludeIconNames = UNSET,
    include_location_relations: Unset | LocationsIncludeLocationRelations = UNSET,
    include_time_dependency: Unset | LocationsIncludeTimeDependency = UNSET,
    document_format: Unset | LocationsDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[Any]:
    """Get locations that are available for the 'filterId' argument

     Get locations that are available for the 'filterId' argument. Locations are also returned if no time
    series are available for a location in the filter. If not filterId is passed then all locations
    configured in the pre-defined filter will be returned.

    Args:
        filter_id (Union[Unset, str]):
        parameter_ids (Union[Unset, str]):
        location_ids (Union[Unset, list[str]]): The parameter can be repeated
        parameter_group_id (Union[Unset, str]):
        show_attributes (Union[Unset, LocationsShowAttributes]):
        attribute_ids (Union[Unset, list[str]]): The parameter can be repeated
        show_parent_locations (Union[Unset, LocationsShowParentLocations]):
        show_thresholds (Union[Unset, LocationsShowThresholds]):
        show_time_series_infos (Union[Unset, LocationsShowTimeSeriesInfos]):
        include_icon_names (Union[Unset, LocationsIncludeIconNames]):
        include_location_relations (Union[Unset, LocationsIncludeLocationRelations]):
        include_time_dependency (Union[Unset, LocationsIncludeTimeDependency]):
        document_format (Union[Unset, LocationsDocumentFormat]):
        document_version (Union[Unset, str]):

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
        parameter_group_id=parameter_group_id,
        show_attributes=show_attributes,
        attribute_ids=attribute_ids,
        show_parent_locations=show_parent_locations,
        show_thresholds=show_thresholds,
        show_time_series_infos=show_time_series_infos,
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
    filter_id: Unset | str = UNSET,
    parameter_ids: Unset | str = UNSET,
    location_ids: Unset | list[str] = UNSET,
    parameter_group_id: Unset | str = UNSET,
    show_attributes: Unset | LocationsShowAttributes = UNSET,
    attribute_ids: Unset | list[str] = UNSET,
    show_parent_locations: Unset | LocationsShowParentLocations = UNSET,
    show_thresholds: Unset | LocationsShowThresholds = UNSET,
    show_time_series_infos: Unset | LocationsShowTimeSeriesInfos = UNSET,
    include_icon_names: Unset | LocationsIncludeIconNames = UNSET,
    include_location_relations: Unset | LocationsIncludeLocationRelations = UNSET,
    include_time_dependency: Unset | LocationsIncludeTimeDependency = UNSET,
    document_format: Unset | LocationsDocumentFormat = UNSET,
    document_version: Unset | str = UNSET,
) -> Response[Any]:
    """Get locations that are available for the 'filterId' argument

     Get locations that are available for the 'filterId' argument. Locations are also returned if no time
    series are available for a location in the filter. If not filterId is passed then all locations
    configured in the pre-defined filter will be returned.

    Args:
        filter_id (Union[Unset, str]):
        parameter_ids (Union[Unset, str]):
        location_ids (Union[Unset, list[str]]): The parameter can be repeated
        parameter_group_id (Union[Unset, str]):
        show_attributes (Union[Unset, LocationsShowAttributes]):
        attribute_ids (Union[Unset, list[str]]): The parameter can be repeated
        show_parent_locations (Union[Unset, LocationsShowParentLocations]):
        show_thresholds (Union[Unset, LocationsShowThresholds]):
        show_time_series_infos (Union[Unset, LocationsShowTimeSeriesInfos]):
        include_icon_names (Union[Unset, LocationsIncludeIconNames]):
        include_location_relations (Union[Unset, LocationsIncludeLocationRelations]):
        include_time_dependency (Union[Unset, LocationsIncludeTimeDependency]):
        document_format (Union[Unset, LocationsDocumentFormat]):
        document_version (Union[Unset, str]):

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
        parameter_group_id=parameter_group_id,
        show_attributes=show_attributes,
        attribute_ids=attribute_ids,
        show_parent_locations=show_parent_locations,
        show_thresholds=show_thresholds,
        show_time_series_infos=show_time_series_infos,
        include_icon_names=include_icon_names,
        include_location_relations=include_location_relations,
        include_time_dependency=include_time_dependency,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
