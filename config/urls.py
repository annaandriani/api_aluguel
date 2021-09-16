from django.urls import path
from snippets import views

urlpatterns = [
    path(r'host/', views.Host_list),
    path(r'cleaning/',views.Cleaning_list),
    path(r'checkin/', views.Checkin_list),
    path(r'checkout/', views.Checkout_list),
]