from django.urls import path, re_path

from .views.news import NewsDetailView, NewsListView, lazy_load_news

urlpatterns = [
    path("", NewsListView.as_view(), name="home"),
    re_path(r"^lazy_load_news/$", lazy_load_news, name="lazy_load_news"),
    path("<int:pk>/", NewsDetailView.as_view(), name="news-detail"),
]
