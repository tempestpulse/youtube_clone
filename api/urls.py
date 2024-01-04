from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'api'

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('user/', views.UserListAPIView.as_view(), name='user-list'),
    path('user/<int:pk>', views.UserDetailAPIView.as_view(), name='user-detail'),
    path('channel/', views.ChannelListAPIView.as_view(), name='channel-list'),
    path('channel/<int:pk>', views.ChannelDetailAPIView.as_view(), name='channel-detail'),
    path('video/', views.VideoListAPIView.as_view(), name='video-list'),
    path('video/<int:pk>', views.VideoDetailAPIView.as_view(), name='video-detail'),
    path('tag/', views.TagListAPIView.as_view(), name='tag-list'),
    path('tag/<int:pk>', views.TagDetailAPIView.as_view(), name='tag-detail'),
    path('watch_later/', views.WatchLaterListAPIView.as_view(), name='watchlater-list'),
    path('watch_later/<int:pk>', views.WatchLaterDetailAPIView.as_view(), name='watchlater-detail'),
    path('comment/', views.CommentListAPIView.as_view(), name='comment-list'),
    path('comment/<int:pk>', views.CommentDetailAPIView.as_view(), name='comment-detail'),
])