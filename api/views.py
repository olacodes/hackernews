from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, permissions, status, viewsets

from news.models.news import News
from utils.response import Response

from .serializers import NewsSerializer


class NewsViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [permissions.AllowAny]
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    #  Allow filtering of certain fields, use filter_fields properties.
    filter_fields = ("type",)
    #  use custom filters
    search_fields = ("title", "text")
    ordering_fields = ("time",)
    ordering = ("-time",)

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if not instance.is_hknews:
            self.perform_update(serializer)
            return Response(data=serializer.data)
        return Response(
            errors=dict(invalid="You are not allow to update this content"),
            status=status.HTTP_400_BAD_REQUEST,
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.is_hknews:
            self.perform_destroy(instance)
            return Response(
                data=dict(success="Item successfully deleted"),
                status=status.HTTP_204_NO_CONTENT,
            )
        return Response(
            errors=dict(invalid="You are not allow to delete this content"),
            status=status.HTTP_400_BAD_REQUEST,
        )

    def perform_destroy(self, instance):
        instance.delete()
