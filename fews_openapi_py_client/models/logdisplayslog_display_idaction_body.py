from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LogdisplayslogDisplayIdactionBody")


@_attrs_define
class LogdisplayslogDisplayIdactionBody:
    """
    Attributes:
        log_displays_action (str): LogDisplaysAction in JSON format sent in the body of the post request. Json format
            is: https://fewsdocs.deltares.nl/webservices/rest-api/v1/schemas/pirest/pi_rest_logdisplays_action_post.json
    """

    log_displays_action: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        log_displays_action = self.log_displays_action

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "logDisplaysAction": log_displays_action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        log_displays_action = d.pop("logDisplaysAction")

        logdisplayslog_display_idaction_body = cls(
            log_displays_action=log_displays_action,
        )

        logdisplayslog_display_idaction_body.additional_properties = d
        return logdisplayslog_display_idaction_body

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
