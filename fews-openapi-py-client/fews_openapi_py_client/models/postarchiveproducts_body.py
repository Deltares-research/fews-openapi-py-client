from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostarchiveproductsBody")


@_attrs_define
class PostarchiveproductsBody:
    file: str
    """ file to upload, used with the multipart/form-data encoding """
    product_content: str | Unset = UNSET
    """ Content of the product to upload as text. Alternative to the 'file' form field, used with the
    application/x-www-form-urlencoded encoding. Requires the fileName query parameter. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file

        product_content = self.product_content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if product_content is not UNSET:
            field_dict["productContent"] = product_content

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", (None, str(self.file).encode(), "text/plain")))

        if not isinstance(self.product_content, Unset):
            files.append(("productContent", (None, str(self.product_content).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = d.pop("file")

        product_content = d.pop("productContent", UNSET)

        postarchiveproducts_body = cls(
            file=file,
            product_content=product_content,
        )

        postarchiveproducts_body.additional_properties = d
        return postarchiveproducts_body

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
