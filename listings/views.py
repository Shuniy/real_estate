from django.http import request
from django.shortcuts import render

# Create your views here.
def listing(request):
    return render(request, 'listings/listing.html')


def listings(request):
    return render(request, 'listings/listings.html')


def search(request):
    return render(request, 'listings/search.html')
