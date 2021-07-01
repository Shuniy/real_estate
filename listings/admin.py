from django.contrib import admin
from listings.models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor', 'state')
    list_display_links = ('id', 'title')

    list_filter = ('realtor', 'city', 'state')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')

    list_per_page = 20

admin.site.register(Listing, ListingAdmin)