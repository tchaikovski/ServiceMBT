from django.contrib.sitemaps import Sitemap
from SinglePages.models import SinglePageModel
from service.models import ServiceModel


class SinglePageSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return SinglePageModel.objects.all()

    def lastmod(self, obj):
        return obj.updated


class ServiceModelSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return ServiceModel.objects.all()

    def lastmod(self, obj):
        return obj.updated
