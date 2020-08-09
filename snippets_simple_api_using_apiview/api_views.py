from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import SimpleApiViewSnippetSerializer
from .models import SnippetApiView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(['GET', 'POST'])
def snippet_list_api_view(request, format=None):
    """
    List all code snippets, or create a new SnippetApiView.
    :param format:
    :param request:
    :return:
    """
    if request.method == "GET":
        snippets = SnippetApiView.objects.all()
        serializer = SimpleApiViewSnippetSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = SimpleApiViewSnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail_api_view(request, pk, format=None):
    """
    Retrieve, update or delete a code SnippetApiView.
    :param format:
    :param request:
    :param pk: int
    :return:
    """
    try:
        snippets = SnippetApiView.objects.get(pk=pk)
    except SnippetApiView.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = SimpleApiViewSnippetSerializer(snippets)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = SimpleApiViewSnippetSerializer(snippets, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        snippets.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
