from django.contrib import admin
from .models import Listing, Booking, Amenity


admin.site.register(Listing)
admin.site.register(Booking)
admin.site.register(Amenity)