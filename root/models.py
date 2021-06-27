# from django.db import models
# from ckeditor.fields import RichTextField
# # Create your models here.
#
# class Company(models.Model):
#
#     content_tr = RichTextField(verbose_name="İçerik TR")
#     content_en = RichTextField(verbose_name="İçerik EN")
#
#
#     class Meta:
#
#         verbose_name_plural = "Şirket"
#         ordering = ["-id"]
#
#
# class Call_Back(models.Model):
#
#     full_name = models.CharField(max_length=200,verbose_name="Ad Soyad")
#     company = models.CharField(max_length=200,verbose_name="Şirket")
#     phone  = models.CharField(max_length=200,verbose_name="Telefon")
#     confirm = models.BooleanField(verbose_name="Gizlilik Politikası Onayı")
#
#
#     def __str__(self):
#         return self.full_name
#
#     class Meta:
#
#         verbose_name_plural = "Geri Arama Talepleri"
#         ordering = ["-id"]
#
# class Privacy_Policy(models.Model):
#
#     content_tr = RichTextField(verbose_name="İçerik TR")
#     content_en = RichTextField(verbose_name="İçerik EN")
#
#
#     class Meta:
#
#         verbose_name_plural = "Gizlilik Politikası"
#         ordering = ["-id"]
