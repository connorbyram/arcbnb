from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listings/', views.listings_index, name='index'),
    path('listings/<int:listing_id>/', views.listings_detail, name='detail'),

    path('accounts/signup/', views.signup, name='signup'),
]
