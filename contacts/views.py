from contacts.models import Contact
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']

        # check if query already made
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)

            if has_contacted:
                messages.error(request, 'You already made query on that listing, waith for the realtor reply')
                return redirect('/listings/' + listing_id)
        
        contact = Contact(listing = listing, listing_id = listing_id, name = name, email = email, phone = phone, message = message, user_id = user_id)
        contact.save()
        # send mail to realtor about inquiry
        send_mail(
            'Property Listing Inquiry',
            'There has been an Inquiry for ' + listing + '/Sign into the admin panel for more information.',
            'put_your_email@gmail.com',
            [realtor_email, 'other emails here'],
            fail_silently=False,
        )

        messages.success(request, 'Your Query is sent.')
        return redirect('/listings/' + listing_id)
