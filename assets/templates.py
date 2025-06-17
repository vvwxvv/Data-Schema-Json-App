from typing import Dict, List, Any
from .models import Schema, Variable


class SchemaTemplate:
    """Schema template definition"""

    def __init__(self, name: str, description: str, preview_data: Dict[str, Any]):
        self.name = name
        self.description = description
        self.preview_data = preview_data

    def to_schema(self, schema_name: str) -> Schema:
        """Convert template to actual schema"""
        schema = Schema(name=schema_name)

        # Copy basic info
        schema.page_title_cn = self.preview_data.get("page_title_cn", "")
        schema.page_title_en = self.preview_data.get("page_title_en", "")
        schema.match_img = self.preview_data.get("match_img", "no")
        schema.filter_with = self.preview_data.get("filter_with", "no")

        # Copy variables
        for var_type in [
            "basic_variables",
            "more_variables",
            "image_variables",
            "url_variables",
            "array_variables",
            "language_item_variables",
        ]:
            var_list = self.preview_data.get(var_type, [])
            schema_vars = []
            for var_dict in var_list:
                for var_name, var_data in var_dict.items():
                    var = Variable(
                        name=var_name,
                        en_text=var_data.get("en", ""),
                        cn_text=var_data.get("cn", ""),
                        rows=var_data.get("rows", 0),
                    )
                    schema_vars.append(var)
            setattr(schema, var_type, schema_vars)

        return schema


class TemplateManager:
    """Manages schema templates"""

    def __init__(self):
        self.templates = self._load_default_templates()

    def _load_default_templates(self) -> Dict[str, SchemaTemplate]:
        """Load default templates"""
        templates = {}

        # E-commerce Product Template
        templates["ecommerce_product"] = SchemaTemplate(
            name="E-commerce Product",
            description="Template for product listings with images, prices, and descriptions",
            preview_data={
                "page_title_cn": "产品详情",
                "page_title_en": "Product Details",
                "match_img": "yes",
                "filter_with": "yes",
                "basic_variables": [
                    {
                        "product_name": {
                            "en": "Product Name",
                            "cn": "产品名称",
                            "rows": 1,
                        }
                    },
                    {"price": {"en": "Price", "cn": "价格", "rows": 1}},
                    {"sku": {"en": "SKU", "cn": "库存单位", "rows": 1}},
                    {"stock": {"en": "Stock", "cn": "库存", "rows": 1}},
                ],
                "more_variables": [
                    {"description": {"en": "Description", "cn": "描述", "rows": 5}},
                    {
                        "specifications": {
                            "en": "Specifications",
                            "cn": "规格",
                            "rows": 3,
                        }
                    },
                ],
                "image_variables": [
                    {"main_image": {"en": "Main Image", "cn": "主图", "rows": 1}},
                    {"gallery": {"en": "Image Gallery", "cn": "图片库", "rows": 4}},
                ],
                "url_variables": [
                    {"product_url": {"en": "Product URL", "cn": "产品链接", "rows": 1}}
                ],
                "array_variables": [
                    {"categories": {"en": "Categories", "cn": "分类", "rows": 3}},
                    {"tags": {"en": "Tags", "cn": "标签", "rows": 5}},
                ],
                "language_item_variables": [],
            },
        )

        # Blog Post Template
        templates["blog_post"] = SchemaTemplate(
            name="Blog Post",
            description="Template for blog articles with author, content, and metadata",
            preview_data={
                "page_title_cn": "博客文章",
                "page_title_en": "Blog Post",
                "match_img": "yes",
                "filter_with": "no",
                "basic_variables": [
                    {"title": {"en": "Title", "cn": "标题", "rows": 1}},
                    {"author": {"en": "Author", "cn": "作者", "rows": 1}},
                    {
                        "publish_date": {
                            "en": "Publish Date",
                            "cn": "发布日期",
                            "rows": 1,
                        }
                    },
                ],
                "more_variables": [
                    {"content": {"en": "Content", "cn": "内容", "rows": 10}},
                    {"excerpt": {"en": "Excerpt", "cn": "摘要", "rows": 3}},
                ],
                "image_variables": [
                    {
                        "featured_image": {
                            "en": "Featured Image",
                            "cn": "特色图片",
                            "rows": 1,
                        }
                    }
                ],
                "url_variables": [
                    {"permalink": {"en": "Permalink", "cn": "永久链接", "rows": 1}},
                    {"author_url": {"en": "Author URL", "cn": "作者链接", "rows": 1}},
                ],
                "array_variables": [
                    {"categories": {"en": "Categories", "cn": "分类", "rows": 3}},
                    {"tags": {"en": "Tags", "cn": "标签", "rows": 5}},
                ],
                "language_item_variables": [
                    {"translations": {"en": "Translations", "cn": "翻译", "rows": 5}}
                ],
            },
        )

        # User Profile Template
        templates["user_profile"] = SchemaTemplate(
            name="User Profile",
            description="Template for user profiles with personal information and settings",
            preview_data={
                "page_title_cn": "用户资料",
                "page_title_en": "User Profile",
                "match_img": "no",
                "filter_with": "no",
                "basic_variables": [
                    {"username": {"en": "Username", "cn": "用户名", "rows": 1}},
                    {"email": {"en": "Email", "cn": "电子邮件", "rows": 1}},
                    {"first_name": {"en": "First Name", "cn": "名字", "rows": 1}},
                    {"last_name": {"en": "Last Name", "cn": "姓氏", "rows": 1}},
                ],
                "more_variables": [
                    {"bio": {"en": "Biography", "cn": "简介", "rows": 5}},
                    {"preferences": {"en": "Preferences", "cn": "偏好设置", "rows": 3}},
                ],
                "image_variables": [
                    {"avatar": {"en": "Avatar", "cn": "头像", "rows": 1}}
                ],
                "url_variables": [
                    {
                        "profile_url": {
                            "en": "Profile URL",
                            "cn": "个人资料链接",
                            "rows": 1,
                        }
                    },
                    {"website": {"en": "Website", "cn": "网站", "rows": 1}},
                ],
                "array_variables": [
                    {"skills": {"en": "Skills", "cn": "技能", "rows": 10}},
                    {"interests": {"en": "Interests", "cn": "兴趣", "rows": 5}},
                ],
                "language_item_variables": [],
            },
        )

        # Event Template
        templates["event"] = SchemaTemplate(
            name="Event",
            description="Template for events with dates, locations, and attendee information",
            preview_data={
                "page_title_cn": "活动详情",
                "page_title_en": "Event Details",
                "match_img": "yes",
                "filter_with": "yes",
                "basic_variables": [
                    {"event_name": {"en": "Event Name", "cn": "活动名称", "rows": 1}},
                    {"start_date": {"en": "Start Date", "cn": "开始日期", "rows": 1}},
                    {"end_date": {"en": "End Date", "cn": "结束日期", "rows": 1}},
                    {"location": {"en": "Location", "cn": "地点", "rows": 1}},
                ],
                "more_variables": [
                    {"description": {"en": "Description", "cn": "描述", "rows": 5}},
                    {"agenda": {"en": "Agenda", "cn": "议程", "rows": 5}},
                ],
                "image_variables": [
                    {"banner": {"en": "Event Banner", "cn": "活动横幅", "rows": 1}},
                    {
                        "venue_images": {
                            "en": "Venue Images",
                            "cn": "场地图片",
                            "rows": 3,
                        }
                    },
                ],
                "url_variables": [
                    {
                        "registration_url": {
                            "en": "Registration URL",
                            "cn": "注册链接",
                            "rows": 1,
                        }
                    },
                    {
                        "event_website": {
                            "en": "Event Website",
                            "cn": "活动网站",
                            "rows": 1,
                        }
                    },
                ],
                "array_variables": [
                    {"speakers": {"en": "Speakers", "cn": "演讲者", "rows": 5}},
                    {"sponsors": {"en": "Sponsors", "cn": "赞助商", "rows": 3}},
                ],
                "language_item_variables": [],
            },
        )

        # API Documentation Template
        templates["api_docs"] = SchemaTemplate(
            name="API Documentation",
            description="Template for API endpoint documentation",
            preview_data={
                "page_title_cn": "API 文档",
                "page_title_en": "API Documentation",
                "match_img": "no",
                "filter_with": "no",
                "basic_variables": [
                    {"endpoint": {"en": "Endpoint", "cn": "端点", "rows": 1}},
                    {"method": {"en": "HTTP Method", "cn": "HTTP 方法", "rows": 1}},
                    {"version": {"en": "Version", "cn": "版本", "rows": 1}},
                ],
                "more_variables": [
                    {"description": {"en": "Description", "cn": "描述", "rows": 3}},
                    {"request_body": {"en": "Request Body", "cn": "请求体", "rows": 5}},
                    {"response": {"en": "Response", "cn": "响应", "rows": 5}},
                ],
                "image_variables": [],
                "url_variables": [
                    {"base_url": {"en": "Base URL", "cn": "基础 URL", "rows": 1}}
                ],
                "array_variables": [
                    {"parameters": {"en": "Parameters", "cn": "参数", "rows": 10}},
                    {"headers": {"en": "Headers", "cn": "请求头", "rows": 5}},
                    {"errors": {"en": "Error Codes", "cn": "错误代码", "rows": 5}},
                ],
                "language_item_variables": [],
            },
        )

        # Simple Form Template
        templates["simple_form"] = SchemaTemplate(
            name="Simple Form",
            description="Basic form template with common fields",
            preview_data={
                "page_title_cn": "表单",
                "page_title_en": "Form",
                "match_img": "no",
                "filter_with": "no",
                "basic_variables": [
                    {"form_title": {"en": "Form Title", "cn": "表单标题", "rows": 1}},
                    {
                        "submit_button": {
                            "en": "Submit Button",
                            "cn": "提交按钮",
                            "rows": 1,
                        }
                    },
                ],
                "more_variables": [
                    {"instructions": {"en": "Instructions", "cn": "说明", "rows": 3}}
                ],
                "image_variables": [],
                "url_variables": [
                    {"action_url": {"en": "Action URL", "cn": "提交地址", "rows": 1}}
                ],
                "array_variables": [
                    {"fields": {"en": "Form Fields", "cn": "表单字段", "rows": 10}}
                ],
                "language_item_variables": [],
            },
        )

        # Gallery Website Template
        templates["gallery_website"] = SchemaTemplate(
            name="Gallery Website",
            description="Template for gallery websites with image collections and product showcases",
            preview_data={
                "page_title_cn": "产品详情",
                "page_title_en": "Product Details",
                "match_img": "yes",
                "filter_with": "yes",
                "basic_variables": [
                    {
                        "product_name": {
                            "en": "Product Name",
                            "cn": "产品名称",
                            "rows": 1,
                        }
                    },
                    {"price": {"en": "Price", "cn": "价格", "rows": 1}},
                    {"sku": {"en": "SKU", "cn": "库存单位", "rows": 1}},
                    {"stock": {"en": "Stock", "cn": "库存", "rows": 1}},
                ],
                "more_variables": [
                    {"description": {"en": "Description", "cn": "描述", "rows": 5}},
                    {
                        "specifications": {
                            "en": "Specifications",
                            "cn": "规格",
                            "rows": 3,
                        }
                    },
                ],
                "image_variables": [
                    {"main_image": {"en": "Main Image", "cn": "主图", "rows": 1}},
                    {"gallery": {"en": "Image Gallery", "cn": "图片库", "rows": 4}},
                ],
                "url_variables": [
                    {"product_url": {"en": "Product URL", "cn": "产品链接", "rows": 1}}
                ],
                "array_variables": [
                    {"categories": {"en": "Categories", "cn": "分类", "rows": 3}},
                    {"tags": {"en": "Tags", "cn": "标签", "rows": 5}},
                ],
                "language_item_variables": [],
            },
        )

        # Artist Website Template
        templates["artist_website"] = SchemaTemplate(
            name="Artist Website",
            description="Comprehensive template for artist portfolios with About, Events, Artworks, Writings, and Media sections",
            preview_data={
                "page_title_cn": "艺术家作品集",
                "page_title_en": "Artist Portfolio",
                "match_img": "yes",
                "filter_with": "yes",
                "basic_variables": [
                    {
                        "artist_name": {
                            "en": "Artist Name",
                            "cn": "艺术家姓名",
                            "rows": 1,
                        }
                    },
                    {"language": {"en": "Language", "cn": "语言", "rows": 1}},
                    {
                        "cover_img_url": {
                            "en": "Cover Image URL",
                            "cn": "封面图片链接",
                            "rows": 1,
                        }
                    },
                ],
                "more_variables": [
                    {
                        "short_bio": {
                            "en": "Short Biography",
                            "cn": "简短传记",
                            "rows": 3,
                        }
                    },
                    {
                        "statement": {
                            "en": "Artist Statement",
                            "cn": "艺术家声明",
                            "rows": 5,
                        }
                    },
                    {
                        "accomplishments": {
                            "en": "Accomplishments",
                            "cn": "成就",
                            "rows": 4,
                        }
                    },
                    {
                        "recent_activities": {
                            "en": "Recent Activities",
                            "cn": "近期活动",
                            "rows": 4,
                        }
                    },
                    {"awards": {"en": "Awards", "cn": "奖项", "rows": 3}},
                    {"email": {"en": "Email", "cn": "电子邮件", "rows": 1}},
                    {
                        "social_media": {
                            "en": "Social Media",
                            "cn": "社交媒体",
                            "rows": 2,
                        }
                    },
                ],
                "image_variables": [
                    {
                        "cover_img_url": {
                            "en": "Cover Image",
                            "cn": "封面图片",
                            "rows": 1,
                        }
                    },
                    {
                        "gallery_images": {
                            "en": "Gallery Images",
                            "cn": "画廊图片",
                            "rows": 5,
                        }
                    },
                ],
                "url_variables": [
                    {"pdf_url": {"en": "PDF URL", "cn": "PDF链接", "rows": 1}},
                    {
                        "press_release_url": {
                            "en": "Press Release URL",
                            "cn": "新闻稿链接",
                            "rows": 1,
                        }
                    },
                    {
                        "info_url": {
                            "en": "Information URL",
                            "cn": "信息链接",
                            "rows": 1,
                        }
                    },
                    {"ref_url": {"en": "Reference URL", "cn": "参考链接", "rows": 1}},
                    {"source_url": {"en": "Source URL", "cn": "来源链接", "rows": 1}},
                    {"url_video": {"en": "Video URL", "cn": "视频链接", "rows": 1}},
                    {
                        "url_flipbook": {
                            "en": "Flipbook URL",
                            "cn": "翻书链接",
                            "rows": 1,
                        }
                    },
                    {"url_other": {"en": "Other URL", "cn": "其他链接", "rows": 1}},
                ],
                "array_variables": [
                    {
                        "press_release_paragraphs": {
                            "en": "Press Release Paragraphs",
                            "cn": "新闻稿段落",
                            "rows": 5,
                        }
                    },
                    {"paragraphs": {"en": "Paragraphs", "cn": "段落", "rows": 5}},
                    {"descriptions": {"en": "Descriptions", "cn": "描述", "rows": 5}},
                    {"quotes": {"en": "Quotes", "cn": "引用", "rows": 4}},
                    {"reflections": {"en": "Reflections", "cn": "反思", "rows": 4}},
                    {"media_urls": {"en": "Media URLs", "cn": "媒体链接", "rows": 5}},
                    {"tag": {"en": "Tags", "cn": "标签", "rows": 3}},
                    {"mark": {"en": "Marks", "cn": "标记", "rows": 2}},
                ],
                "language_item_variables": [
                    {
                        "media_tag_en": {
                            "en": "Media Tag (EN)",
                            "cn": "媒体标签 (英文)",
                            "rows": 1,
                        }
                    },
                    {
                        "media_tag_cn": {
                            "en": "Media Tag (CN)",
                            "cn": "媒体标签 (中文)",
                            "rows": 1,
                        }
                    },
                    {
                        "credit_en": {
                            "en": "Credit (EN)",
                            "cn": "致谢 (英文)",
                            "rows": 1,
                        }
                    },
                    {
                        "credit_cn": {
                            "en": "Credit (CN)",
                            "cn": "致谢 (中文)",
                            "rows": 1,
                        }
                    },
                    {
                        "caption_en": {
                            "en": "Caption (EN)",
                            "cn": "说明 (英文)",
                            "rows": 1,
                        }
                    },
                    {
                        "caption_cn": {
                            "en": "Caption (CN)",
                            "cn": "说明 (中文)",
                            "rows": 1,
                        }
                    },
                ],
            },
        )

        return templates

    def get_template(self, template_id: str) -> SchemaTemplate:
        """Get a specific template"""
        return self.templates.get(template_id)

    def get_all_templates(self) -> Dict[str, SchemaTemplate]:
        """Get all available templates"""
        return self.templates

    def add_custom_template(self, template_id: str, template: SchemaTemplate):
        """Add a custom template"""
        self.templates[template_id] = template
