from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.post_list,name='post_list'),
    path('hello/', views.hello,name='hello'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
