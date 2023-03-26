from django.urls import path

from url_shortener import views

urlpatterns = [
    path('', views.urls_index, name='index'),
    path('stats/', views.urls_stats, name='stats'),
    path('<str:key>/', views.short_url_redirect, name='url-redirect'),
]
