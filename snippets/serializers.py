from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']

class UserSerializer(serializers.ModelSerializer):
    snippetsByOwner = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())  # Should be the same as related_name

    class Meta:
        model = User
        fields = ['id', 'username', 'snippetsByOwner']