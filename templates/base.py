from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from assets.models import Schema, Variable


@dataclass
class TemplateVariable:
    """Represents a template variable with metadata"""

    name: str
    en_text: str
    cn_text: str
    rows: int = 1
    required: bool = True
    default_value: str = ""
    validation_rules: Optional[Dict[str, Any]] = None


@dataclass
class TemplateMetadata:
    """Template metadata and configuration"""

    name: str
    description: str
    category: str
    version: str = "1.0.0"
    author: str = "System"
    tags: List[str] = field(default_factory=list)
    requires_images: bool = False
    requires_filtering: bool = False


class BaseTemplate(ABC):
    """Abstract base class for all schema templates"""

    def __init__(self):
        self.metadata = self._get_metadata()
        self._validate_template()

    @abstractmethod
    def _get_metadata(self) -> TemplateMetadata:
        """Return template metadata"""
        pass

    @abstractmethod
    def _get_basic_variables(self) -> List[TemplateVariable]:
        """Return basic variables for the template"""
        pass

    @abstractmethod
    def _get_more_variables(self) -> List[TemplateVariable]:
        """Return extended variables for the template"""
        pass

    def _get_image_variables(self) -> List[TemplateVariable]:
        """Return image variables (optional override)"""
        return []

    def _get_url_variables(self) -> List[TemplateVariable]:
        """Return URL variables (optional override)"""
        return []

    def _get_array_variables(self) -> List[TemplateVariable]:
        """Return array variables (optional override)"""
        return []

    def _get_language_item_variables(self) -> List[TemplateVariable]:
        """Return language item variables (optional override)"""
        return []

    def _get_page_config(self) -> Dict[str, str]:
        """Return page configuration"""
        return {
            "page_title_cn": "页面标题",
            "page_title_en": "Page Title",
            "match_img": "no",
            "filter_with": "no",
        }

    def _validate_template(self) -> None:
        """Validate template configuration"""
        required_methods = [
            "_get_metadata",
            "_get_basic_variables",
            "_get_more_variables",
        ]
        for method in required_methods:
            if not hasattr(self, method):
                raise NotImplementedError(f"Template must implement {method}")

    def to_preview_data(self) -> Dict[str, Any]:
        """Convert template to preview data format"""
        preview_data = self._get_page_config().copy()

        # Convert template variables to preview format
        variable_mappings = {
            "basic_variables": self._get_basic_variables(),
            "more_variables": self._get_more_variables(),
            "image_variables": self._get_image_variables(),
            "url_variables": self._get_url_variables(),
            "array_variables": self._get_array_variables(),
            "language_item_variables": self._get_language_item_variables(),
        }

        for var_type, variables in variable_mappings.items():
            preview_data[var_type] = [
                {var.name: {"en": var.en_text, "cn": var.cn_text, "rows": var.rows}}
                for var in variables
            ]

        return preview_data

    def to_schema(self, schema_name: str) -> Schema:
        """Convert template to actual schema"""
        schema = Schema(name=schema_name)

        # Set page configuration
        page_config = self._get_page_config()
        schema.page_title_cn = page_config.get("page_title_cn", "")
        schema.page_title_en = page_config.get("page_title_en", "")
        schema.match_img = page_config.get("match_img", "no")
        schema.filter_with = page_config.get("filter_with", "no")

        # Convert template variables to schema variables
        variable_mappings = {
            "basic_variables": self._get_basic_variables(),
            "more_variables": self._get_more_variables(),
            "image_variables": self._get_image_variables(),
            "url_variables": self._get_url_variables(),
            "array_variables": self._get_array_variables(),
            "language_item_variables": self._get_language_item_variables(),
        }

        for var_type, template_vars in variable_mappings.items():
            schema_vars = []
            for template_var in template_vars:
                var = Variable(
                    name=template_var.name,
                    en_text=template_var.en_text,
                    cn_text=template_var.cn_text,
                    rows=template_var.rows,
                )
                schema_vars.append(var)
            setattr(schema, var_type, schema_vars)

        return schema
