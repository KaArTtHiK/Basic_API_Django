
from django.urls import path
from .views import article_list,detail_article
from basic_api_app import views

urlpatterns = [
    path('article/',article_list ),
    path('detail/<int:pk>/',detail_article),
]