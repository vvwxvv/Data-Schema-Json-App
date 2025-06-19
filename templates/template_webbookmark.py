from typing import List
from .base import BaseTemplate, TemplateVariable, TemplateMetadata


class WebBookmarkTemplate(BaseTemplate):
    """Website bookmark template for collecting and organizing web resources"""
    
    REGISTRY_NAME = "website_bookmark"
    
    def _get_metadata(self) -> TemplateMetadata:
        return TemplateMetadata(
            name="Website Bookmark",
            description="Template for organizing and cataloging website bookmarks with categories, descriptions, and metadata",
            category="reference",
            tags=["bookmark", "website", "collection", "resource"],
            requires_images=True,
            requires_filtering=True,
        )
    
    def _get_page_config(self) -> dict:
        return {
            "page_title_cn": "网站收藏",
            "page_title_en": "Website Bookmark",
            "match_img": "yes",
            "filter_with": "yes",
        }
    
    def _get_basic_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("title", "Title", "标题", 1),
            TemplateVariable("url", "URL", "网址", 1),
            TemplateVariable("category", "Category", "分类", 1),
            TemplateVariable("description", "Description", "描述", 2),
        ]
    
    def _get_more_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("keywords", "Keywords", "关键词", 1),
            TemplateVariable("mark", "Mark", "记号", 1),
            TemplateVariable("order", "Order", "排序", 1),
        ]
    
    def _get_image_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("screenshot_url", "Screenshot", "截图", 1),
        ]
    
    def _get_url_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("website_url", "URL", "URL链接", 1),
        ]
    
    def _get_array_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("tags", "Tags", "标签", 1),
            TemplateVariable("highlights", "Highlights", "重点内容", 3),
        ]
    
    def _get_language_item_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("language", "Language", "语言", 1)
        ]