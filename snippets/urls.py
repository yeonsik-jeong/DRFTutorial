from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.listSnippets),
    path('snippets/<int:pk>/', views.detailSnippet),
]