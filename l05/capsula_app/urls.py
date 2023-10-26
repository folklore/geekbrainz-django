from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (listing,
                    edit_product,
                    update_product)


urlpatterns = [
    path('listing/<str:interval>/', listing, name='listing'),
    path('edit_product/<int:pk>/', edit_product, name='edit_product'),
    path('update_product/<int:pk>/', update_product, name='update_product')
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
