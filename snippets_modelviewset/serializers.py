from drf_yasg import openapi

from .models import SnippetModelViewSet, LANGUAGE_CHOICES, STYLE_CHOICES

from rest_framework import serializers


class SimpleModelViewSetSnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(allow_blank=True, max_length=100, required=True)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default="python")
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        :param validated_data:dict
        :return:
        """
        return SnippetModelViewSet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
         Update and return an existing `Snippet` instance, given the validated data.
        :param instance:
        :param validated_data:
        :return:
        """
        instance.title = validated_data.get("title", instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
