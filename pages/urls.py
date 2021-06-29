from django.urls import path
from pages import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('about/', view=views.about, name='about'),
]
