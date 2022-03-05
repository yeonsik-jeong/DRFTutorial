from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippetHighlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'owner', 'highlight', 'title', 'code', 'linenos', 'language', 'style']
        extra_kwargs = {  # Necessary for using programmer-wanted url name instead of default '{model_name}-detail'
            'url': {'view_name': 'snippetDetail'},
        }

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippetsByOwner = serializers.HyperlinkedRelatedField(many=True, view_name='snippetDetail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippetsByOwner']
        extra_kwargs = {
            'url': {'view_name': 'userDetail'},
        }

""" Using ModelSerializer
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
"""