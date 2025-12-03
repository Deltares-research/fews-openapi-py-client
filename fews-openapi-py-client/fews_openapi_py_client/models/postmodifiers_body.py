from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostmodifiersBody")


@_attrs_define
class PostmodifiersBody:
    pi_modifiers_xml_content: str
    """ https://fewsdocs.deltares.nl/schemas/version1.0/pi-schemas/pi_modifiers.xsd """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pi_modifiers_xml_content = self.pi_modifiers_xml_content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "piModifiersXmlContent": pi_modifiers_xml_content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pi_modifiers_xml_content = d.pop("piModifiersXmlContent")

        postmodifiers_body = cls(
            pi_modifiers_xml_content=pi_modifiers_xml_content,
        )

        postmodifiers_body.additional_properties = d
        return postmodifiers_body

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
