from django.db import models
from django.urls import reverse

ARCTYPE = (
    ('Modern', 'Modern'),
    ('MCM', 'Midcentury Modern'),
    ('NC', 'Neo Classical'),
    ('R', 'California Romanza'),
    ('CR', 'Craftsman'),
    ('COL', 'Colonial Revival'),
    ('SP', 'Spanish'),
    ('CHT','Châteauesque'),
)

# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=50)
    yearbuilt = models.IntegerField()
    description = models.TextField(max_length=250)
    arc_type = models.CharField(
        max_length=20,
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
    

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'listing_id': self.id})
    