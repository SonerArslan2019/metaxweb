# from django.db import models
# from ckeditor.fields import RichTextField
# from django.urls import reverse
# from django.utils.text import slugify
#
#
#
# class News(models.Model):
#
#     title_tr = models.CharField(verbose_name='Başlık - TR',max_length=100)
#     title_en = models.CharField(verbose_name='Başlık - EN',max_length=100)
#     content_tr = RichTextField(verbose_name='İçerik - TR')
#     content_en = RichTextField(verbose_name='İçerik - EN')
#     slug = models.SlugField(unique=True, editable=False, max_length=130)
#     image = models.ImageField(verbose_name='Resim')
#
#     date = models.DateField(auto_now_add=True)
#
#     def save(self, *args, **kwargs):
#         if True:
#
#             news_test = News.objects.all().order_by("id")
#             value = 0
#             for x in news_test:
#                 unique_slug = slugify(self.title_en)
#                 if value > 0:
#                     control_slug = str(unique_slug) + "-{0}".format(value)
#                 else:
#                     control_slug = unique_slug
#
#                 if x.slug == control_slug:
#                     value +=1
#
#             if news_test and value > 0:
#                 self.slug = str(unique_slug) + "-{0}".format(value)
#             else:
#                 self.slug = slugify(self.title_en)
#             super(News, self).save(*args, **kwargs)
#
#     def __str__(self):
#
#         return self.title_tr
#
#     class Meta:
#
#         ordering = ['-id']
#         verbose_name_plural = 'Haberler'