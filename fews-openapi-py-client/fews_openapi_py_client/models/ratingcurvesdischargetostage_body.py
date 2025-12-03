from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RatingcurvesdischargetostageBody")


@_attrs_define
class RatingcurvesdischargetostageBody:
    discharge_values: str
    """ Discharge values in JSON format that conforms to the schema: https://fewsdocs.deltares.nl/webservices/rest-
    api/v1/schemas/pirest/pi_rest_ratingcurves_discharge.json. Example: {
      "dischargeValues" : [ "9920.0", "10200.0" ]
    } """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discharge_values = self.discharge_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dischargeValues": discharge_values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        discharge_values = d.pop("dischargeValues")

        ratingcurvesdischargetostage_body = cls(
            discharge_values=discharge_values,
        )

        ratingcurvesdischargetostage_body.additional_properties = d
        return ratingcurvesdischargetostage_body

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
