# from django.contrib.sitemaps import Sitemap
# from django.shortcuts import reverse
# from products.models import Automatic_Doors, Hospital_Doors, Security_Doors
#
#
# class StaticViewSitemap(Sitemap):
#     def items(self):
#         return ['automatic-doors', 'hospital-doors', 'security-doors']
#
#     def location(self, item):
#         return reverse(item)
#
#
# def location(self, item):
#     return reverse(item)
#
#
# class AutomaticDoorsSitemap(Sitemap):
#     def items(self):
#         return Automatic_Doors.objects.all()
#
#
# class HospitalDoorsSitemap(Sitemap):
#     def items(self):
#         return Hospital_Doors.objects.all()
#
#
# class SecurityDoorsSitemap(Sitemap):
#     def items(self):
#         return Security_Doors.objects.all()