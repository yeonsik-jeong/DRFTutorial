from django.urls import path
from authentication import views

app_name = 'authentication'

urlpatterns = [
    path('signup/', views.Signup.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
] 