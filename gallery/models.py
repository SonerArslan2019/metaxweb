from django.db import models
from django.contrib import messages
from datetime import datetime

product = (
    ("Otomatik Kapılar", "Otomatik Kapılar"),
    ("Hastane Kapıları", "Hastane Kapıları"),
    ("Security Kapıları", "Security Kapıları"),
)


class Gallery(models.Model):
    title_de = models.CharField(max_length=80, verbose_name="Resim Başlığı - DE")
    title_en = models.CharField(max_length=80, verbose_name="Resim Başlığı - EN")

    image = models.ImageField(verbose_name='Resim', blank=True)
    video = models.CharField(verbose_name='Video Url(YouTube)', max_length=300, blank=True)
    product_category = models.CharField(choices=product, default="Otomatik Kapılar", blank=False, null=False,
                                        max_length=500, verbose_name="Ürün Kategorisi")

    def __str__(self):
        return self.product_category

    def save(self, *args, **kwargs):
        if self.image and self.video:
            self.image = None

        super(Gallery, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Galeri'
        ordering = ['-id']


class Popup(models.Model):
    title = models.CharField(verbose_name="Başlık", max_length=150)
    content = models.TextField(verbose_name="Kısa Mesaj")
    image = models.ImageField(verbose_name="Popup Resimi")
    upgrade_date = models.DateTimeField(verbose_name='Güncellenme Tarihi', editable=False)
    finish_date = models.DateTimeField(verbose_name="Bitiş Tarihi")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-upgrade_date']
        verbose_name_plural = 'Popups'

    def save(self, *args, **kwargs):
        self.upgrade_date = datetime.now()
        super(Popup, self).save(*args, **kwargs)


