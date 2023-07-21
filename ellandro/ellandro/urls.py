
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from web.views import Homepage, Products, Contact, ContactPage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Homepage.as_view(), name="homepage"),
    path('products/', Products.as_view(), name="products" ),
    path('contact_form/', Contact.as_view(), name="contact" ),
    path('contactpage/', ContactPage.as_view(), name="contact_page")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
