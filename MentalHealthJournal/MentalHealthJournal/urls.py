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

# from asyncio import start_server
from functools import cache

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
#from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.decorators.cache import cache_page
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token

from MentalHealthJournal import settings
from users.views import (AccountUpdateView, HomeView, LoginFormView,
                         LogOutTemplateView, SignUpFormView, JournalView)

# from tkinter.font import names




# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view
# from rest_framework import permissions



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cache_page(30)(HomeView.as_view(extra_context={'title': 'MentalHealthJournal'})), name='HomeView'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('sign_up/', SignUpFormView.as_view(), name='sign_up'),
    path('account/', AccountUpdateView.as_view(), name='account'),
    #  path('edit_account/', name='edit_account'),
    path('logout/', LogOutTemplateView.as_view(), name='logout'),
    path('accounts/', include('allauth.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('account/', JournalView.as_view(), name='account'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )





# schema_views = get_schema_view(
#     openapi.Info(
#         title="Mental Health Journal API",
#         default_version='v1',
#         description="API documentation for Mental Health Journal",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="support@example.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

# Cntr + D - продублировать строку


    # Swagger & Redoc
    # path('swagger/', schema_views.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_views.with_ui('redoc', cache_timeout=8), name='schema-redoc'),
