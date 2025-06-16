"""
URL configuration for MentalHealthJournal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from functools import cache

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users import views
# from .views import ping
from users.views import home, authorization
from django.contrib.auth import views as auth_views


schema_views = get_schema_view(
    openapi.Info(
        title="Mental Health Journal API",
        default_version='v1',
        description="API documentation for Mental Health Journal",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), # Cntr + D - продублировать строку
    #path('login', authorization, name='login'),
    path('/login', views.custom_login, name='login'),
    path('/signUp', views.sign_up_user, name='signUp'),
    path('/signUp', auth_views.LoginView.as_view(template_name='registration/signUp.html'), name='signUp')



    # Swagger & Redoc
    # path('swagger/', schema_views.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_views.with_ui('redoc', cache_timeout=8), name='schema-redoc'),
]
