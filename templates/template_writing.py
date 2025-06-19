from typing import List
from .base import BaseTemplate, TemplateVariable, TemplateMetadata


class WritingTemplate(BaseTemplate):
    """Writing template for personal diary, dream journal, notes, and creative writing"""
    
    REGISTRY_NAME = "writing"
    
    def _get_metadata(self) -> TemplateMetadata:
        return TemplateMetadata(
            name="Writing",
            description="Template for personal writing including diary entries, dream journals, notes, reflections, and creative writing",
            category="writing",
            tags=["writing", "personal", "diary", "journal", "notes"],
            requires_images=False,
            requires_filtering=False,
        )
    
    def _get_page_config(self) -> dict:
        return {
            "page_title_cn": "写作",
            "page_title_en": "Writing",
            "match_img": "no",
            "filter_with": "no",
        }
    
    def _get_basic_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("title", "Title", "标题", 1),
            TemplateVariable("type", "Type", "类型", 1),  # diary, dream, note, reflection, creative
            TemplateVariable("date", "Date", "日期", 1),
        ]
    
    def _get_more_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("caption", "Caption", "简介", 10),
            TemplateVariable("keywords", "Keywords", "关键词", 1),
            TemplateVariable("quotes", "Quotes", "引用", 2),
            TemplateVariable("reflection", "Reflection", "反思", 3),
            TemplateVariable("mark", "Mark", "标记", 1),
        ]
    
    def _get_image_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("attached_img_url", "Attached Image", "附图", 1),
        ]
    
    def _get_url_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("related_url", "Related URL", "相关链接", 1),
        ]
    
    def _get_array_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("paragraphs", "Paragraphs", "内容段落", 5),
            TemplateVariable("bullet_points", "Bullet Points", "要点", 3),
            TemplateVariable("tag", "Tag", "标签", 1),
        ]
    
    def _get_language_item_variables(self) -> List[TemplateVariable]:
        return [TemplateVariable("language", "Language", "语言", 1)]