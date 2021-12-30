from time import time

from django.shortcuts import render

from ..models.news import News


def home(request):
    starting_time = time()
    news = News.objects.all().order_by("-time")
    total_time = time() - starting_time

    return render(
        request,
        "news/home.html",
        {"data": news, "time": total_time},
    )
