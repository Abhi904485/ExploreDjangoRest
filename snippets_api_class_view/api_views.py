from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import SimpleApiClassViewSnippetSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import SnippetApiClassView, LANGUAGE_CHOICES, STYLE_CHOICES
from django.shortcuts import get_object_or_404

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


class SnippetList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Retrieve all code SnippetApiClassView.",
                         responses={status.HTTP_200_OK: SimpleApiClassViewSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Retrieve all code SnippetApiClassView."
                         )
    def get(self, request, format=None):
        snippets = SnippetApiClassView.objects.all()
        serializer = SimpleApiClassViewSnippetSerializer(instance=snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(manual_parameters=[title, code, linenos, language, style],
                         responses={status.HTTP_201_CREATED: SimpleApiClassViewSnippetSerializer,
                                    status.HTTP_400_BAD_REQUEST: "Bad Request"},
                         operation_summary="Summary of List all code snippets, or create a new SnippetApiClassView.",
                         operation_description="List all code snippets, or create a new SnippetApiClassView.")
    def post(self, request, format=None):
        data = {'title': request.query_params.get('title'), 'code': request.query_params.get('code'),
                'linenos': request.query_params.get('linenos'), 'language': request.query_params.get('language'),
                'style': request.query_params.get('style')}
        serializer = SimpleApiClassViewSnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED, content_type='application/json')
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type='Application/json')


class SnippetDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[title, code, linenos, language, style],
                         responses={status.HTTP_200_OK: SimpleApiClassViewSnippetSerializer,
                                    status.HTTP_400_BAD_REQUEST: "Bad Request"},
                         operation_description="Retrieve, update or delete a code SnippetApiClassView.",
                         operation_summary="Summary of List all code snippets, or create a new SnippetApiClassView.")
    def put(self, request, pk, format=None):
        data = {'title': request.query_params.get('title'), 'code': request.query_params.get('code'),
                'linenos': request.query_params.get('linenos'), 'language': request.query_params.get('language'),
                'style': request.query_params.get('style')}
        snippet = get_object_or_404(SnippetApiClassView, pk=pk)
        serializer = SimpleApiClassViewSnippetSerializer(instance=snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK, content_type='application/json')
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type='Application/json')

    @swagger_auto_schema(request_body=SimpleApiClassViewSnippetSerializer,
                         responses={status.HTTP_200_OK: SimpleApiClassViewSnippetSerializer,
                                    status.HTTP_400_BAD_REQUEST: "Bad Request"},
                         operation_description="Patch SnippetApiClassView.",
                         operation_summary="Patch SnippetApiClassView.")
    def patch(self, request, pk, format=None):
        data = {'title': request.query_params.get('title'), 'code': request.query_params.get('code'),
                'linenos': request.query_params.get('linenos'), 'language': request.query_params.get('language'),
                'style': request.query_params.get('style')}
        snippet = get_object_or_404(SnippetApiClassView, pk=pk)
        serializer = SimpleApiClassViewSnippetSerializer(instance=snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK, content_type='application/json')
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type='Application/json')

    @swagger_auto_schema(operation_description="Retrieve a code SnippetApiClassView.",
                         responses={status.HTTP_200_OK: SimpleApiClassViewSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Retrieve a code SnippetApiClassView."
                         )
    def get(self, request, pk, format=None):
        snippet = get_object_or_404(SnippetApiClassView, pk=pk)
        serializer = SimpleApiClassViewSnippetSerializer(instance=snippet)
        return Response(data=serializer.data, status=status.HTTP_200_OK, content_type='application/json')

    @swagger_auto_schema(responses={status.HTTP_204_NO_CONTENT: SimpleApiClassViewSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found",
                                    status.HTTP_400_BAD_REQUEST: "Bad Request"},
                         operation_description="Delete a code SnippetApiClassView.",
                         operation_summary="Delete a code SnippetApiClassView."
                         )
    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(SnippetApiClassView, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, content_type='application/json')
