from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Gallery

def gallery_view(request):

    title = ''
    gallery = Gallery.objects.all()

    if request.LANGUAGE_CODE == 'de':
        title = 'Galeri - ARSLANYAPI'
    else:
        title = 'Gallery - ARSLANYAPI'

    paginator = Paginator(gallery, 12)

    page = request.GET.get('sayfa')
    images = paginator.get_page(page)

    context = {
        'title':title,
        'all_objects':images,
    }

    return render(request,'gallery/gallery.html',context)

def gallery_automatic_view(request):

    title = ''
    gallery = Gallery.objects.filter(product_category="Otomatik Kapılar")

    if request.LANGUAGE_CODE == 'de':
        title = 'Galeri | Otomatik Kapılar - ARSLANYAPI'
    else:
        title = 'Gallery | Automatic Doors - ARSLANYAPI'

    paginator = Paginator(gallery, 12)

    page = request.GET.get('sayfa')
    images = paginator.get_page(page)

    context = {
        'title':title,
        'all_objects':images,
    }

    return render(request,'gallery/gallery-automatic.html',context)


def gallery_hospital_view(request):

    title = ''
    gallery = Gallery.objects.filter(product_category="Hastane Kapıları")

    if request.LANGUAGE_CODE == 'de':
        title = 'Galeri | Hastane Kapıları - ARSLANYAPI'
    else:
        title = 'Gallery | Hospital Doors - ARSLANYAPI'

    paginator = Paginator(gallery, 12)

    page = request.GET.get('sayfa')
    images = paginator.get_page(page)

    context = {
        'title':title,
        'all_objects':images,
    }

    return render(request,'gallery/gallery-hospital.html',context)

def gallery_security_view(request):

    title = ''
    gallery = Gallery.objects.filter(product_category="Security Kapıları")

    if request.LANGUAGE_CODE == 'de':
        title = 'Galeri | Security Kapıları - ARSLANYAPI'
    else:
        title = 'Gallery | Security Doors - ARSLANYAPI'

    paginator = Paginator(gallery, 12)

    page = request.GET.get('sayfa')
    images = paginator.get_page(page)

    context = {
        'title':title,
        'all_objects':images,
    }

    return render(request,'gallery/gallery-security.html', context)

