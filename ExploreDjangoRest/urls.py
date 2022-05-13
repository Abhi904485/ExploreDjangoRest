"""ExploreDjangoRest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# Below is the way to add all apis using router alternate way is present at snippets_simple_api_using_viewsets.api_urls

# from rest_framework.routers import DefaultRouter
# from snippets_viewsets.api_views import SnippetList as sv
# from snippets_viewset_mixin.api_views import SnippetList as smv
# from snippets_modelviewset.api_views import SnippetList as smov
#
# router = DefaultRouter()
#
# router.register('SnippetViewSet', sv, basename='SnippetViewSet')
# router.register('SnippetMixinViewSet', smv, basename='SnippetMixinViewSet')
# router.register('SnippetModelViewSet', smov, basename='SnippetModelViewSet')

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Snippets Rest Documentation using Yet Another Swagger",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('auth/', include('rest_framework.urls')),
    path('', include('snippets_simple_api.api_urls'), name="snippets_simple_api"),
    path('', include('snippets_function_view.api_urls'), name="snippets_simple_api_using_apiview"),
    path('', include('snippets_api_class_view.api_urls'), name="snippets_simple_api_using_class_view"),
    path('', include('snippets_mixin_class_view.api_urls'), name="snippets_simple_api_using_mixin"),
    path('', include('snippets_generic_class_view.api_urls'), name="snippets_simple_api_using_generic_class"),
    path('', include('snippets_viewsets.api_urls'), name="snippets_simple_api_using_viewsets"),
    path('', include('snippets_modelviewset.api_urls'), name="snippets_simple_api_using_viewsets"),
    path('', include('snippets_viewset_mixin.api_urls'), name="snippets_simple_api_using_viewsets")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += router.urls

