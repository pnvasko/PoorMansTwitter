from django.contrib import admin

from .models import Twitters


class AdminTwitters(admin.ModelAdmin):
    pass


admin.site.register(Twitters, AdminTwitters)
