from typing import List
from .base import BaseTemplate, TemplateVariable, TemplateMetadata


class PublicationsTemplate(BaseTemplate):

    REGISTRY_NAME = "publication"

    def _get_metadata(self) -> TemplateMetadata:
        return TemplateMetadata(
            name="Publications",
            description="Template for articles, essays, publications, and written works with authorship, publication details, and content",
            category="publication",
            tags=["publication"],
            requires_images=True,
            requires_filtering=True,
        )

    def _get_page_config(self) -> dict:
        return {
            "page_title_cn": "文章",
            "page_title_en": "Publications",
            "match_img": "yes",
            "filter_with": "yes",
        }

    def _get_basic_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("title", "Title", "标题", 1),
            TemplateVariable("type", "Type", "类型", 1),
            TemplateVariable("author", "Author", "作者", 1),
            TemplateVariable("date", "Date", "日期", 1),
        ]

    def _get_more_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("keywords", "Keywords", "关键词", 1),
            TemplateVariable("summary", "Summary", "摘要", 4),
            TemplateVariable("book_title", "Book Title", "书名", 1),
            TemplateVariable("publisher", "Publisher", "出版商", 1),
            TemplateVariable("credit", "Credit", "致谢", 2),
            TemplateVariable("ISSN", "ISSN", "国际标准期刊号", 1),
            TemplateVariable("CN", "CN", "中国统一刊号", 1),
            TemplateVariable("issue_no", "Issue Number", "期号", 1),
            TemplateVariable("mark", "Mark", "标记", 1),
        ]

    def _get_image_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("cover_img_url", "Cover Image", "封面图片", 1),
        ]

    def _get_url_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("ref_url", "Reference URL", "参考链接", 1),
            TemplateVariable("pdf_url", "PDF URL", "PDF链接", 1),
            TemplateVariable("source_url", "Source URL", "源链接", 1),
        ]

    def _get_array_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("quotes", "Quotes", "引用", 3),
            TemplateVariable("paragraphs", "Paragraphs", "内容段落", 5),
            TemplateVariable("tag", "Tag", "标签", 1),
        ]

    def _get_language_item_variables(self) -> List[TemplateVariable]:
        return [TemplateVariable("language", "Language", "语言", 1)]
