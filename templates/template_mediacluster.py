from typing import List
from .base import BaseTemplate, TemplateVariable, TemplateMetadata


class MediaclusterTemplate(BaseTemplate):
    """Media cluster template for grouped media collections with multilingual support"""

    REGISTRY_NAME = "mediacluster"

    def _get_metadata(self) -> TemplateMetadata:
        return TemplateMetadata(
            name="Mediacluster",
            description="Template for media clusters and collections with multilingual tags, captions, and credits",
            category="mediacluster",
            tags=[
                "mediacluster",
            ],
            requires_images=True,
            requires_filtering=True,
        )

    def _get_page_config(self) -> dict:
        return {
            "page_title_cn": "媒体集合",
            "page_title_en": "Media Cluster",
            "match_img": "yes",
            "filter_with": "yes",
        }

    def _get_basic_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("media_tag_en", "Media Tag (EN)", "媒体标签(英文)", 1),
            TemplateVariable("media_tag_cn", "Media Tag (CN)", "媒体标签(中文)", 1),
            TemplateVariable("category", "Category", "分类", 1),
        ]

    def _get_more_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("caption_en", "Caption (EN)", "说明(英文)", 3),
            TemplateVariable("caption_cn", "Caption (CN)", "说明(中文)", 3),
            TemplateVariable("mark", "Mark", "标记", 1),
        ]

    def _get_image_variables(self) -> List[TemplateVariable]:
        return []

    def _get_url_variables(self) -> List[TemplateVariable]:
        return []

    def _get_array_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("media_urls", "Media URLs", "媒体链接", 5),
            TemplateVariable("tag", "Tag", "标签", 1),
        ]

    def _get_language_item_variables(self) -> List[TemplateVariable]:
        return []
