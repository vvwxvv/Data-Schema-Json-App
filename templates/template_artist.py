from typing import List
from .base import BaseTemplate, TemplateVariable, TemplateMetadata


class ArtistWebsiteTemplate(BaseTemplate):
    """Artist website template"""

    REGISTRY_NAME = "artist"

    def _get_metadata(self) -> TemplateMetadata:
        return TemplateMetadata(
            name="Artist",
            description="Comprehensive template for artist portfolios with About, Events, Artworks, Writings, and Media sections",
            category="art",
            tags=["artist"],
            requires_images=True,
            requires_filtering=True,
        )

    def _get_page_config(self) -> dict:
        return {
            "page_title_cn": "艺术家",
            "page_title_en": "Artist",
            "match_img": "yes",
            "filter_with": "yes",
        }

    def _get_basic_variables(self) -> List[TemplateVariable]:
        return [TemplateVariable("name", "Name", "姓名", 1)]

    def _get_more_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("short_bio", "Short Biography", "简短介绍", 3),
            TemplateVariable("statement", "Artist Statement", "艺术家陈述", 5),
            TemplateVariable("accomplishments", "Accomplishments", "成就", 4),
            TemplateVariable("awards", "Awards", "奖项", 3),
            TemplateVariable("email", "Email", "电子邮件", 1),
            TemplateVariable("website", "Website", "网站", 1),
            TemplateVariable("social_media", "Social Media", "社交媒体", 2),
        ]

    def _get_image_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("cover_img_url", "Cover Image", "封面图片", 1),
            TemplateVariable("profile_img_url", "Profile Image", "肖像照", 1),
        ]

    def _get_url_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("pdf_url", "PDF URL", "PDF链接", 1),
            TemplateVariable("url_video", "Video URL", "视频链接", 1),
        ]

    def _get_array_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("quotes", "Quotes", "引用", 4),
            TemplateVariable("recent_activities", "Recent Activities", "近期活动", 4),
            TemplateVariable("press_release_url", "Press Release URL", "新闻稿链接", 1),
            TemplateVariable("tag", "Tags", "标签", 3),
        ]

    def _get_language_item_variables(self) -> List[TemplateVariable]:
        return [TemplateVariable("language", "Language", "语言", 1)]
