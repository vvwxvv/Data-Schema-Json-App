from typing import Dict, List, Optional, Any
from typing import Type
from assets.models import Schema, Variable
from templates.base import BaseTemplate
from templates.registry import template_registry, TemplateRegistry


class SchemaTemplate:
    """Wrapper for backward compatibility"""

    def __init__(self, name: str, description: str, preview_data: Dict[str, Any]):
        self.name = name
        self.description = description
        self.preview_data = preview_data

    def to_schema(self, schema_name: str) -> Schema:
        """Convert template to actual schema (legacy method)"""
        schema = Schema(name=schema_name)

        # Copy basic info
        schema.page_title_cn = self.preview_data.get("page_title_cn", "")
        schema.page_title_en = self.preview_data.get("page_title_en", "")
        schema.match_img = self.preview_data.get("match_img", "no")
        schema.filter_with = self.preview_data.get("filter_with", "no")

        # Copy variables (existing logic)
        for var_type in [
            "basic_variables",
            "more_variables",
            "image_variables",
            "url_variables",
            "array_variables",
            "language_item_variables",
        ]:
            var_list = self.preview_data.get(var_type, [])
            schema_vars = []
            for var_dict in var_list:
                for var_name, var_data in var_dict.items():
                    var = Variable(
                        name=var_name,
                        en_text=var_data.get("en", ""),
                        cn_text=var_data.get("cn", ""),
                        rows=var_data.get("rows", 0),
                    )
                    schema_vars.append(var)
            setattr(schema, var_type, schema_vars)

        return schema


class TemplateManager:
    """Enhanced template manager with new template system"""

    def __init__(self, registry: Optional[TemplateRegistry] = None):
        self.registry = registry or template_registry
        self._legacy_templates: Dict[str, SchemaTemplate] = {}

    def get_template(self, template_id: str) -> BaseTemplate:
        """Get template instance"""
        return self.registry.create_template(template_id)

    def get_legacy_template(self, template_id: str) -> SchemaTemplate:
        """Get legacy template format for backward compatibility"""
        if template_id in self._legacy_templates:
            return self._legacy_templates[template_id]

        # Convert new template to legacy format
        template = self.get_template(template_id)
        legacy_template = SchemaTemplate(
            name=template.metadata.name,
            description=template.metadata.description,
            preview_data=template.to_preview_data(),
        )

        self._legacy_templates[template_id] = legacy_template
        return legacy_template

    def create_schema_from_template(self, template_id: str, schema_name: str) -> Schema:
        """Create schema from template"""
        template = self.get_template(template_id)
        return template.to_schema(schema_name)

    def list_templates(self) -> List[str]:
        """List all available templates"""
        return self.registry.list_templates()

    def search_templates(self, **criteria) -> List[str]:
        """Search templates by criteria"""
        return self.registry.search_templates(**criteria)

    def register_custom_template(
        self, template_id: str, template_class: Type[BaseTemplate]
    ):
        """Register a custom template"""
        self.registry.register(template_id, template_class)
        # Clear legacy cache for this template
        if template_id in self._legacy_templates:
            del self._legacy_templates[template_id]

    def get_template_info(self, template_id: str) -> Dict:
        """Get comprehensive template information"""
        template = self.get_template(template_id)
        return {
            "id": template_id,
            "metadata": template.metadata,
            "preview_data": template.to_preview_data(),
        }
