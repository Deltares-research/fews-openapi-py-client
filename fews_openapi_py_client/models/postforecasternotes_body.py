from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostforecasternotesBody")


@_attrs_define
class PostforecasternotesBody:
    """
    Attributes:
        forecaster_note (str): JSON payload conform the schema: pi_rest_forecaster_notes_post.json. Forecaster note in
            JSON format sent in the body of the post request. To update an existing forecaster note, the id and taskRunId
            has to be passed. Json format is: https://fewsdocs.deltares.nl/webservices/rest-
            api/v1/schemas/pirest/pi_rest_forecaster_notes_post.json
    """

    forecaster_note: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        forecaster_note = self.forecaster_note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "forecasterNote": forecaster_note,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        forecaster_note = d.pop("forecasterNote")

        postforecasternotes_body = cls(
            forecaster_note=forecaster_note,
        )

        postforecasternotes_body.additional_properties = d
        return postforecasternotes_body

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
