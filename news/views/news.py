from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.template import loader
from django.views.generic import DetailView, ListView

from ..models.comment import Comment
from ..models.news import News


class NewsListView(ListView):
    context_object_name = "news"
    template_name = "news/news_list.html"
    model = News

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        if query:
            return News.objects.filter(
                Q(text__icontains=query) | Q(title__icontains=query)
            )
        filter = self.request.GET.get("f")
        if filter:
            return News.objects.filter(type=filter).order_by("-time")[:5]
        return News.objects.all().order_by("-time")[:5]


class NewsDetailView(DetailView):
    context_object_name = "news"
    # queryset = News.objects.all()
    template_name = "news/news_detail.html"
    model = News

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = kwargs.get("object", "")
        comments = Comment.objects.filter(parent=query.news_id)
        print(query.id)
        context["comments"] = comments
        return context


def lazy_load_news(request):
    page = request.POST.get("page")
    news = News.objects.all()
    # use Django's pagination
    # https://docs.djangoproject.com/en/dev/topics/pagination/
    results_per_page = 5
    paginator = Paginator(news, results_per_page)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(2)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    # build a html posts list with the paginated posts
    news_html = loader.render_to_string("news/news_index.html", {"news": news})
    # package output data and return it as a JSON object
    output_data = {"news_html": news_html, "has_next": news.has_next()}
    return JsonResponse(output_data)
