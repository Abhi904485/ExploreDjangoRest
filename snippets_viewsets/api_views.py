from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import SimpleViewSetSnippetSerializer

from .models import SnippetViewSet, STYLE_CHOICES, LANGUAGE_CHOICES

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


class SnippetList(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = SnippetViewSet.objects.all()

    @swagger_auto_schema(operation_description="Retrieve all code Viewsets.",
                         responses={status.HTTP_200_OK: SimpleViewSetSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Retrieve all code Viewsets",
                         )
    def list(self, request, format=None):
        queryset = SnippetViewSet.objects.all()
        serializer = SimpleViewSetSnippetSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_description="Create code using Viewsets.",
                         manual_parameters=[title, code, linenos, language, style],
                         responses={status.HTTP_200_OK: SimpleViewSetSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Create code using Viewsets",
                         )
    def create(self, request, format=None):
        serializer = SimpleViewSetSnippetSerializer(data=request.query_params)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type='Application/json')

    @swagger_auto_schema(operation_description="Get code Detail using Viewsets",
                         responses={status.HTTP_200_OK: SimpleViewSetSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Get code Detail using Viewsets",
                         )
    def retrieve(self, request, pk=None, format=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = SimpleViewSetSnippetSerializer(item)
        return Response(serializer.data)

    @swagger_auto_schema(operation_description="Update code Detail using Viewsets",
                         request_body=SimpleViewSetSnippetSerializer,
                         responses={status.HTTP_200_OK: SimpleViewSetSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Update code Detail using Viewsets",
                         )
    def update(self, request, pk=None, format=None):
        serializer = SimpleViewSetSnippetSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type='Application/json')

    @swagger_auto_schema(operation_description="Patch code Detail using Viewsets",
                         request_body=SimpleViewSetSnippetSerializer,
                         responses={status.HTTP_200_OK: SimpleViewSetSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Patch code Detail using Viewsets",
                         )
    def partial_update(self, request, pk=None):
        serializer = SimpleViewSetSnippetSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST, content_type='Application/json')

    @swagger_auto_schema(operation_description="Delete Code using Viewsets",
                         responses={status.HTTP_200_OK: SimpleViewSetSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Delete Code using Viewsets",
                         )
    def destroy(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        if item:
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT, content_type='application/json')
        return Response(data={pk: "Item with primary key {} is not available".format(pk)}, status=status.HTTP_404_NOT_FOUND, content_type='Application/json')
