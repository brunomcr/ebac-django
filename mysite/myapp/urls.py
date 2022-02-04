from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.Post.as_view(), name='home')
]
