from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from .models import SnippetMixinClassView, STYLE_CHOICES, LANGUAGE_CHOICES
from .serializers import SimpleMixinClassViewSnippetSerializer

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


class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = SnippetMixinClassView.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SimpleMixinClassViewSnippetSerializer

    @swagger_auto_schema(operation_description="Retrieve all code Using ClassMixins.",
                         responses={status.HTTP_200_OK: SimpleMixinClassViewSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Retrieve all code Using ClassMixins."
                         )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create code using ClassMixins..",
                         responses={status.HTTP_200_OK: SimpleMixinClassViewSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Create code using ClassMixins.",
                         )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetDetail(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = SnippetMixinClassView.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SimpleMixinClassViewSnippetSerializer

    @swagger_auto_schema(operation_description="Update code Detail using ClassMixins.",
                         request_body=SimpleMixinClassViewSnippetSerializer,
                         responses={status.HTTP_200_OK: SimpleMixinClassViewSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Update code Detail using ClassMixins.",
                         )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Get code Detail using ClassMixins.",
                         responses={status.HTTP_200_OK: SimpleMixinClassViewSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Get code Detail using ClassMixins.",
                         )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete Code using ClassMixins.",
                         responses={status.HTTP_200_OK: SimpleMixinClassViewSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Delete Code using ClassMixins.",
                         )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Patch code Detail using ClassMixins.",
                         request_body=SimpleMixinClassViewSnippetSerializer,
                         responses={status.HTTP_200_OK: SimpleMixinClassViewSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Patch code Detail using ClassMixins.",
                         )
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, partial=True, **kwargs)
