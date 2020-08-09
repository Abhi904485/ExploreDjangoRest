from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import SimpleApiSnippetSerializer
from .models import Snippet
from rest_framework import status


@csrf_exempt
def snippet_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    :param format:
    :param request:
    :return:
    """
    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SimpleApiSnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = SimpleApiSnippetSerializer(data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    :param format:
    :param request:
    :param pk: int
    :return:
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = SimpleApiSnippetSerializer(snippet)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = SimpleApiSnippetSerializer(snippet, data=JSONParser().parse(request))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
