from django.db import models
from datetime import datetime
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Contact(models.Model):

    listing = models.CharField(max_length=100)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = PhoneNumberField()
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    class Meta:
        ordering = ['name', 'email', 'phone', 'listing', 'user_id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Contact_detail", kwargs={"pk": self.pk})
