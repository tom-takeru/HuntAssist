from django.urls import path
from . import views

app_name = 'es_manager'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('es_list/', views.EntrySheetListView.as_view(), name='es_list'),
    path('es_detail/<int:pk>/', views.EntrySheetDetailView.as_view(), name='es_detail'),
    path('es_create/', views.EntrySheetCreateView.as_view(), name='es_create'),
    path('es_update/<int:pk>/', views.EntrySheetUpdateView.as_view(), name='es_update'),
    path('es_delete/<int:pk>/', views.EntrySheetDeleteView.as_view(), name='es_delete'),
]
