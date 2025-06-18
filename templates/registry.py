from typing import Dict, Type, List, Optional
from .base import BaseTemplate, TemplateMetadata
from .template_artist import ArtistWebsiteTemplate
from .template_about import AboutTemplate
from .template_artwork import ArtworkTemplate
from .template_event import EventTemplate
from .template_mediacluster import MediaclusterTemplate
from .template_publication import PublicationsTemplate

# Import other templates as needed


class TemplateRegistry:
    """Central registry for all available templates"""

    def __init__(self):
        self._templates: Dict[str, Type[BaseTemplate]] = {}
        self._register_default_templates()

    def _register_default_templates(self):
        """Register default system templates using their REGISTRY_NAME"""

        self.auto_register(ArtistWebsiteTemplate)
        self.auto_register(AboutTemplate)
        self.auto_register(ArtworkTemplate)
        self.auto_register(EventTemplate)
        self.auto_register(MediaclusterTemplate)
        self.auto_register(PublicationsTemplate)

    def auto_register(self, template_class: Type[BaseTemplate]):
        """Automatically register a template using its REGISTRY_NAME"""
        if not hasattr(template_class, "REGISTRY_NAME"):
            raise ValueError(
                f"Template class {template_class.__name__} must have REGISTRY_NAME attribute"
            )

        registry_name = template_class.REGISTRY_NAME
        self.register(registry_name, template_class)

    def register(self, template_id: str, template_class: Type[BaseTemplate]):
        """Register a template class"""
        if not issubclass(template_class, BaseTemplate):
            raise ValueError(f"Template class must inherit from BaseTemplate")

        self._templates[template_id] = template_class

    def unregister(self, template_id: str):
        """Unregister a template"""
        if template_id in self._templates:
            del self._templates[template_id]

    def get_template_class(self, template_id: str) -> Type[BaseTemplate]:
        """Get template class by ID"""
        if template_id not in self._templates:
            raise KeyError(f"Template '{template_id}' not found")
        return self._templates[template_id]

    def create_template(self, template_id: str) -> BaseTemplate:
        """Create template instance by ID"""
        template_class = self.get_template_class(template_id)
        return template_class()

    def list_templates(self) -> List[str]:
        """List all registered template IDs"""
        return list(self._templates.keys())

    def get_template_metadata(self, template_id: str) -> TemplateMetadata:
        """Get template metadata without creating instance"""
        template = self.create_template(template_id)
        return template.metadata

    def get_registry_names(self) -> Dict[str, str]:
        """Get mapping of template class names to their registry names"""
        mapping = {}
        for template_id, template_class in self._templates.items():
            mapping[template_class.__name__] = template_id
        return mapping

    def print_template_registry_info(self):
        """Print information about all registered templates and their registry names"""
        print("Template Registry Information:")
        print("-" * 50)
        for template_id, template_class in self._templates.items():
            print(f"Registry Name: {template_id}")
            print(f"Class Name: {template_class.__name__}")
            if hasattr(template_class, "REGISTRY_NAME"):
                print(f"Template's REGISTRY_NAME: {template_class.REGISTRY_NAME}")
            print("-" * 30)

    def search_templates(
        self,
        category: Optional[str] = None,
        tags: Optional[List[str]] = None,
        requires_images: Optional[bool] = None,
    ) -> List[str]:
        """Search templates by criteria"""
        matching_templates = []

        for template_id in self.list_templates():
            metadata = self.get_template_metadata(template_id)

            # Filter by category
            if category and metadata.category != category:
                continue

            # Filter by tags
            if tags and not any(tag in metadata.tags for tag in tags):
                continue

            # Filter by image requirements
            if (
                requires_images is not None
                and metadata.requires_images != requires_images
            ):
                continue

            matching_templates.append(template_id)

        return matching_templates


# Global registry instance
template_registry = TemplateRegistry()
