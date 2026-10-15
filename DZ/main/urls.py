from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),
]

