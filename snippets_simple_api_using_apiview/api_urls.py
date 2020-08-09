from django.urls import path
from .api_views import snippet_list_api_view, snippet_detail_api_view

urlpatterns = [
    path('snippets_api_view/', snippet_list_api_view),
    path('snippets_api_view/<int:pk>/', snippet_detail_api_view),
]
