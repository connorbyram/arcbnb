from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User

ARCTYPE = (
    ('Modern', 'Modern'),
    ('Midcentury Modern', 'Midcentury Modern'),
    ('Neo Classica', 'Neo Classical'),
    ('California Romanza', 'California Romanza'),
    ('Craftsman', 'Craftsman'),
    ('Colonial Revival', 'Colonial Revival'),
    ('Spanish', 'Spanish'),
    ('Châteauesque','Châteauesque'),
)



class Amenity(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('amenities_detail', kwargs={'pk': self.id})

class Listing(models.Model):
    name = models.CharField(max_length=50)
    yearbuilt = models.IntegerField()
    description = models.TextField(max_length=250)
    arc_type = models.CharField(
        max_length=50,
        choices=ARCTYPE,
        default=ARCTYPE[0][0]
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    guest_num = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    available = models.BooleanField()
    main_img = models.CharField(max_length=200)
    second_img = models.CharField(max_length=200)
    third_img = models.CharField(max_length=200)
    fourth_img = models.CharField(max_length=200)
    fifth_img = models.CharField(max_length=200)

    amenities = models.ManyToManyField(Amenity)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'listing_id': self.id})
    
class Booking(models.Model):
    date = models.DateField('Booking Date', default=datetime.now())
    checkin = models.DateField('Checkin Date', default=datetime.now())
    checkout = models.DateField('Checkout Date', default=datetime.now())
    guests = models.IntegerField()
    listing = models.ForeignKey(
        Listing, 
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('booking_detail', kwargs={'booking_id': self.id})

    def __str__(self):
        return f'{self.user} made a booking for ({self.listing.name})'