from django.http import HttpResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import SimpleApiFunctionViewSnippetSerializer
from .models import SnippetApiFunctionView, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

title = openapi.Parameter(
    name="title",
    description="Enter Title",
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    required=True
)
code = openapi.Parameter(
    name="code",
    description="Enter Code",
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    required=True
)
linenos = openapi.Parameter(
    name="linenos",
    description="Enter linenos",
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_BOOLEAN,
    default=False
)
language = openapi.Parameter(
    name="language",
    description="Enter Language",
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    enum=[lan[0] for lan in LANGUAGE_CHOICES],
    default="python"

)
style = openapi.Parameter(
    name="style",
    description="Enter Style",
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    enum=[style[0] for style in STYLE_CHOICES],
    default="friendly",
)


@swagger_auto_schema(method='GET', operation_description="Retrieve all code SnippetApiFunctionView.",
                     responses={status.HTTP_200_OK: SimpleApiFunctionViewSnippetSerializer,
                                status.HTTP_404_NOT_FOUND: "Not Found"},
                     operation_summary="Retrieve all code SnippetApiFunctionView."
                     )
@swagger_auto_schema(method='POST',
                     manual_parameters=[title, code, linenos, language, style],
                     responses={status.HTTP_201_CREATED: SimpleApiFunctionViewSnippetSerializer,
                                status.HTTP_400_BAD_REQUEST: "Bad Request"},
                     operation_summary="Summary of List all code snippets, or create a new SnippetApiFunctionView.",
                     operation_description="List all code snippets, or create a new SnippetApiFunctionView.")
@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def snippet_list_api_view(request):
    """
    List all code snippets, or create a new SnippetApiFunctionView.
    """
    data = {}
    if request.method == "GET":
        snippets = SnippetApiFunctionView.objects.all()
        serializer = SimpleApiFunctionViewSnippetSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        data['title'] = request.query_params.get('title')
        data['code'] = request.query_params.get('code')
        data['linenos'] = request.query_params.get('linenos')
        data['language'] = request.query_params.get('language')
        data['style'] = request.query_params.get('style')
        serializer = SimpleApiFunctionViewSnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='PUT',
                     manual_parameters=[title, code, linenos, language, style],
                     responses={status.HTTP_200_OK: SimpleApiFunctionViewSnippetSerializer,
                                status.HTTP_400_BAD_REQUEST: "Bad Request"},
                     operation_description="Retrieve, update or delete a code SnippetApiFunctionView.",
                     operation_summary="Summary of List all code snippets, or create a new SnippetApiFunctionView.")
@swagger_auto_schema(method='GET',
                     operation_description="Retrieve a code SnippetApiFunctionView.",
                     responses={status.HTTP_200_OK: SimpleApiFunctionViewSnippetSerializer,
                                status.HTTP_404_NOT_FOUND: "Not Found"},
                     operation_summary="Retrieve a code SnippetApiFunctionView."
                     )
@swagger_auto_schema(method='DELETE', responses={status.HTTP_204_NO_CONTENT: SimpleApiFunctionViewSnippetSerializer,
                                                 status.HTTP_404_NOT_FOUND: "Not Found",
                                                 status.HTTP_400_BAD_REQUEST: "Bad Request"},
                     operation_description="Delete a code SnippetApiFunctionView.",
                     operation_summary="Delete a code SnippetApiFunctionView."
                     )
@swagger_auto_schema(method='PATCH', responses={status.HTTP_206_PARTIAL_CONTENT: SimpleApiFunctionViewSnippetSerializer,
                                                status.HTTP_404_NOT_FOUND: "Not Found",
                                                status.HTTP_400_BAD_REQUEST: "Bad Request"},
                     request_body=SimpleApiFunctionViewSnippetSerializer,
                     operation_description="Patch a code SnippetApiFunctionView.",
                     operation_summary="Patch a code SnippetApiFunctionView."
                     )
@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def snippet_detail_api_view(request, pk):
    """
    Retrieve, update, patch or delete a code SnippetApiFunctionView.
    """
    data = {}
    try:
        snippets = SnippetApiFunctionView.objects.get(pk=pk)
    except SnippetApiFunctionView.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SimpleApiFunctionViewSnippetSerializer(snippets)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        data['title'] = request.query_params.get('title') or ""
        data['code'] = request.query_params.get('code') or ""
        data['linenos'] = request.query_params.get('linenos') or ""
        data['language'] = request.query_params.get('language') or ""
        data['style'] = request.query_params.get('style') or ""
        serializer = SimpleApiFunctionViewSnippetSerializer(snippets, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        data['title'] = request.query_params.get('title') or ""
        data['code'] = request.query_params.get('code') or ""
        data['linenos'] = request.query_params.get('linenos') or ""
        data['language'] = request.query_params.get('language') or ""
        data['style'] = request.query_params.get('style') or ""
        serializer = SimpleApiFunctionViewSnippetSerializer(snippets, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        snippets.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
