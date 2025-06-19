import logging
from typing import Dict, Optional, Any
from .models import Schema, Variable, VariableType

logger = logging.getLogger(__name__)


class SchemaManager:
    """Business logic for schema management"""

    def __init__(self):
        self.schemas: Dict[str, Schema] = {}

    def add_schema(self, schema: Schema) -> bool:
        """Add a new schema"""
        if schema.name in self.schemas:
            return False
        self.schemas[schema.name] = schema
        return True

    def update_schema(self, old_name: str, schema: Schema) -> bool:
        """Update an existing schema"""
        if old_name != schema.name and schema.name in self.schemas:
            return False
        if old_name != schema.name:
            del self.schemas[old_name]
        self.schemas[schema.name] = schema
        return True

    def delete_schema(self, name: str) -> bool:
        """Delete a schema"""
        if name in self.schemas:
            del self.schemas[name]
            return True
        return False

    def get_schema(self, name: str) -> Optional[Schema]:
        """Get a schema by name"""
        return self.schemas.get(name)

    def duplicate_schema(self, name: str, new_name: str) -> bool:
        """Duplicate a schema"""
        if name not in self.schemas or new_name in self.schemas:
            return False
        original = self.schemas[name]
        # Create a deep copy
        new_schema = Schema(
            name=new_name,
            page_title_cn=original.page_title_cn,
            page_title_en=original.page_title_en,
            match_img=original.match_img,
            filter_with=original.filter_with,
            basic_variables=original.basic_variables.copy(),
            more_variables=original.more_variables.copy(),
            image_variables=original.image_variables.copy(),
            url_variables=original.url_variables.copy(),
            array_variables=original.array_variables.copy(),
            language_item_variables=original.language_item_variables.copy(),
        )
        self.schemas[new_name] = new_schema
        return True

    def export_schemas(self) -> Dict[str, Any]:
        """Export all schemas as dictionary"""
        return {name: schema.to_dict() for name, schema in self.schemas.items()}

    def import_schemas(self, data: Dict[str, Any]):
        """Import schemas from dictionary"""
        self.schemas.clear()
        for name, schema_data in data.items():
            schema = self._parse_schema(name, schema_data)
            if schema:
                self.schemas[name] = schema

    def _parse_schema(self, name: str, data: Dict[str, Any]) -> Optional[Schema]:
        """Parse schema from dictionary"""
        try:
            schema = Schema(name=name)
            schema.page_title_cn = data.get("page_title_cn", "")
            schema.page_title_en = data.get("page_title_en", "")
            schema.match_img = data.get("match_img", "no")
            schema.filter_with = data.get("filter_with", "no")

            # Parse variables
            for var_type in VariableType:
                var_list = data.get(var_type.value, [])
                parsed_vars = []
                for var_dict in var_list:
                    for var_name, var_data in var_dict.items():
                        var = Variable(
                            name=var_name,
                            en_text=var_data.get("en", ""),
                            cn_text=var_data.get("cn", ""),
                            rows=var_data.get("rows", 0),
                        )
                        parsed_vars.append(var)
                setattr(schema, var_type.value, parsed_vars)

            return schema
        except Exception as e:
            logger.error(f"Error parsing schema {name}: {e}")
            return None
