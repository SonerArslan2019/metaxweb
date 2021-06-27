from django.urls import path,include
from .views import news_list_view, news_detail_view

urlpatterns = [
    path('',news_list_view,name="news"),
    path('<slug>/',news_detail_view,name='news-detail'),
]



