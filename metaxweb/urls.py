from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic.base import TemplateView
from products.sitemaps import StaticViewSitemap, AutomaticDoorsSitemap, HospitalDoorsSitemap, SecurityDoorsSitemap
from django.conf.urls.i18n import i18n_patterns
from root.views import *

sitemaps = {
    'static': StaticViewSitemap, 'automatic-doors': AutomaticDoorsSitemap, 'hospital-doors': HospitalDoorsSitemap,
    'security-doors': SecurityDoorsSitemap,
}

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('company/', company_view, name="company"),
    path('pdf/<file>/', pdf_view, name="pdf"),
    path('contact/', contact_view, name="contact"),
    path('privacy-policy/', privacy_view, name="privacy"),

    path('news/', include('news.urls')),
    path('products/', include('products.urls')),
    path('gallery/', include('gallery.urls')),

    # language
    path('i18n/', include('django.conf.urls.i18n')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), ),

    prefix_default_language=False
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

