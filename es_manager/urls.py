from django.urls import path
from . import views

app_name = 'es_manager'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('es_list/', views.EntrySheetListView.as_view(), name='es_list')
]
