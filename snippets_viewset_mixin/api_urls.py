# Alternate way of adding routes without router
from django.urls import path

from .api_views import SnippetList

snippet_list = SnippetList.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    path('snippets_mixin_viewsets/', snippet_list, name='snippet-list'),
    path('snippets_mixin_viewsets/<int:pk>/', snippet_detail, name='snippet-detail'),
]
