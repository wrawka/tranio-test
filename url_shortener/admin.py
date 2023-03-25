from django.contrib import admin
from models import UserShortURL


@admin.register(UserShortURL)
class URLAdmin(admin.ModelAdmin):
    pass
