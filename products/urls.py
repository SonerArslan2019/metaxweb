from django.urls import path, include
from .views import *

urlpatterns = [
    path('automatic-doors/',automatic_doors_list,name='automatic-doors'),
    path('automatic-doors/<slug>/',automatic_doors_content,name='automatic-doors-content'),
    path('hospital-doors/',hospital_doors_list,name='hospital-doors'),
    path('hospital-doors/<slug>/',hospital_doors_content,name='hospital-doors-content'),
    path('security-doors/',security_doors_list,name='security-doors'),
    path('security-doors/<slug>/',security_doors_content,name='security-doors-content'),
]



