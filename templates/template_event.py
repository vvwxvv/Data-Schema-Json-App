from typing import List
from .base import BaseTemplate, TemplateVariable, TemplateMetadata


class EventTemplate(BaseTemplate):
    """Event template for exhibitions, shows, and cultural events"""

    REGISTRY_NAME = "event"

    def _get_metadata(self) -> TemplateMetadata:
        return TemplateMetadata(
            name="Event",
            description="Template for exhibitions, shows, performances, and cultural events with details, participants, and documentation",
            category="event",
            tags=["event"],
            requires_images=True,
            requires_filtering=True,
        )

    def _get_page_config(self) -> dict:
        return {
            "page_title_cn": "事件",
            "page_title_en": "Event",
            "match_img": "yes",
            "filter_with": "yes",
        }

    def _get_basic_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("title", "Title", "标题", 1),
            TemplateVariable("type", "Type", "类型", 1),
            TemplateVariable("year", "Year", "年份", 1),
        ]

    def _get_more_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("description", "Description", "描述", 5),
            TemplateVariable("introduction", "Introduction", "介绍", 4),
            TemplateVariable("role", "Role", "角色", 1),
            TemplateVariable("start_date", "Start Date", "开始日期", 1),
            TemplateVariable("end_date", "End Date", "结束日期", 1),
            TemplateVariable("opening_date", "Opening Date", "开幕日期", 1),
            TemplateVariable("venue", "Venue", "场地", 1),
            TemplateVariable("location", "Location", "地点", 1),
            TemplateVariable("city", "City", "城市", 1),
            TemplateVariable("country", "Country", "国家", 1),
            TemplateVariable("curator", "Curator", "策展人", 1),
            TemplateVariable("organizer", "Organizer", "组织者", 1),
            TemplateVariable("participants", "Participants", "参与者", 2),
            TemplateVariable("sponsors", "Sponsors", "赞助商", 2),
            TemplateVariable("credit", "Credit", "致谢", 2),
            TemplateVariable("tag", "Tag", "标签", 1),
            TemplateVariable("mark", "Mark", "标记", 1),
        ]

    def _get_image_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("cover_img_url", "Cover Image", "封面图片", 1),
        ]

    def _get_url_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("press_release_url", "Press Release URL", "新闻稿链接", 1),
            TemplateVariable("info_url", "Info URL", "信息链接", 1),
            TemplateVariable("pdf_url", "PDF URL", "PDF链接", 1),
        ]

    def _get_array_variables(self) -> List[TemplateVariable]:
        return [TemplateVariable("paragraphs", "Paragraphs", "内容段落", 5)]

    def _get_language_item_variables(self) -> List[TemplateVariable]:
        return [TemplateVariable("language", "Language", "语言", 1)]
