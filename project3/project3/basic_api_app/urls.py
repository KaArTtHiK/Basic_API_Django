
from django.urls import path,include
from .views import article_list,detail_article,Article_APIView,Detail_APIView,GenericAPIView, ArticleViewSet, GenericViewSet
from rest_framework.routers import DefaultRouter
from basic_api_app import views

router = DefaultRouter()
router.register('article', GenericViewSet, basename = 'article')
urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>',include(router.urls)),
    #path('article/',article_list ),
    path('article/', Article_APIView.as_view()),
    #path('detail/<int:pk>/',detail_article),
    path('detail/<int:id>/',Detail_APIView.as_view()),
    path('generic/article/<int:id>/',GenericAPIView.as_view())
]