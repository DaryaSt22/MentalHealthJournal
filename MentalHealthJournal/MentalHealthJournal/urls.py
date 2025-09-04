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

from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.views.decorators.cache import cache_page
from rest_framework.authtoken.views import obtain_auth_token
from users.views import (AccountView, HomeView, LoginFormView,
                         LogOutTemplateView, SignUpFormView, logout_then_home)

from MentalHealthJournal import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(extra_context={'title': 'MentalHealthJournal'}), name='HomeView'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('sign_up/', SignUpFormView.as_view(), name='sign_up'),
    path('account/', AccountView.as_view(), name='account'),
    # path('account/', AccountUpdateView.as_view(), name='account'),
    # path('edit_account/', name='edit_account'),
    path('logout/', logout_then_home, name='logout'),
    path('accounts/', include('allauth.urls')),
    path('api-token-auth/', obtain_auth_token),
    path("journal/", include("journal.urls"))
]

static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

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

    # Swagger & Redoc
    # path('swagger/', schema_views.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_views.with_ui('redoc', cache_timeout=8), name='schema-redoc'),
