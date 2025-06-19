from typing import List
from .base import BaseTemplate, TemplateVariable, TemplateMetadata


class WebServiceTemplate(BaseTemplate):
    """Professional website service template for web development projects, digital services, and online platforms"""
    
    REGISTRY_NAME = "website_service"
    
    def _get_metadata(self) -> TemplateMetadata:
        return TemplateMetadata(
            name="Website Service",
            description="Professional template for website development projects, digital services, web applications, and online platforms with comprehensive pricing and payment management",
            category="service",
            tags=["website", "service", "web", "digital", "platform", "pricing", "payment"],
            requires_images=True,
            requires_filtering=True,
        )
    
    def _get_page_config(self) -> dict:
        return {
            "page_title_cn": "网站服务",
            "page_title_en": "Website Service",
            "match_img": "yes",
            "filter_with": "yes",
        }
    
    def _get_basic_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("title", "Title", "标题", 1),
            TemplateVariable("service_type", "Service Type", "服务类型", 1),
            TemplateVariable("status", "Status", "状态", 1),  # active, development, maintenance, archived
            TemplateVariable("priority", "Priority", "优先级", 1),  # high, medium, low
        ]
    
    def _get_more_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("description", "Description", "描述", 5),
            TemplateVariable("overview", "Overview", "概述", 3),
            TemplateVariable("client", "Client", "客户", 1),
            TemplateVariable("client_contact", "Client Contact", "客户联系方式", 1),
            
            # Pricing and Payment Variables
            TemplateVariable("total_price", "Total Price", "总价格", 1),
            TemplateVariable("price_type", "Price Type", "定价类型", 1),  # fixed, hourly, milestone
            TemplateVariable("original_price", "Original Price", "原价", 1),
            TemplateVariable("discount_amount", "Discount Amount", "折扣金额", 1),
            TemplateVariable("discount_percentage", "Discount Percentage", "折扣百分比", 1),
            TemplateVariable("promotional_offer", "Promotional Offer", "促销优惠", 2),
            
            # Payment Status and Tracking
            TemplateVariable("payment_status", "Payment Status", "付款状态", 1),  # pending, partial, completed, overdue
            TemplateVariable("amount_paid", "Amount Paid", "已付金额", 1),
            TemplateVariable("amount_pending", "Amount Pending", "待付金额", 1),
            TemplateVariable("payment_due_date", "Payment Due Date", "付款截止日期", 1),
            TemplateVariable("payment_terms", "Payment Terms", "付款条款", 2),
            # Additional Costs
            TemplateVariable("additional_costs", "Additional Costs", "额外费用", 2),
            TemplateVariable("hosting_fee", "Hosting Fee", "托管费用", 1),
            TemplateVariable("domain_fee", "Domain Fee", "域名费用", 1),
            TemplateVariable("maintenance_fee", "Maintenance Fee", "维护费用", 1),
            TemplateVariable("support_fee", "Support Fee", "技术支持费用", 1),

            # Project Details
            TemplateVariable("start_date", "Start Date", "开始日期", 1),
            TemplateVariable("launch_date", "Launch Date", "上线日期", 1),
            TemplateVariable("completion_date", "Completion Date", "完成日期", 1),
            TemplateVariable("domain", "Domain", "域名", 1),
            TemplateVariable("hosting", "Hosting", "托管服务", 1),
            TemplateVariable("platform", "Platform", "平台", 1),  # WordPress, React, Vue, etc.
            TemplateVariable("technologies", "Technologies Used", "使用技术", 2),
            TemplateVariable("seo_optimization", "SEO Optimization", "SEO优化", 2),
            TemplateVariable("maintenance_plan", "Maintenance Plan", "维护计划", 2),
            TemplateVariable("support_level", "Support Level", "技术支持级别", 1),
            TemplateVariable("documentation", "Documentation", "文档", 2),
            TemplateVariable("tag", "Tag", "标签", 1),
            TemplateVariable("mark", "Mark", "标记", 1),
            TemplateVariable("notes", "Internal Notes", "内部备注", 3),
        ]
    
    def _get_image_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("cover_img_url", "Cover Image", "封面图片", 1),
            TemplateVariable("screenshot_desktop", "Desktop Screenshot", "桌面截图", 1),
            TemplateVariable("screenshot_mobile", "Mobile Screenshot", "移动端截图", 1)
        ]
    
    def _get_url_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("live_url", "Live URL", "网站链接", 1),
            TemplateVariable("database_url", "Datace URL", "数据库链接", 1),
            TemplateVariable("github_url", "GitHub URL", "代码仓库", 1),
            TemplateVariable("contractPDF_url", "Contract PDF URL", "PDF合同链接", 1),
            TemplateVariable("admin_url", "Admin URL", "后台管理", 1)
        ]
    
    def _get_array_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("update_log", "Update Log", "更新日志", 3),
            TemplateVariable("payment_history", "Payment History", "付款历史", 3)
        ]
    
    def _get_language_item_variables(self) -> List[TemplateVariable]:
        return [
            TemplateVariable("language", "Language", "语言", 1)
        ]