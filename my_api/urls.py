from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome_view, name="welcome_view"),
    path('api/', views.user_info, name="user_info"),
]
