from django.urls import path
from ecommerceapp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contactus", views.contactus, name="contactus"),
    path("aboutus", views.aboutus, name="aboutus"),
]