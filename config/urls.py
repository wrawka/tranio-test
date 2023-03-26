from django.urls import include, path

urlpatterns = [
    path('urls/', include('url_shortener.urls')),
]
