from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from api.views import NewsViewSet
from hackernews.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register(r"news", NewsViewSet, basename="news")


app_name = "api"
urlpatterns = router.urls
