from django.urls import path
from .views import QuoteListAPI

urlpatterns = [
    path("quotes/", QuoteListAPI.as_view(), name="quote-list"),
]