from django.contrib import admin
from django.contrib.admin.sites import site
from realtors.models import Realtor

# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'phone')
    list_per_page = 20

admin.site.register(Realtor, RealtorAdmin)
