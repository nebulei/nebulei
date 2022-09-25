from django.contrib import admin
from django.urls import path, include


# URLS

django_urls = [
    path('admin/', admin.site.urls),
]

third_party_urls = [
    #path('api/', include('rest_framework.urls')),
]

nebulei_urls = [
]



urlpatterns = django_urls + nebulei_urls + third_party_urls


