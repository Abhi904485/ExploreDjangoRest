from django.urls import path
from .api_views import SnippetList, SnippetDetail

urlpatterns = [
    path('snippets_class_view/', SnippetList.as_view()),
    path('snippets_class_view/<int:pk>/', SnippetDetail.as_view())
]
