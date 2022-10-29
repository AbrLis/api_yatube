from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register(r'^posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='group')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
