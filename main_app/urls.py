from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listings/', views.listings_index, name='index'),
    path('listings/<int:listing_id>/', views.listings_detail, name='detail'),
    path('listings/filter/<int:feature_id>/', views.index_feature, name='index_feature'),
    path('listings/<int:listing_id>/add_booking/', views.add_booking, name='add_booking'),
    path('user/bookings/', views.user_bookings, name='bookings'),
    path('user/bookings/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('user/bookings/<int:pk>/update/', views.BookingUpdate.as_view(), name='booking_update'),
    path('user/bookings/<int:pk>/delete/', views.BookingDelete.as_view(), name='booking_delete'),

    path('accounts/signup/', views.signup, name='signup'),
]
