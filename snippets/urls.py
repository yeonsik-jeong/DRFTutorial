from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from snippets import views

app_name = 'snippets'

""" 
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 
"""
 
snippet_list = views.SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = views.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = views.SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = views.UserViewSet.as_view({
    'get': 'list'
})

user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('snippets/', snippet_list, name='snippetList'),
    path('snippets/<int:pk>/', snippet_detail, name='snippetDetail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippetHighlight'),
    path('users/', user_list, name='userList'),
    path('users/<int:pk>/', user_detail, name='userDetail'),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.apiIndex),
] 

"""
urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='snippetList'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippetDetail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippetHighlight'),
    path('users/', views.UserList.as_view(), name='userList'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='userDetail'),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.apiIndex),
]
"""

urlpatterns = format_suffix_patterns(urlpatterns)