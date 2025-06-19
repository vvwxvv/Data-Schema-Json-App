from typing import List
from .base import BaseTemplate, TemplateVariable, TemplateMetadata


class ArtworkTemplate(BaseTemplate):
    """Artwork template for art pieces, installations, and creative works"""

    REGISTRY_NAME = "artwork"

    def _get_metadata(self) -> TemplateMetadata:
        return TemplateMetadata(
            name="Artwork",
            description="Template for artworks, installations, and creative pieces with details, medium, and documentation",
            category="art",
            tags=["artwork"],
            requires_images=True,
            requires_filtering=True,
        )

    def _get_page_config(self) -> dict:
        return {
            "page_title_cn": "作品",
            "page_title_en": "Artwork",
            "match_img": "yes",
            "filter_with": "yes",
        }

    def _get_basic_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("title", "Title", "标题", 1),
            TemplateVariable("type", "Type", "类型", 1),
            TemplateVariable("medium", "Medium", "媒介", 1),
            TemplateVariable("year", "Year", "年份", 1),
            TemplateVariable("size", "Size", "尺寸", 1),
            TemplateVariable("series", "Series", "系列", 1),
            TemplateVariable("caption", "Caption", "说明", 2),
        ]

    def _get_more_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("duration", "Duration", "时长", 1),
            TemplateVariable("introduction", "Introduction", "介绍", 4),
            TemplateVariable("work_value", "Work Value", "价格", 1),
            TemplateVariable("version", "version", "版数", 1),
            TemplateVariable("tag", "Tag", "标签", 1),
            TemplateVariable("mark", "Mark", "标记", 1),
            TemplateVariable("order", "Order", "排序", 1),
        ]

    def _get_image_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("cover_img_url", "Cover Image", "封面图片", 1),
        ]

    def _get_url_variables(self) -> List[TemplateVariable]:
        return [TemplateVariable("url_video", "Video URL", "视频链接", 1)]

    def _get_array_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("descriptions", "Descriptions", "描述", 5),
            TemplateVariable("tag", "Tag", "标签", 1),
            ]

    def _get_language_item_variables(self) -> List[TemplateVariable]:
        return [TemplateVariable("language", "Language", "语言", 1)]
