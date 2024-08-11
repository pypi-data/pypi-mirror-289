from datetime import datetime
from django.contrib import admin
from django.utils.timesince import timesince

from .models import Stdout as Model

class ModelAdmin(admin.ModelAdmin):
    list_display = ['id','app','command','stdout_intro','size','timesince']
    list_filter = ('app', 'command', )
    search_fields = ('app','command', 'stdout',)

    def stdout_intro(self, obj):
        return obj.stdout[0:100].strip()

    def timesince(self, obj):
        return timesince(datetime.fromtimestamp(obj.created_at)).split(',')[0]+' ago'

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Model, ModelAdmin)
