from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='snippetList'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippetDetail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippetHighlight'),
    path('users/', views.UserList.as_view(), name='userList'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='userDetail'),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.apiIndex),
]

urlpatterns = format_suffix_patterns(urlpatterns)