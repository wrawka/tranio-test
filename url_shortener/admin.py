from django.contrib import admin

from url_shortener.models import UserShortURL


@admin.register(UserShortURL)
class URLAdmin(admin.ModelAdmin):
    pass
