from django.contrib import admin
from .models import Radio


class RadioAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


admin.site.register(Radio, RadioAdmin)