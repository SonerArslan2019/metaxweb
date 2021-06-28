from django.contrib.sitemaps import Sitemap
from main.models import Item

class ProductSiteMap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9