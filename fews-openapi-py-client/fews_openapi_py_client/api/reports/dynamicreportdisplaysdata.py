from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dynamicreportdisplaysdata_use_last_value import DynamicreportdisplaysdataUseLastValue
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    display_id: str,
    location_id: str | Unset = UNSET,
    time: str | Unset = UNSET,
    use_last_value: DynamicreportdisplaysdataUseLastValue | Unset = UNSET,
    time_zero: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["displayId"] = display_id

    params["locationId"] = location_id

    params["time"] = time

    json_use_last_value: str | Unset = UNSET
    if not isinstance(use_last_value, Unset):
        json_use_last_value = use_last_value.value

    params["useLastValue"] = json_use_last_value

    params["timeZero"] = time_zero

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dynamicreportdisplays/data",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

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
    display_id: str,
    location_id: str | Unset = UNSET,
    time: str | Unset = UNSET,
    use_last_value: DynamicreportdisplaysdataUseLastValue | Unset = UNSET,
    time_zero: str | Unset = UNSET,
) -> Response[Any]:
    """Get the json data that is used to render a dynamic report display

     Get the json data that is used to render a dynamic report display.

    Args:
        display_id (str):
        location_id (str | Unset):
        time (str | Unset):
        use_last_value (DynamicreportdisplaysdataUseLastValue | Unset):
        time_zero (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        display_id=display_id,
        location_id=location_id,
        time=time,
        use_last_value=use_last_value,
        time_zero=time_zero,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    display_id: str,
    location_id: str | Unset = UNSET,
    time: str | Unset = UNSET,
    use_last_value: DynamicreportdisplaysdataUseLastValue | Unset = UNSET,
    time_zero: str | Unset = UNSET,
) -> Response[Any]:
    """Get the json data that is used to render a dynamic report display

     Get the json data that is used to render a dynamic report display.

    Args:
        display_id (str):
        location_id (str | Unset):
        time (str | Unset):
        use_last_value (DynamicreportdisplaysdataUseLastValue | Unset):
        time_zero (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        display_id=display_id,
        location_id=location_id,
        time=time,
        use_last_value=use_last_value,
        time_zero=time_zero,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
