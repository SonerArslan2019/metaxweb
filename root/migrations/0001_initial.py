# Generated by Django 3.2.4 on 2021-06-28 19:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call_Back',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='Ad Soyad')),
                ('company', models.CharField(max_length=200, verbose_name='Şirket')),
                ('phone', models.CharField(max_length=200, verbose_name='Telefon')),
                ('confirm', models.BooleanField(verbose_name='Gizlilik Politikası Onayı')),
            ],
            options={
                'verbose_name_plural': 'Geri Arama Talepleri',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_de', ckeditor.fields.RichTextField(verbose_name='İçerik DE')),
                ('content_en', ckeditor.fields.RichTextField(verbose_name='İçerik EN')),
            ],
            options={
                'verbose_name_plural': 'Şirket',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Privacy_Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_de', ckeditor.fields.RichTextField(verbose_name='İçerik DE')),
                ('content_en', ckeditor.fields.RichTextField(verbose_name='İçerik EN')),
            ],
            options={
                'verbose_name_plural': 'Gizlilik Politikası',
                'ordering': ['-id'],
            },
        ),
    ]
