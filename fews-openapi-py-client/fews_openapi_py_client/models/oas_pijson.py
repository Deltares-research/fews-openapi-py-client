from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OasPIJSON")


@_attrs_define
class OasPIJSON:
    """
    Example:
        {
              "openapi" : "3.0.3",
              "info" : {
                "title" : "Delft-FEWS Web Services REST API v1",
                "description" : "Delft-FEWS Web Services REST API v1. For more information see:
            https://publicwiki.deltares.nl/x/fwNdBw",
                "version" : "v1-2021-11-01T13:23:09Z"
              },
              "servers" : [ {
                "url" : "/FewsWebServices/rest/fewspiservice/v1",
                "description" : "API server"
              } ]

            }

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        oas_pijson = cls()

        oas_pijson.additional_properties = d
        return oas_pijson

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
