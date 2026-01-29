import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.processdata_run_locally_and_promote_to_server import ProcessdataRunLocallyAndPromoteToServer
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workflow_id: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    x_min: str | Unset = UNSET,
    x_max: str | Unset = UNSET,
    y_min: str | Unset = UNSET,
    y_max: str | Unset = UNSET,
    x_cell_size: str | Unset = UNSET,
    y_cell_size: str | Unset = UNSET,
    run_locally_and_promote_to_server: ProcessdataRunLocallyAndPromoteToServer | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["workflowId"] = workflow_id

    json_start_time: str | Unset = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: str | Unset = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params["xMin"] = x_min

    params["xMax"] = x_max

    params["yMin"] = y_min

    params["yMax"] = y_max

    params["xCellSize"] = x_cell_size

    params["yCellSize"] = y_cell_size

    json_run_locally_and_promote_to_server: str | Unset = UNSET
    if not isinstance(run_locally_and_promote_to_server, Unset):
        json_run_locally_and_promote_to_server = run_locally_and_promote_to_server.value

    params["runLocallyAndPromoteToServer"] = json_run_locally_and_promote_to_server

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/processdata",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.content)
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    workflow_id: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    x_min: str | Unset = UNSET,
    x_max: str | Unset = UNSET,
    y_min: str | Unset = UNSET,
    y_max: str | Unset = UNSET,
    x_cell_size: str | Unset = UNSET,
    y_cell_size: str | Unset = UNSET,
    run_locally_and_promote_to_server: ProcessdataRunLocallyAndPromoteToServer | Unset = UNSET,
) -> Response[str]:
    """Run workflow and make processed netcdf data available as an attachment of type application/octet-
    stream

     Run workflow and make processed netcdf data available as an attachment of type application/octet-
    stream. A property EXPORT_FOLDER_PROCESS_DATA should be configured in the global properties or in
    the webservice properties. The workflow indicated by the workflow id should export data to a folder
    EXPORT_FOLDER_PROCESS_DATA. Readonly mode has to be disabled in the FewsPiService.properties to
    allow this functionality. Automatic clean-up of the output folder is not implemented.

    Args:
        workflow_id (str | Unset):
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        x_min (str | Unset):
        x_max (str | Unset):
        y_min (str | Unset):
        y_max (str | Unset):
        x_cell_size (str | Unset):
        y_cell_size (str | Unset):
        run_locally_and_promote_to_server (ProcessdataRunLocallyAndPromoteToServer | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        start_time=start_time,
        end_time=end_time,
        x_min=x_min,
        x_max=x_max,
        y_min=y_min,
        y_max=y_max,
        x_cell_size=x_cell_size,
        y_cell_size=y_cell_size,
        run_locally_and_promote_to_server=run_locally_and_promote_to_server,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    workflow_id: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    x_min: str | Unset = UNSET,
    x_max: str | Unset = UNSET,
    y_min: str | Unset = UNSET,
    y_max: str | Unset = UNSET,
    x_cell_size: str | Unset = UNSET,
    y_cell_size: str | Unset = UNSET,
    run_locally_and_promote_to_server: ProcessdataRunLocallyAndPromoteToServer | Unset = UNSET,
) -> str | None:
    """Run workflow and make processed netcdf data available as an attachment of type application/octet-
    stream

     Run workflow and make processed netcdf data available as an attachment of type application/octet-
    stream. A property EXPORT_FOLDER_PROCESS_DATA should be configured in the global properties or in
    the webservice properties. The workflow indicated by the workflow id should export data to a folder
    EXPORT_FOLDER_PROCESS_DATA. Readonly mode has to be disabled in the FewsPiService.properties to
    allow this functionality. Automatic clean-up of the output folder is not implemented.

    Args:
        workflow_id (str | Unset):
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        x_min (str | Unset):
        x_max (str | Unset):
        y_min (str | Unset):
        y_max (str | Unset):
        x_cell_size (str | Unset):
        y_cell_size (str | Unset):
        run_locally_and_promote_to_server (ProcessdataRunLocallyAndPromoteToServer | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        client=client,
        workflow_id=workflow_id,
        start_time=start_time,
        end_time=end_time,
        x_min=x_min,
        x_max=x_max,
        y_min=y_min,
        y_max=y_max,
        x_cell_size=x_cell_size,
        y_cell_size=y_cell_size,
        run_locally_and_promote_to_server=run_locally_and_promote_to_server,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    workflow_id: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    x_min: str | Unset = UNSET,
    x_max: str | Unset = UNSET,
    y_min: str | Unset = UNSET,
    y_max: str | Unset = UNSET,
    x_cell_size: str | Unset = UNSET,
    y_cell_size: str | Unset = UNSET,
    run_locally_and_promote_to_server: ProcessdataRunLocallyAndPromoteToServer | Unset = UNSET,
) -> Response[str]:
    """Run workflow and make processed netcdf data available as an attachment of type application/octet-
    stream

     Run workflow and make processed netcdf data available as an attachment of type application/octet-
    stream. A property EXPORT_FOLDER_PROCESS_DATA should be configured in the global properties or in
    the webservice properties. The workflow indicated by the workflow id should export data to a folder
    EXPORT_FOLDER_PROCESS_DATA. Readonly mode has to be disabled in the FewsPiService.properties to
    allow this functionality. Automatic clean-up of the output folder is not implemented.

    Args:
        workflow_id (str | Unset):
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        x_min (str | Unset):
        x_max (str | Unset):
        y_min (str | Unset):
        y_max (str | Unset):
        x_cell_size (str | Unset):
        y_cell_size (str | Unset):
        run_locally_and_promote_to_server (ProcessdataRunLocallyAndPromoteToServer | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        start_time=start_time,
        end_time=end_time,
        x_min=x_min,
        x_max=x_max,
        y_min=y_min,
        y_max=y_max,
        x_cell_size=x_cell_size,
        y_cell_size=y_cell_size,
        run_locally_and_promote_to_server=run_locally_and_promote_to_server,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    workflow_id: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    x_min: str | Unset = UNSET,
    x_max: str | Unset = UNSET,
    y_min: str | Unset = UNSET,
    y_max: str | Unset = UNSET,
    x_cell_size: str | Unset = UNSET,
    y_cell_size: str | Unset = UNSET,
    run_locally_and_promote_to_server: ProcessdataRunLocallyAndPromoteToServer | Unset = UNSET,
) -> str | None:
    """Run workflow and make processed netcdf data available as an attachment of type application/octet-
    stream

     Run workflow and make processed netcdf data available as an attachment of type application/octet-
    stream. A property EXPORT_FOLDER_PROCESS_DATA should be configured in the global properties or in
    the webservice properties. The workflow indicated by the workflow id should export data to a folder
    EXPORT_FOLDER_PROCESS_DATA. Readonly mode has to be disabled in the FewsPiService.properties to
    allow this functionality. Automatic clean-up of the output folder is not implemented.

    Args:
        workflow_id (str | Unset):
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        x_min (str | Unset):
        x_max (str | Unset):
        y_min (str | Unset):
        y_max (str | Unset):
        x_cell_size (str | Unset):
        y_cell_size (str | Unset):
        run_locally_and_promote_to_server (ProcessdataRunLocallyAndPromoteToServer | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            client=client,
            workflow_id=workflow_id,
            start_time=start_time,
            end_time=end_time,
            x_min=x_min,
            x_max=x_max,
            y_min=y_min,
            y_max=y_max,
            x_cell_size=x_cell_size,
            y_cell_size=y_cell_size,
            run_locally_and_promote_to_server=run_locally_and_promote_to_server,
        )
    ).parsed
