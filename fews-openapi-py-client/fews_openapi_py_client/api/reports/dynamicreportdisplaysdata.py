from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dynamicreportdisplaysdata_use_last_value import DynamicreportdisplaysdataUseLastValue
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    display_id: str,
    location_id: Union[Unset, str] = UNSET,
    time: Union[Unset, str] = UNSET,
    use_last_value: Union[Unset, DynamicreportdisplaysdataUseLastValue] = UNSET,
    time_zero: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["displayId"] = display_id

    params["locationId"] = location_id

    params["time"] = time

    json_use_last_value: Union[Unset, str] = UNSET
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


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    display_id: str,
    location_id: Union[Unset, str] = UNSET,
    time: Union[Unset, str] = UNSET,
    use_last_value: Union[Unset, DynamicreportdisplaysdataUseLastValue] = UNSET,
    time_zero: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get the json data that is used to render a dynamic report display

     Get the json data that is used to render a dynamic report display.

    Args:
        display_id (str):
        location_id (Union[Unset, str]):
        time (Union[Unset, str]):
        use_last_value (Union[Unset, DynamicreportdisplaysdataUseLastValue]):
        time_zero (Union[Unset, str]):

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
    client: Union[AuthenticatedClient, Client],
    display_id: str,
    location_id: Union[Unset, str] = UNSET,
    time: Union[Unset, str] = UNSET,
    use_last_value: Union[Unset, DynamicreportdisplaysdataUseLastValue] = UNSET,
    time_zero: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Get the json data that is used to render a dynamic report display

     Get the json data that is used to render a dynamic report display.

    Args:
        display_id (str):
        location_id (Union[Unset, str]):
        time (Union[Unset, str]):
        use_last_value (Union[Unset, DynamicreportdisplaysdataUseLastValue]):
        time_zero (Union[Unset, str]):

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
