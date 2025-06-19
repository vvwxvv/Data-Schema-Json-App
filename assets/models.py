from dataclasses import dataclass, field
from typing import Dict, List, Any
from enum import Enum


@dataclass
class Variable:
    """Data model for a variable"""

    name: str
    en_text: str = ""
    cn_text: str = ""
    rows: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {self.name: {"en": self.en_text, "cn": self.cn_text, "rows": self.rows}}


@dataclass
class Schema:
    """Data model for a schema"""

    name: str
    page_title_cn: str = ""
    page_title_en: str = ""
    match_img: str = "no"
    filter_with: str = "no"
    basic_variables: List[Variable] = field(default_factory=list)
    more_variables: List[Variable] = field(default_factory=list)
    image_variables: List[Variable] = field(default_factory=list)
    url_variables: List[Variable] = field(default_factory=list)
    array_variables: List[Variable] = field(default_factory=list)
    language_item_variables: List[Variable] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert schema to dictionary format"""
        return {
            "page_title_cn": self.page_title_cn,
            "page_title_en": self.page_title_en,
            "match_img": self.match_img,
            "filter_with": self.filter_with,
            "basic_variables": [var.to_dict() for var in self.basic_variables],
            "more_variables": [var.to_dict() for var in self.more_variables],
            "image_variables": [var.to_dict() for var in self.image_variables],
            "url_variables": [var.to_dict() for var in self.url_variables],
            "array_variables": [var.to_dict() for var in self.array_variables],
            "language_item_variables": [
                var.to_dict() for var in self.language_item_variables
            ],
        }


class VariableType(Enum):
    """Enumeration for variable types"""

    BASIC = "basic_variables"
    MORE = "more_variables"
    IMAGE = "image_variables"
    URL = "url_variables"
    ARRAY = "array_variables"
    LANGUAGE = "language_item_variables"
