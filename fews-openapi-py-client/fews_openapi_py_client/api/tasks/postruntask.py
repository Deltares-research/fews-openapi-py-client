import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.postruntask_body import PostruntaskBody
from ...models.postruntask_run_locally_and_promote_to_server import PostruntaskRunLocallyAndPromoteToServer
from ...models.postruntask_run_option import PostruntaskRunOption
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostruntaskBody | Unset = UNSET,
    workflow_id: str,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    time_zero: datetime.datetime | Unset = UNSET,
    cold_state_id: str | Unset = UNSET,
    scenario_id: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    run_option: PostruntaskRunOption | Unset = UNSET,
    run_locally_and_promote_to_server: PostruntaskRunLocallyAndPromoteToServer | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

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

    json_time_zero: str | Unset = UNSET
    if not isinstance(time_zero, Unset):
        json_time_zero = time_zero.isoformat()
    params["timeZero"] = json_time_zero

    params["coldStateId"] = cold_state_id

    params["scenarioId"] = scenario_id

    params["userId"] = user_id

    params["description"] = description

    json_run_option: str | Unset = UNSET
    if not isinstance(run_option, Unset):
        json_run_option = run_option.value

    params["runOption"] = json_run_option

    json_run_locally_and_promote_to_server: str | Unset = UNSET
    if not isinstance(run_locally_and_promote_to_server, Unset):
        json_run_locally_and_promote_to_server = run_locally_and_promote_to_server.value

    params["runLocallyAndPromoteToServer"] = json_run_locally_and_promote_to_server

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/runtask",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> str | None:
    if response.status_code == 200:
        response_200 = response.text
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
    body: PostruntaskBody | Unset = UNSET,
    workflow_id: str,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    time_zero: datetime.datetime | Unset = UNSET,
    cold_state_id: str | Unset = UNSET,
    scenario_id: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    run_option: PostruntaskRunOption | Unset = UNSET,
    run_locally_and_promote_to_server: PostruntaskRunLocallyAndPromoteToServer | Unset = UNSET,
) -> Response[str]:
    """Runs a one-off task for a given workflowId

     Runs a one-off task for a given workflowId. The application/x-www-form-urlencoded encoding has to be
    used. Returns a handle to the task in the form of a taskId. This taskId can be used to track the
    status of the workflow using the taskrunstatus method. Since 2018.02 it is possible to use a
    workflow descriptor attribute: waitWhenAlreadyRunning. This will allow running a task that hasn't
    been scheduled to wait when another task of that workflow is already running.
    Since 2022.02 properties can be included in the url. These will be used as taskRunProperties, and
    override global or workflow properties. Each property has to be added to the URL separately.
    Example: &property(fileName)=exportFile&property(outputValue)=9.0 , where the name of the property
    is fileName, the value is exportFile. The name of the second property is outputValue, the value is
    9.0

    Args:
        workflow_id (str):
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        time_zero (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        cold_state_id (str | Unset):
        scenario_id (str | Unset):
        user_id (str | Unset):
        description (str | Unset):
        run_option (PostruntaskRunOption | Unset):
        run_locally_and_promote_to_server (PostruntaskRunLocallyAndPromoteToServer | Unset):
        body (PostruntaskBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        body=body,
        workflow_id=workflow_id,
        start_time=start_time,
        end_time=end_time,
        time_zero=time_zero,
        cold_state_id=cold_state_id,
        scenario_id=scenario_id,
        user_id=user_id,
        description=description,
        run_option=run_option,
        run_locally_and_promote_to_server=run_locally_and_promote_to_server,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PostruntaskBody | Unset = UNSET,
    workflow_id: str,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    time_zero: datetime.datetime | Unset = UNSET,
    cold_state_id: str | Unset = UNSET,
    scenario_id: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    run_option: PostruntaskRunOption | Unset = UNSET,
    run_locally_and_promote_to_server: PostruntaskRunLocallyAndPromoteToServer | Unset = UNSET,
) -> str | None:
    """Runs a one-off task for a given workflowId

     Runs a one-off task for a given workflowId. The application/x-www-form-urlencoded encoding has to be
    used. Returns a handle to the task in the form of a taskId. This taskId can be used to track the
    status of the workflow using the taskrunstatus method. Since 2018.02 it is possible to use a
    workflow descriptor attribute: waitWhenAlreadyRunning. This will allow running a task that hasn't
    been scheduled to wait when another task of that workflow is already running.
    Since 2022.02 properties can be included in the url. These will be used as taskRunProperties, and
    override global or workflow properties. Each property has to be added to the URL separately.
    Example: &property(fileName)=exportFile&property(outputValue)=9.0 , where the name of the property
    is fileName, the value is exportFile. The name of the second property is outputValue, the value is
    9.0

    Args:
        workflow_id (str):
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        time_zero (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        cold_state_id (str | Unset):
        scenario_id (str | Unset):
        user_id (str | Unset):
        description (str | Unset):
        run_option (PostruntaskRunOption | Unset):
        run_locally_and_promote_to_server (PostruntaskRunLocallyAndPromoteToServer | Unset):
        body (PostruntaskBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return sync_detailed(
        client=client,
        body=body,
        workflow_id=workflow_id,
        start_time=start_time,
        end_time=end_time,
        time_zero=time_zero,
        cold_state_id=cold_state_id,
        scenario_id=scenario_id,
        user_id=user_id,
        description=description,
        run_option=run_option,
        run_locally_and_promote_to_server=run_locally_and_promote_to_server,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostruntaskBody | Unset = UNSET,
    workflow_id: str,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    time_zero: datetime.datetime | Unset = UNSET,
    cold_state_id: str | Unset = UNSET,
    scenario_id: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    run_option: PostruntaskRunOption | Unset = UNSET,
    run_locally_and_promote_to_server: PostruntaskRunLocallyAndPromoteToServer | Unset = UNSET,
) -> Response[str]:
    """Runs a one-off task for a given workflowId

     Runs a one-off task for a given workflowId. The application/x-www-form-urlencoded encoding has to be
    used. Returns a handle to the task in the form of a taskId. This taskId can be used to track the
    status of the workflow using the taskrunstatus method. Since 2018.02 it is possible to use a
    workflow descriptor attribute: waitWhenAlreadyRunning. This will allow running a task that hasn't
    been scheduled to wait when another task of that workflow is already running.
    Since 2022.02 properties can be included in the url. These will be used as taskRunProperties, and
    override global or workflow properties. Each property has to be added to the URL separately.
    Example: &property(fileName)=exportFile&property(outputValue)=9.0 , where the name of the property
    is fileName, the value is exportFile. The name of the second property is outputValue, the value is
    9.0

    Args:
        workflow_id (str):
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        time_zero (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        cold_state_id (str | Unset):
        scenario_id (str | Unset):
        user_id (str | Unset):
        description (str | Unset):
        run_option (PostruntaskRunOption | Unset):
        run_locally_and_promote_to_server (PostruntaskRunLocallyAndPromoteToServer | Unset):
        body (PostruntaskBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
    """

    kwargs = _get_kwargs(
        body=body,
        workflow_id=workflow_id,
        start_time=start_time,
        end_time=end_time,
        time_zero=time_zero,
        cold_state_id=cold_state_id,
        scenario_id=scenario_id,
        user_id=user_id,
        description=description,
        run_option=run_option,
        run_locally_and_promote_to_server=run_locally_and_promote_to_server,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostruntaskBody | Unset = UNSET,
    workflow_id: str,
    start_time: datetime.datetime | Unset = UNSET,
    end_time: datetime.datetime | Unset = UNSET,
    time_zero: datetime.datetime | Unset = UNSET,
    cold_state_id: str | Unset = UNSET,
    scenario_id: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    run_option: PostruntaskRunOption | Unset = UNSET,
    run_locally_and_promote_to_server: PostruntaskRunLocallyAndPromoteToServer | Unset = UNSET,
) -> str | None:
    """Runs a one-off task for a given workflowId

     Runs a one-off task for a given workflowId. The application/x-www-form-urlencoded encoding has to be
    used. Returns a handle to the task in the form of a taskId. This taskId can be used to track the
    status of the workflow using the taskrunstatus method. Since 2018.02 it is possible to use a
    workflow descriptor attribute: waitWhenAlreadyRunning. This will allow running a task that hasn't
    been scheduled to wait when another task of that workflow is already running.
    Since 2022.02 properties can be included in the url. These will be used as taskRunProperties, and
    override global or workflow properties. Each property has to be added to the URL separately.
    Example: &property(fileName)=exportFile&property(outputValue)=9.0 , where the name of the property
    is fileName, the value is exportFile. The name of the second property is outputValue, the value is
    9.0

    Args:
        workflow_id (str):
        start_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339.
            Example: 2020-03-18T15:00:00Z.
        end_time (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        time_zero (datetime.datetime | Unset): Date-time string that adheres to RFC 3339. Example:
            2020-03-18T15:00:00Z.
        cold_state_id (str | Unset):
        scenario_id (str | Unset):
        user_id (str | Unset):
        description (str | Unset):
        run_option (PostruntaskRunOption | Unset):
        run_locally_and_promote_to_server (PostruntaskRunLocallyAndPromoteToServer | Unset):
        body (PostruntaskBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            workflow_id=workflow_id,
            start_time=start_time,
            end_time=end_time,
            time_zero=time_zero,
            cold_state_id=cold_state_id,
            scenario_id=scenario_id,
            user_id=user_id,
            description=description,
            run_option=run_option,
            run_locally_and_promote_to_server=run_locally_and_promote_to_server,
        )
    ).parsed
