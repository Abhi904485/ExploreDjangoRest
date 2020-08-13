from django.urls import path
from .api_views import SnippetList, SnippetDetail

urlpatterns = [
    path('snippets_api_mixin_view/', SnippetList.as_view()),
    path('snippets_api_mixin_view/<int:pk>/', SnippetDetail.as_view())
]
