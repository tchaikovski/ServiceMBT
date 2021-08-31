from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static
# from sitemenu.views import *
from ServiceMBT.sitemaps import ServiceModelSitemap, SinglePageSitemap
from django.views.defaults import server_error, page_not_found, permission_denied

sitemaps = {
    'service': ServiceModelSitemap,
    # 'post': SinglePageSitemap,
            }
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('blog/', include('blog.urls', namespace='blog')),
                  path('service/', include('service.urls', namespace='uslugi')),
                  path('', TemplateView.as_view(template_name='base.html'), name='index'),
                  path('', include('SinglePages.urls')),
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
                  # path('captcha/', include('captcha.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "sitemenu.views.page_not_found_view"
handler403 = "sitemenu.views.page403_not_found_view"
# handler500 = "sitemenu.views.page500_not_found_view"
