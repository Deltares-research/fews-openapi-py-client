from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.filtersactions_convert_datum import FiltersactionsConvertDatum
from ...models.filtersactions_document_format import FiltersactionsDocumentFormat
from ...models.filtersactions_include_non_resampled import FiltersactionsIncludeNonResampled
from ...models.filtersactions_resampling_methods import FiltersactionsResamplingMethods
from ...models.filtersactions_resampling_omit_missing import FiltersactionsResamplingOmitMissing
from ...models.filtersactions_use_display_units import FiltersactionsUseDisplayUnits
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_id: str | Unset = UNSET,
    parameter_group_id: str | Unset = UNSET,
    parameter_ids: str | Unset = UNSET,
    module_instance_ids: str | Unset = UNSET,
    location_ids: str | Unset = UNSET,
    time_zero: str | Unset = UNSET,
    resampling_methods: FiltersactionsResamplingMethods | Unset = UNSET,
    resampling_time_step_id: str | Unset = UNSET,
    resampling_omit_missing: FiltersactionsResamplingOmitMissing | Unset = UNSET,
    include_non_resampled: FiltersactionsIncludeNonResampled | Unset = UNSET,
    use_display_units: FiltersactionsUseDisplayUnits | Unset = UNSET,
    convert_datum: FiltersactionsConvertDatum | Unset = UNSET,
    document_format: FiltersactionsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["filterId"] = filter_id

    params["parameterGroupId"] = parameter_group_id

    params["parameterIds"] = parameter_ids

    params["moduleInstanceIds"] = module_instance_ids

    params["locationIds"] = location_ids

    params["timeZero"] = time_zero

    json_resampling_methods: str | Unset = UNSET
    if not isinstance(resampling_methods, Unset):
        json_resampling_methods = resampling_methods.value

    params["resamplingMethods"] = json_resampling_methods

    params["resamplingTimeStepId"] = resampling_time_step_id

    json_resampling_omit_missing: str | Unset = UNSET
    if not isinstance(resampling_omit_missing, Unset):
        json_resampling_omit_missing = resampling_omit_missing.value

    params["resamplingOmitMissing"] = json_resampling_omit_missing

    json_include_non_resampled: str | Unset = UNSET
    if not isinstance(include_non_resampled, Unset):
        json_include_non_resampled = include_non_resampled.value

    params["includeNonResampled"] = json_include_non_resampled

    json_use_display_units: str | Unset = UNSET
    if not isinstance(use_display_units, Unset):
        json_use_display_units = use_display_units.value

    params["useDisplayUnits"] = json_use_display_units

    json_convert_datum: str | Unset = UNSET
    if not isinstance(convert_datum, Unset):
        json_convert_datum = convert_datum.value

    params["convertDatum"] = json_convert_datum

    json_document_format: str | Unset = UNSET
    if not isinstance(document_format, Unset):
        json_document_format = document_format.value

    params["documentFormat"] = json_document_format

    params["documentVersion"] = document_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/filters/actions",
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
    parameter_group_id: str | Unset = UNSET,
    parameter_ids: str | Unset = UNSET,
    module_instance_ids: str | Unset = UNSET,
    location_ids: str | Unset = UNSET,
    time_zero: str | Unset = UNSET,
    resampling_methods: FiltersactionsResamplingMethods | Unset = UNSET,
    resampling_time_step_id: str | Unset = UNSET,
    resampling_omit_missing: FiltersactionsResamplingOmitMissing | Unset = UNSET,
    include_non_resampled: FiltersactionsIncludeNonResampled | Unset = UNSET,
    use_display_units: FiltersactionsUseDisplayUnits | Unset = UNSET,
    convert_datum: FiltersactionsConvertDatum | Unset = UNSET,
    document_format: FiltersactionsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get the actions for a set of filters

     Get the actions for a set of filters

    Args:
        filter_id (str | Unset):
        parameter_group_id (str | Unset):
        parameter_ids (str | Unset):
        module_instance_ids (str | Unset):
        location_ids (str | Unset):
        time_zero (str | Unset):
        resampling_methods (FiltersactionsResamplingMethods | Unset):
        resampling_time_step_id (str | Unset):
        resampling_omit_missing (FiltersactionsResamplingOmitMissing | Unset):
        include_non_resampled (FiltersactionsIncludeNonResampled | Unset):
        use_display_units (FiltersactionsUseDisplayUnits | Unset):
        convert_datum (FiltersactionsConvertDatum | Unset):
        document_format (FiltersactionsDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        filter_id=filter_id,
        parameter_group_id=parameter_group_id,
        parameter_ids=parameter_ids,
        module_instance_ids=module_instance_ids,
        location_ids=location_ids,
        time_zero=time_zero,
        resampling_methods=resampling_methods,
        resampling_time_step_id=resampling_time_step_id,
        resampling_omit_missing=resampling_omit_missing,
        include_non_resampled=include_non_resampled,
        use_display_units=use_display_units,
        convert_datum=convert_datum,
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
    parameter_group_id: str | Unset = UNSET,
    parameter_ids: str | Unset = UNSET,
    module_instance_ids: str | Unset = UNSET,
    location_ids: str | Unset = UNSET,
    time_zero: str | Unset = UNSET,
    resampling_methods: FiltersactionsResamplingMethods | Unset = UNSET,
    resampling_time_step_id: str | Unset = UNSET,
    resampling_omit_missing: FiltersactionsResamplingOmitMissing | Unset = UNSET,
    include_non_resampled: FiltersactionsIncludeNonResampled | Unset = UNSET,
    use_display_units: FiltersactionsUseDisplayUnits | Unset = UNSET,
    convert_datum: FiltersactionsConvertDatum | Unset = UNSET,
    document_format: FiltersactionsDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get the actions for a set of filters

     Get the actions for a set of filters

    Args:
        filter_id (str | Unset):
        parameter_group_id (str | Unset):
        parameter_ids (str | Unset):
        module_instance_ids (str | Unset):
        location_ids (str | Unset):
        time_zero (str | Unset):
        resampling_methods (FiltersactionsResamplingMethods | Unset):
        resampling_time_step_id (str | Unset):
        resampling_omit_missing (FiltersactionsResamplingOmitMissing | Unset):
        include_non_resampled (FiltersactionsIncludeNonResampled | Unset):
        use_display_units (FiltersactionsUseDisplayUnits | Unset):
        convert_datum (FiltersactionsConvertDatum | Unset):
        document_format (FiltersactionsDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        filter_id=filter_id,
        parameter_group_id=parameter_group_id,
        parameter_ids=parameter_ids,
        module_instance_ids=module_instance_ids,
        location_ids=location_ids,
        time_zero=time_zero,
        resampling_methods=resampling_methods,
        resampling_time_step_id=resampling_time_step_id,
        resampling_omit_missing=resampling_omit_missing,
        include_non_resampled=include_non_resampled,
        use_display_units=use_display_units,
        convert_datum=convert_datum,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
