from django.urls import path
from home.views import HomeView, MovementDetail, NewsList, NewDetail, ArticleApi

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("pages/<slug:slug>/", MovementDetail.as_view(), name="custom_templates"),
    path("api/pages", ArticleApi.as_view(), name="custom_templates"),
    path("news/", NewsList.as_view(), name="news"),
    path("news/<int:pk>", NewDetail.as_view(), name="new"),
]
