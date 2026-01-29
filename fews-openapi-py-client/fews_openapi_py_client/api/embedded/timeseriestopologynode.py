import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.timeseriestopologynode_convert_datum import TimeseriestopologynodeConvertDatum
from ...models.timeseriestopologynode_document_format import TimeseriestopologynodeDocumentFormat
from ...models.timeseriestopologynode_omit_missing import TimeseriestopologynodeOmitMissing
from ...models.timeseriestopologynode_thresholds_visible import TimeseriestopologynodeThresholdsVisible
from ...models.timeseriestopologynode_use_display_units import TimeseriestopologynodeUseDisplayUnits
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    topology_node_id: str | Unset = UNSET,
    time_zero: datetime.datetime | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    thresholds_visible: TimeseriestopologynodeThresholdsVisible | Unset = UNSET,
    omit_missing: TimeseriestopologynodeOmitMissing | Unset = UNSET,
    use_display_units: TimeseriestopologynodeUseDisplayUnits | Unset = UNSET,
    convert_datum: TimeseriestopologynodeConvertDatum | Unset = UNSET,
    document_format: TimeseriestopologynodeDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["topologyNodeId"] = topology_node_id

    json_time_zero: str | Unset = UNSET
    if not isinstance(time_zero, Unset):
        json_time_zero = time_zero.isoformat()
    params["timeZero"] = json_time_zero

    json_start_time: str | Unset = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: str | Unset = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    json_thresholds_visible: str | Unset = UNSET
    if not isinstance(thresholds_visible, Unset):
        json_thresholds_visible = thresholds_visible.value

    params["thresholdsVisible"] = json_thresholds_visible

    json_omit_missing: str | Unset = UNSET
    if not isinstance(omit_missing, Unset):
        json_omit_missing = omit_missing.value

    params["omitMissing"] = json_omit_missing

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
        "url": "/timeseries/topology/node",
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
    topology_node_id: str | Unset = UNSET,
    time_zero: datetime.datetime | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    thresholds_visible: TimeseriestopologynodeThresholdsVisible | Unset = UNSET,
    omit_missing: TimeseriestopologynodeOmitMissing | Unset = UNSET,
    use_display_units: TimeseriestopologynodeUseDisplayUnits | Unset = UNSET,
    convert_datum: TimeseriestopologynodeConvertDatum | Unset = UNSET,
    document_format: TimeseriestopologynodeDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get the time series for the selected topology node

     Get the time series for the selected topology node. Only supported when running as a embedded tomcat
    service in the Operator Client or in a Stand Alone. Since 2022.02

    Args:
        topology_node_id (str | Unset):  Example: myNodeId.
        time_zero (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-19T15:00:00Z.
        thresholds_visible (TimeseriestopologynodeThresholdsVisible | Unset):  Example: true.
        omit_missing (TimeseriestopologynodeOmitMissing | Unset):
        use_display_units (TimeseriestopologynodeUseDisplayUnits | Unset):
        convert_datum (TimeseriestopologynodeConvertDatum | Unset):
        document_format (TimeseriestopologynodeDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        topology_node_id=topology_node_id,
        time_zero=time_zero,
        start_time=start_time,
        end_time=end_time,
        thresholds_visible=thresholds_visible,
        omit_missing=omit_missing,
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
    topology_node_id: str | Unset = UNSET,
    time_zero: datetime.datetime | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    thresholds_visible: TimeseriestopologynodeThresholdsVisible | Unset = UNSET,
    omit_missing: TimeseriestopologynodeOmitMissing | Unset = UNSET,
    use_display_units: TimeseriestopologynodeUseDisplayUnits | Unset = UNSET,
    convert_datum: TimeseriestopologynodeConvertDatum | Unset = UNSET,
    document_format: TimeseriestopologynodeDocumentFormat | Unset = UNSET,
    document_version: str | Unset = UNSET,
) -> Response[Any]:
    """Get the time series for the selected topology node

     Get the time series for the selected topology node. Only supported when running as a embedded tomcat
    service in the Operator Client or in a Stand Alone. Since 2022.02

    Args:
        topology_node_id (str | Unset):  Example: myNodeId.
        time_zero (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-19T15:00:00Z.
        thresholds_visible (TimeseriestopologynodeThresholdsVisible | Unset):  Example: true.
        omit_missing (TimeseriestopologynodeOmitMissing | Unset):
        use_display_units (TimeseriestopologynodeUseDisplayUnits | Unset):
        convert_datum (TimeseriestopologynodeConvertDatum | Unset):
        document_format (TimeseriestopologynodeDocumentFormat | Unset):
        document_version (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        topology_node_id=topology_node_id,
        time_zero=time_zero,
        start_time=start_time,
        end_time=end_time,
        thresholds_visible=thresholds_visible,
        omit_missing=omit_missing,
        use_display_units=use_display_units,
        convert_datum=convert_datum,
        document_format=document_format,
        document_version=document_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
