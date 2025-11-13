from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PosttimeseriesBody")


@_attrs_define
class PosttimeseriesBody:
    """
    Attributes:
        pi_time_series_xml_content (Union[Unset, str]): https://fewsdocs.deltares.nl/schemas/version1.0/pi-
            schemas/pi_timeseries.xsd
        pi_time_series_json_content (Union[Unset, str]): Since 2023.02. https://fewsdocs.deltares.nl/webservices/rest-
            api/v1/schemas/pirest/pi_rest_timeseries.json
    """

    pi_time_series_xml_content: Unset | str = UNSET
    pi_time_series_json_content: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pi_time_series_xml_content = self.pi_time_series_xml_content

        pi_time_series_json_content = self.pi_time_series_json_content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pi_time_series_xml_content is not UNSET:
            field_dict["piTimeSeriesXmlContent"] = pi_time_series_xml_content
        if pi_time_series_json_content is not UNSET:
            field_dict["piTimeSeriesJsonContent"] = pi_time_series_json_content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pi_time_series_xml_content = d.pop("piTimeSeriesXmlContent", UNSET)

        pi_time_series_json_content = d.pop("piTimeSeriesJsonContent", UNSET)

        posttimeseries_body = cls(
            pi_time_series_xml_content=pi_time_series_xml_content,
            pi_time_series_json_content=pi_time_series_json_content,
        )

        posttimeseries_body.additional_properties = d
        return posttimeseries_body

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
