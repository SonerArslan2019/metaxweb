# from django.shortcuts import render,HttpResponse
# from news.models import News
# from core.settings import BASE_DIR
# from products.models import Automatic_Doors, Hospital_Doors, Security_Doors
# import os
# from root.models import Company,Call_Back,Privacy_Policy
# from gallery.models import Popup
# from datetime import datetime, timezone
#
#
# def home_view(request):
#     popup = Popup.objects.all()
#     view_popup = None
#     if popup:
#         view_popup = popup[0]
#         if view_popup.finish_date < datetime.now(timezone.utc):
#             view_popup = None
#     title = ''
#     news = News.objects.all()[0:3]
#     auto_doors = Automatic_Doors.objects.all()
#     hospital_doors = Hospital_Doors.objects.all()
#     security_doors = Security_Doors.objects.all()
#
#     if request.LANGUAGE_CODE == 'tr':
#
#         title = 'Otomatik Kapılar, Hastane Kapıları ve Security Çözümleri - METAXDOOR - ARSLANYAPI'
#     else:
#         title = 'Automatic Doors, Hospital and Security Doors Solutions - METAXDOOR - ARSLANYAPI'
#
#     context = {
#         'news':news,
#         'title':title,
#         'auto_doors':auto_doors[0:3],
#         'hospital_doors':hospital_doors[0:3],
#         'security_doors': security_doors[0:3],
#         'view_popup':view_popup,
#
#     }
#
#     return render(request,'home.html',context)
#
#
# def pdf_view(request,file):
#
#     with open('%s/%s'%(os.path.join(BASE_DIR,'media'),file), 'rb') as pdf:
#
#         response = HttpResponse(pdf.read(), content_type='application/pdf')
#         response['Content-Disposition'] = 'inline;filename=%s'%(file)
#         return response
#     pdf.closed
#
#
#
# def company_view(request):
#
#     title =''
#     company = Company.objects.all().last()
#
#     if request.LANGUAGE_CODE == 'tr':
#         title = 'Şirket - ARSLANYAPI'
#     else:
#         title = 'Company - ARSLANYAPI'
#
#     context = {
#         'company':company,
#         'title':title,
#     }
#
#     return render(request,'company.html',context)
#
# def contact_view(request):
#
#     title = ''
#
#     if request.LANGUAGE_CODE == 'tr':
#         title = 'İletişim - ARSLANYAPI'
#     else:
#         title = 'Contact - ARSLANYAPI'
#
#     if 'btn_click' in request.POST:
#
#         full_name = request.POST.get('full_name')
#         company = request.POST.get('company')
#         phone = request.POST.get('phone')
#         privacy = request.POST.get('check_privacy')
#         print(privacy)
#
#         if privacy in 'on':
#             status = True
#
#         if status:
#
#             Call_Back.objects.create(full_name=full_name,company=company,phone=phone,confirm=status)
#
#         request.session['btn_click-send'] = True
#     else:
#         request.session['btn_click-send'] = False
#
#     context = {
#         'title':title,
#         'status':request.session['btn_click-send'],
#
#     }
#
#     return render(request,'contact.html',context)
#
#
#
# def privacy_view(request):
#
#     title = ''
#     privacy = Privacy_Policy.objects.all().last()
#
#     if request.LANGUAGE_CODE == 'tr':
#         title = 'Gizlilik Politikası'
#     else:
#         title = 'Privacy Policy'
#
#     context  = {
#         'title':title,
#         'privacy':privacy,
#     }
#     return render(request,'privacy.html',context)
