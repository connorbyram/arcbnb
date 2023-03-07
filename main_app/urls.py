from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listings/', views.listings_index, name='index'),
    path('listings/<int:listing_id>/', views.listings_detail, name='detail'),
    path('listings/<int:listing_id>/add_booking/', views.add_booking, name='add_booking'),
    path('user/bookings/', views.user_bookings, name='bookings'),

    path('accounts/signup/', views.signup, name='signup'),
]
