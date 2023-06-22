from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewset, PostViewSet

app_name = 'api'
VERSION = 'v1'

router_1 = DefaultRouter()
router_1.register('posts', PostViewSet, basename='posts')
router_1.register('groups', GroupViewset, basename='groups')
router_1.register('follow', FollowViewSet, basename='follows')
router_1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)

urlpatterns = [
    path(f'{VERSION}/', include((router_1.urls))),
    path(f'{VERSION}/', include('djoser.urls.jwt')),
]
