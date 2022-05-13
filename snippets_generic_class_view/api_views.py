from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import SnippetGenericClassView
from .serializers import SimpleGenericClassViewSnippetSerializer


class SnippetGenericList(ListCreateAPIView):
    queryset = SnippetGenericClassView.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SimpleGenericClassViewSnippetSerializer

    @swagger_auto_schema(operation_description="Retrieve all code Using GenericClassView.",
                         responses={status.HTTP_200_OK: SimpleGenericClassViewSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Retrieve all code Using GenericClassView.",
                         )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create code Using GenericClassView.",
                         responses={status.HTTP_200_OK: SimpleGenericClassViewSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Create code Using GenericClassView.",
                         )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class SnippetGenericDetail(ListAPIView, RetrieveUpdateDestroyAPIView):
    queryset = SnippetGenericClassView.objects.all()
    serializer_class = SimpleGenericClassViewSnippetSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Get code Using GenericClassView.",
                         responses={status.HTTP_200_OK: SimpleGenericClassViewSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Get code Using GenericClassView.",
                         )
    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update code Using GenericClassView.",
                         responses={status.HTTP_200_OK: SimpleGenericClassViewSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Update code Using GenericClassView.",
                         )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Patch code Using GenericClassView.",
                         responses={status.HTTP_200_OK: SimpleGenericClassViewSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Patch code Using GenericClassView.",
                         )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete code Using GenericClassView.",
                         responses={status.HTTP_200_OK: SimpleGenericClassViewSnippetSerializer,
                                    status.HTTP_404_NOT_FOUND: "Not Found"},
                         operation_summary="Delete code Using GenericClassView.",
                         )
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
