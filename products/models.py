from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class Automatic_Doors(models.Model):

    title_de = models.CharField(max_length=150,verbose_name="Ürün İsmi - DE")
    title_en = models.CharField(max_length=150,verbose_name="Ürün İsmi - EN")
    product_type = models.CharField(max_length=150,verbose_name="Ürün Tipi")
    content_de = RichTextField(verbose_name="Ürün Açıklamaları - DE")
    content_en = RichTextField(verbose_name="Ürün Açıklamaları - EN")
    slug = models.SlugField(unique=True,editable=False,max_length=130)

    image_de = models.ImageField(verbose_name="Ürün Resmi - DE")
    image_en = models.ImageField(blank=True,verbose_name="Ürün Resmi - EN (Zorunlu Değil)")

    spec_file_de = models.FileField(verbose_name="Teknik Özellikler Dosyası (Pdf) - DE",blank=True)
    spec_file_en = models.FileField(verbose_name="Teknik Özellikler Dosyası (Pdf) - EN",blank=True)


    catalog_file_de = models.FileField(verbose_name="Ürün Kataloğu (Pdf) - DE",blank=True)
    catalog_file_en = models.FileField(verbose_name="Ürün Kataloğu (Pdf) - EN",blank=True)

    def save(self, *args, **kwargs):
        if True:

            auto_test = Automatic_Doors.objects.all().order_by("id")
            value = 0
            for x in auto_test:
                uniqe_slug = slugify(self.title_de)
                if value > 0:
                    control_slug = str(uniqe_slug) + "-{0}".format(value)
                else:
                    control_slug = uniqe_slug

                if x.slug == control_slug:
                    value +=1
            if auto_test and value > 0:
                self.slug = str(uniqe_slug) + "-{0}".format(value)
            else:
                self.slug = slugify(self.title_en)
            super(Automatic_Doors, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/products/automatic-doors/{self.slug}'

    def __str__(self):

        return self.title_de

    class Meta:

        verbose_name_plural = 'Otomatik Kapılar'
        ordering = ['-id']


class Hospital_Doors(models.Model):

    title_de = models.CharField(max_length=150,verbose_name="Ürün İsmi - DE")
    title_en = models.CharField(max_length=150,verbose_name="Ürün İsmi - EN")
    product_type = models.CharField(max_length=150,verbose_name="Ürün Tipi")
    content_de = RichTextField(verbose_name="Ürün Açıklamaları - DE")
    content_en = RichTextField(verbose_name="Ürün Açıklamaları - EN")
    slug = models.SlugField(unique=True,editable=False,max_length=130)

    image_de = models.ImageField(verbose_name="Ürün Resmi - DE")
    image_en = models.ImageField(blank=True,verbose_name="Ürün Resmi - EN (Zorunlu Değil)")

    spec_file_de = models.FileField(verbose_name="Teknik Özellikler Dosyası (Pdf) - DE",blank=True)
    spec_file_en = models.FileField(verbose_name="Teknik Özellikler Dosyası (Pdf) - EN",blank=True)

    catalog_file_de = models.FileField(verbose_name="Ürün Kataloğu (Pdf) - DE",blank=True)
    catalog_file_en  = models.FileField(verbose_name="Ürün Kataloğu (Pdf) - EN",blank=True)

    def __str__(self):

        return self.title_de

    def save(self, *args, **kwargs):
        if True:

            hospital_test = Hospital_Doors.objects.all().order_by("id")
            value = 0
            for x in hospital_test:
                uniqe_slug = slugify(self.title_en)
                if value > 0:
                    control_slug = str(uniqe_slug) + "-{0}".format(value)
                else:
                    control_slug = uniqe_slug

                if x.slug == control_slug:
                    value +=1

            if hospital_test and value > 0:
                self.slug = str(uniqe_slug) + "-{0}".format(value)
            else:
                self.slug = slugify(self.title_en)
            super(Hospital_Doors, self).save(*args, **kwargs)

    class Meta:

        verbose_name_plural = 'Hastane Kapıları'
        ordering = ['-id']

    def get_absolute_url(self):
        return f'/products/hospital-doors/{self.slug}'


class Request_Messages(models.Model):

    email = models.EmailField(verbose_name="Gönderen Email'i",max_length=200)
    full_name = models.CharField(verbose_name="Gönderen Adı Soyadı",max_length=200)
    message = models.TextField(verbose_name="Mesaj")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Gelen İstekler'
        ordering = ['-id']

class Failure_Notification(models.Model):

    full_name = models.CharField(verbose_name="Adı Soyadı",max_length=200)
    company = models.CharField(verbose_name="Firma Adı",max_length=200)
    email = models.EmailField(verbose_name="Email'i",max_length=200)
    phone_number = models.CharField(verbose_name="Telefon Numarası",max_length=200)
    address = models.CharField(verbose_name="Address",max_length=200)
    door_model = models.CharField(verbose_name="Kapı Türü",max_length=200)
    trademark = models.CharField(verbose_name="Model",max_length=200)

    fault = models.TextField(verbose_name="fault")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Arıza Bildirimleri'
        ordering = ['-id']

class Security_Doors(models.Model):

    title_de = models.CharField(max_length=150,verbose_name="Ürün İsmi - DE")
    title_en = models.CharField(max_length=150,verbose_name="Ürün İsmi - EN")
    product_type = models.CharField(max_length=150,verbose_name="Ürün Tipi")
    content_de = RichTextField(verbose_name="Ürün Açıklamaları - DE")
    content_en = RichTextField(verbose_name="Ürün Açıklamaları - EN")
    slug = models.SlugField(unique=True,editable=False,max_length=130)

    image_de = models.ImageField(verbose_name="Ürün Resmi - DE")
    image_en = models.ImageField(blank=True,verbose_name="Ürün Resmi - EN (Zorunlu Değil)")

    spec_file_de = models.FileField(verbose_name="Teknik Özellikler Dosyası (Pdf) - DE",blank=True)
    spec_file_en = models.FileField(verbose_name="Teknik Özellikler Dosyası (Pdf) - EN",blank=True)

    catalog_file_de = models.FileField(verbose_name="Ürün Kataloğu (Pdf) - DE",blank=True)
    catalog_file_en  = models.FileField(verbose_name="Ürün Kataloğu (Pdf) - EN",blank=True)

    def __str__(self):

        return self.title_de

    def save(self, *args, **kwargs):
        if True:

            security_test = Security_Doors.objects.all().order_by("id")
            value = 0
            for x in security_test:
                uniqe_slug = slugify(self.title_en)
                if value > 0:
                    control_slug = str(uniqe_slug) + "-{0}".format(value)
                else:
                    control_slug = uniqe_slug

                if x.slug == control_slug:
                    value +=1

            if security_test and value > 0:
                self.slug = str(uniqe_slug) + "-{0}".format(value)
            else:
                self.slug = slugify(self.title_en)
            super(Security_Doors, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/products/security-doors/{self.slug}'

    class Meta:

        verbose_name_plural = 'Security Kapıları'
        ordering = ['-id']