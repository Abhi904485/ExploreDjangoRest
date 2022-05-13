from django.urls import path
from .api_views import SnippetGenericList, SnippetGenericDetail

urlpatterns = [
    path('snippets_generic_class_view/', SnippetGenericList.as_view()),
    path('snippets_generic_class_view/<int:pk>/', SnippetGenericDetail.as_view())
]
