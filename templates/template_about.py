from typing import List
from .base import BaseTemplate, TemplateVariable, TemplateMetadata


class AboutTemplate(BaseTemplate):
    """About template for personal/professional profiles"""

    # Add registry name as class attribute
    REGISTRY_NAME = "about_page"

    def _get_metadata(self) -> TemplateMetadata:
        return TemplateMetadata(
            name="About",
            description="Template for personal and professional about pages with biography, statement, accomplishments, and contact information",
            category="profile",
            tags=["about", "profile", "personal", "professional"],
            requires_images=True,
            requires_filtering=False,
        )

    def _get_page_config(self) -> dict:
        return {
            "page_title_cn": "关于",
            "page_title_en": "About",
            "match_img": "yes",
            "filter_with": "no",
        }

    def _get_basic_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("language", "Language", "语言", 1),
            TemplateVariable("cover_img_url", "Cover Image URL", "封面图片链接", 1),
        ]

    def _get_more_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("short_bio", "Short Biography", "简短传记", 3),
            TemplateVariable("statement", "Statement", "声明", 5),
            TemplateVariable("accomplishments", "Accomplishments", "成就", 4),
            TemplateVariable("recent_activities", "Recent Activities", "近期活动", 4),
            TemplateVariable("awards", "Awards", "奖项", 3),
            TemplateVariable("email", "Email", "电子邮件", 1),
            TemplateVariable("social_media", "Social Media", "社交媒体", 2),
        ]

    def _get_image_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("cover_img_url", "Cover Image", "封面图片", 1),
        ]

    def _get_url_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("pdf_url", "PDF URL", "PDF链接", 1),
        ]

    def _get_array_variables(self) -> List[TemplateVariable]:
        return []

    def _get_language_item_variables(self) -> List[TemplateVariable]:
        return []
