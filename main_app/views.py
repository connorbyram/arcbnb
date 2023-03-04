from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Listing


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
   return render(request, 'listings/detail.html', {
      'listing': listing
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