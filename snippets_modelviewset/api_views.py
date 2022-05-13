from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import SimpleModelViewSetSnippetSerializer

from .models import SnippetModelViewSet, STYLE_CHOICES, LANGUAGE_CHOICES

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


class SnippetList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = SnippetModelViewSet.objects.all()
    serializer_class = SimpleModelViewSetSnippetSerializer

    @swagger_auto_schema(operation_description="Retrieve all code ModelViewsets.",
                         responses={status.HTTP_200_OK: SimpleModelViewSetSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Retrieve all code SnippetSimpleApiUsingModelViewsets",
                         )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create code using ModelViewsets.",
                         responses={status.HTTP_200_OK: SimpleModelViewSetSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Create code using ModelViewsets",
                         )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Get code Detail using ModelViewsets",
                         responses={status.HTTP_200_OK: SimpleModelViewSetSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Get code Detail using ModelViewsets",
                         )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update code Detail using ModelViewsets",
                         request_body=SimpleModelViewSetSnippetSerializer,
                         responses={status.HTTP_200_OK: SimpleModelViewSetSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Update code Detail using ModelViewsets",
                         )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Patch code Detail using ModelViewsets",
                         request_body=SimpleModelViewSetSnippetSerializer,
                         responses={status.HTTP_200_OK: SimpleModelViewSetSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Patch code Detail using ModelViewsets",
                         )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete Code using ModelViewsets",
                         responses={status.HTTP_200_OK: SimpleModelViewSetSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Delete Code using ModelViewsets",
                         )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
