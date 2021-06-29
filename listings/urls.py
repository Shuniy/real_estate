from django.urls import path
from listings import views

urlpatterns = [
    path('', view=views.listings, name='listings'),
    path('<int:listing_id>/', view=views.listing, name='listing'),
    path('search/', view=views.search, name='search'),

]
