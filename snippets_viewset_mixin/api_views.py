from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import SimpleMixinViewSetSnippetSerializer

from .models import SnippetApiMixinViewSet, STYLE_CHOICES, LANGUAGE_CHOICES

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


class SnippetList(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = SnippetApiMixinViewSet.objects.all()
    serializer_class = SimpleMixinViewSetSnippetSerializer

    @swagger_auto_schema(operation_description="Retrieve all code MixinViewsets.",
                         responses={status.HTTP_200_OK: SimpleMixinViewSetSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Retrieve all code SnippetSimpleApiUsingMixinViewsets",
                         )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create code using MixinViewsets.",
                         responses={status.HTTP_200_OK: SimpleMixinViewSetSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Create code using MixinViewsets",
                         )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Get code Detail using MixinViewsets",
                         responses={status.HTTP_200_OK: SimpleMixinViewSetSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Get code Detail using MixinViewsets",
                         )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update code Detail using MixinViewsets",
                         request_body=SimpleMixinViewSetSnippetSerializer,
                         responses={status.HTTP_200_OK: SimpleMixinViewSetSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Update code Detail using MixinViewsets",
                         )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Patch code Detail using MixinViewsets",
                         request_body=SimpleMixinViewSetSnippetSerializer,
                         responses={status.HTTP_200_OK: SimpleMixinViewSetSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Patch code Detail using MixinViewsets",
                         )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete Code using MixinViewsets",
                         responses={status.HTTP_200_OK: SimpleMixinViewSetSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Delete Code using MixinViewsets",
                         )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
