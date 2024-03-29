# Generated by Django 5.0 on 2023-12-15 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_de', models.CharField(max_length=80, verbose_name='Resim Başlığı - DE')),
                ('title_en', models.CharField(max_length=80, verbose_name='Resim Başlığı - EN')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Resim')),
                ('video', models.CharField(blank=True, max_length=300, verbose_name='Video Url(YouTube)')),
                ('product_category', models.CharField(choices=[('Otomatik Kapılar', 'Otomatik Kapılar'), ('Hastane Kapıları', 'Hastane Kapıları'), ('Security Kapıları', 'Security Kapıları')], default='Otomatik Kapılar', max_length=500, verbose_name='Ürün Kategorisi')),
            ],
            options={
                'verbose_name_plural': 'Galeri',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Popup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Başlık')),
                ('content', models.TextField(verbose_name='Kısa Mesaj')),
                ('image', models.ImageField(upload_to='', verbose_name='Popup Resimi')),
                ('upgrade_date', models.DateTimeField(editable=False, verbose_name='Güncellenme Tarihi')),
                ('finish_date', models.DateTimeField(verbose_name='Bitiş Tarihi')),
            ],
            options={
                'verbose_name_plural': 'Popups',
                'ordering': ['-upgrade_date'],
            },
        ),
    ]
