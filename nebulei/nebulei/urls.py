from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# URLS

django_urls = [
    path('admin/', admin.site.urls),
]

third_party_urls = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

nebulei_urls = [
    path('api/user/', include('account.urls', namespace='account')),
]



urlpatterns = django_urls + nebulei_urls + third_party_urls


