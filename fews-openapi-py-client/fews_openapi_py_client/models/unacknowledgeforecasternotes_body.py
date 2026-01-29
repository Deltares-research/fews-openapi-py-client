from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UnacknowledgeforecasternotesBody")


@_attrs_define
class UnacknowledgeforecasternotesBody:
    forecaster_note_keys: str
    """ JSON body conform the schema: pi_rest_forecaster_notes_log_keys_post.json. The Forecaster Notes keys have to
    be passed in JSON format in the body of the post request following this specification:
    https://fewsdocs.deltares.nl/webservices/rest-api/v1/schemas/pirest/pi_rest_forecaster_notes_log_keys_post.json
    """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        forecaster_note_keys = self.forecaster_note_keys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "forecasterNoteKeys": forecaster_note_keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        forecaster_note_keys = d.pop("forecasterNoteKeys")

        unacknowledgeforecasternotes_body = cls(
            forecaster_note_keys=forecaster_note_keys,
        )

        unacknowledgeforecasternotes_body.additional_properties = d
        return unacknowledgeforecasternotes_body

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
