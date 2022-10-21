from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('ajax/validate_username/', views.validate_username, name='validate_username'),
    path('admin/', admin.site.urls, name='admin'),
    path('api-auth/', include('rest_framework.urls')),
]