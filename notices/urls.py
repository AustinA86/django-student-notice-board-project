from django.urls import path
from . import views
from .feeds import LatestNoticesFeed

urlpatterns = [
    path('', views.NoticeListView.as_view(), name='notice-list'),
    path('notice/<int:pk>/', views.NoticeDetailView.as_view(), name='notice-detail'),
    path('notice/new/', views.NoticeCreateView.as_view(), name='notice-create'),
    path('notice/<int:pk>/update/', views.NoticeUpdateView.as_view(), name='notice-update'),
    path('notice/<int:pk>/delete/', views.NoticeDeleteView.as_view(), name='notice-delete'),
    path('session/', views.session_example_view, name='session-info'),
    path('like/<int:pk>/', views.like_notice, name='like-notice'),
    path('feed/', LatestNoticesFeed(), name='notice-feed'),
]
