from typing import List
from .base import BaseTemplate, TemplateVariable, TemplateMetadata


class InquiryTemplate(BaseTemplate):
    """Inquiry template for customer inquiries, support requests, and general questions"""
    
    REGISTRY_NAME = "inquiry"
    
    def _get_metadata(self) -> TemplateMetadata:
        return TemplateMetadata(
            name="Inquiry",
            description="Template for customer inquiries, support requests, and general questions with contact details and status tracking",
            category="communication",
            tags=["inquiry", "support", "contact"],
            requires_images=False,
            requires_filtering=True,
        )
    
    def _get_page_config(self) -> dict:
        return {
            "page_title_cn": "咨询",
            "page_title_en": "Inquiry",
            "match_img": "no",
            "filter_with": "yes",
        }
    
    def _get_basic_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("type", "Type", "类型", 1),
            TemplateVariable("name", "Name", "姓名", 1),
            TemplateVariable("email", "Email", "邮箱", 1),
            TemplateVariable("subject", "Subject", "主题", 1),
            TemplateVariable("messages", "Messages", "消息", 5),
        ]
    
    def _get_more_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("status", "Status", "状态", 1),
            TemplateVariable("tags", "Tags", "标签", 1),
        ]
    
    def _get_image_variables(self) -> List[TemplateVariable]:
        return []
    
    def _get_url_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("url_reference", "Reference URL", "参考链接", 1),
            TemplateVariable("url_documentation", "Documentation URL", "文档链接", 1),
        ]
    
    def _get_array_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("reply", "reply", "回复", 4),
        ]
    
    def _get_language_item_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("language", "Language", "语言", 1)
        ]