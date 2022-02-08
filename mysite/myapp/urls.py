from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail')
    path('<slug:slug>/', views.post_detail, name='post_detail')
]
