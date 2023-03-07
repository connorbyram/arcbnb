from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Listing, Booking
from .forms import BookingForm


# Create your views here.
def home(request):
    return render(request, 'home.html')
def listings_index(request):
    listings = Listing.objects.all()
    return render(request, 'listings/index.html', {
       'listings': listings
    })
def listings_detail(request, listing_id):
   listing = Listing.objects.get(id=listing_id)
   booking_form = BookingForm()
   return render(request, 'listings/detail.html', {
      'listing': listing, 'booking_form': booking_form
   })
  
def add_booking(request, listing_id):
   if request.user.is_authenticated:
      user = request.user
      form = BookingForm(request.POST)
      if form.is_valid():
         new_booking = form.save(commit=False)
         new_booking.listing_id = listing_id
         new_booking.user = user
         new_booking.save()
      return redirect('/', listing_id=listing_id)
   else:
      return redirect('/accounts/login', listing_id=listing_id)


def user_bookings(request):
   user = request.user
   bookings = Booking.objects.filter(user=user)
   return render(request, 'user/bookings.html', {
      'user': user,
      'bookings': bookings,
   })




def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - Try Again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)