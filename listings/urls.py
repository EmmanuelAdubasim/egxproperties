from django.urls import path
from .views import home, listings_page, listing_detail, about, contact

urlpatterns = [
    path("", home, name="home"),
    path("listings/", listings_page, name="listings"),
    path("listings/<slug:slug>/", listing_detail, name="listing_detail"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
]
