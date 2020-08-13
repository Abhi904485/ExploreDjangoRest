from django.urls import path
from .api_views import SnippetGenericList, SnippetGenericDetail

urlpatterns = [
    path('snippets_api_generic_view/', SnippetGenericList.as_view()),
    path('snippets_api_generic_view/<int:pk>/', SnippetGenericDetail.as_view())
]
