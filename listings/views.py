from django.http import request
from django.shortcuts import get_object_or_404, render
from listings.models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from listings.choices import bedroom_choices, state_choices, price_choices

# Create your views here.

def listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings =  paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context=context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing':listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    query_set_list = Listing.objects.order_by('-list_date')

    # if keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_set_list = query_set_list.filter(description__icontains=keywords)

    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_set_list = query_set_list.filter(
                city__iexact=city)

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_set_list = query_set_list.filter(
                state__iexact=state)

    # bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_set_list = query_set_list.filter(
                bedrooms__lte=bedrooms).order_by('-bedrooms')
    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_set_list = query_set_list.filter(
                price__lte=price).order_by('-price')

    paginator = Paginator(query_set_list, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'listings':paged_listings,
        'values':request.GET,
    }

    return render(request, 'listings/search.html', context)
