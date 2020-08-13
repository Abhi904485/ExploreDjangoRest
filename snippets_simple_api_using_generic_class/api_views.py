from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import SnippetApiGenericView
from .serializers import SimpleGenericApiViewSnippetSerializer


class SnippetGenericList(ListCreateAPIView):
    queryset = SnippetApiGenericView.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SimpleGenericApiViewSnippetSerializer


class SnippetGenericDetail(RetrieveUpdateDestroyAPIView):
    queryset = SnippetApiGenericView.objects.all()
    serializer_class = SimpleGenericApiViewSnippetSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]