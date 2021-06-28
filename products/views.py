from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator
from .models import *


#Otomatik Kapılar
def automatic_doors_list(request):

    title = ''
    auto_doors = Automatic_Doors.objects.all()

    if request.LANGUAGE_CODE == 'de':
        title = 'Otomatik Kapılar - METAXDOOR'
    else:
        title = 'Automatic Doors - METAXDOOR'

    paginator = Paginator(auto_doors,8) #

    page = request.GET.get('sayfa')
    auto_doors_page = paginator.get_page(page)

    context = {
        'title':title,
        'all_objects':auto_doors_page,
    }

    return render(request,'products/automatic_doors/list.html',context)


def automatic_doors_content(request,slug):

    title = ''
    auto_doors = get_object_or_404(Automatic_Doors,slug=slug)

    if request.LANGUAGE_CODE == 'de':
        title = auto_doors.title_de
    else:
        title = auto_doors.title_en

    if 'request-file' in request.POST:

        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        message = request.POST.get('message')
        print(email,full_name,message)

        Request_Messages.objects.create(email=email,full_name=full_name,message=message)

        request.session['send-status'] = True

    else:

        request.session['send-status'] = False

    context = {
        'title':title,
        'auto_doors':auto_doors,
        'status':request.session['send-status'],
    }

    return render(request,'products/automatic_doors/content.html',context)


#Hastane Kapıları
def hospital_doors_list(request):

    title = ''
    hospital_doors = Hospital_Doors.objects.all()

    if request.LANGUAGE_CODE == 'de':
        title = 'Hastane Kapıları - METAXDOOR'
    else:
        title = 'Hospital Doors - METAXDOOR'

    paginator = Paginator(hospital_doors,8) #

    page = request.GET.get('sayfa')
    hospital_doors_page = paginator.get_page(page)

    context = {
        'title':title,
        'all_objects':hospital_doors_page,
    }

    return render(request,'products/hospital_doors/list.html',context)


def hospital_doors_content(request,slug):

    title = ''
    hospital_doors = get_object_or_404(Hospital_Doors,slug=slug)

    if request.LANGUAGE_CODE == 'de':
        title = hospital_doors.title_de
    else:
        title = hospital_doors.title_en

    if 'request-file' in request.POST:

        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        message = request.POST.get('message')
        print(email,full_name,message)

        Request_Messages.objects.create(email=email,full_name=full_name,message=message)


        request.session['send-status'] = True

    else:

        request.session['send-status'] = False

    context = {
        'title':title,
        'hospital_doors':hospital_doors,
        'status':request.session['send-status'],
    }

    return render(request,'products/hospital_doors/content.html',context)

#Security Kapıları

def security_doors_list(request):

    title = ''
    security_doors = Security_Doors.objects.all()

    if request.LANGUAGE_CODE == 'de':
        title = 'Security Yüksek Güvenlikli Kapılar - METAXDOOR'
    else:
        title = 'Security Doors - METAXDOOR'

    paginator = Paginator(security_doors,8) #

    page = request.GET.get('sayfa')
    security_doors_page = paginator.get_page(page)

    context = {
        'title':title,
        'all_objects':security_doors_page,
    }

    return render(request,'products/security_doors/list.html',context)


def security_doors_content(request,slug):

    title = ''
    security_doors = get_object_or_404(Security_Doors,slug=slug)

    if request.LANGUAGE_CODE == 'de':
        title = security_doors.title_de
    else:
        title = security_doors.title_en

    if 'request-file' in request.POST:

        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        message = request.POST.get('message')
        print(email,full_name,message)

        Request_Messages.objects.create(email=email,full_name=full_name,message=message)


        request.session['send-status'] = True

    else:

        request.session['send-status'] = False

    context = {
        'title':title,
        'security_doors':security_doors,
        'status':request.session['send-status'],
    }

    return render(request,'products/security_doors/content.html',context)
