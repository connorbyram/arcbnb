from django.forms import ModelForm
from .models import Booking 
from django.contrib.auth.models import User

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'guests']