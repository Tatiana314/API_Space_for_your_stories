from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated


from posts.models import Group, Post
from api.serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
)
from api.permissions import AuthorOrAuthorization


class GroupViewset(viewsets.ReadOnlyModelViewSet):
    """Получаем список или одну группу по id."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AuthorOrAuthorization,)


class PostViewSet(viewsets.ModelViewSet):
    """Получаем/изменяем/создаем посты."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrAuthorization,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Получаем/изменяем/создаем комментарии."""
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrAuthorization,)

    def post_object(self):
        return get_object_or_404(Post, id=self.kwargs.get("post_id"))

    def get_queryset(self):
        return self.post_object().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.post_object())


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Получаем/создаем подписку пользователя, сделавшего запрос."""
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
