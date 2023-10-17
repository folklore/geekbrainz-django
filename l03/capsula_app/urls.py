from django.urls import path
from .views import listing


urlpatterns = [
    path('listing/<str:interval>/', listing, name='listing')
]
