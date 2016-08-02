from django.utils.translation import ugettext_lazy as _
from shuup.admin.base import Section
from shuup.campaigns.models import BasketCampaign, CatalogCampaign


class ProductCampaignsSection(Section):
    identifier = "product_campaigns"
    name = _("Active Campaigns")
    icon = "fa-bullhorn"
    template = "shuup/campaigns/admin/_product_campaigns.jinja"

    @staticmethod
    def visible_for_object(product):
        return bool(product.pk)

    @staticmethod
    def get_context_data(product):
        return {
            "basket_campaigns": BasketCampaign.get_for_product(product)[:100],
            "catalog_campaigns": CatalogCampaign.get_for_product(product)[:100]
        }
