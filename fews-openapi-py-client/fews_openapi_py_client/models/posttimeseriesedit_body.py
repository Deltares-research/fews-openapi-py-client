from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PosttimeserieseditBody")


@_attrs_define
class PosttimeserieseditBody:
    time_series: str
    """ Time Series sent in timeseries pi json format sent in the body of the post request. Json format is:
    https://fewsdocs.deltares.nl/webservices/rest-api/v1/schemas/pirest/pi_rest_timeseries.json """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time_series = self.time_series

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timeSeries": time_series,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time_series = d.pop("timeSeries")

        posttimeseriesedit_body = cls(
            time_series=time_series,
        )

        posttimeseriesedit_body.additional_properties = d
        return posttimeseriesedit_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
