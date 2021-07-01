from django.db import models
from datetime import datetime
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Realtor(models.Model):

    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now())

    class Meta:
        ordering = ['name', 'email', 'hire_date']

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse("Realtor_detail", kwargs={"pk": self.pk})
