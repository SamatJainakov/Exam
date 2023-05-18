from django.urls import path

from . import views


urlpatterns = [
    path('', views.NewsListCreateAPIView.as_view()),
    path('<int:pk>/', views.NewsRetrieveUpdateDestroyAPIView.as_view()),
    path('<int:news_id>/comments/', views.CommentListCreateAPIView.as_view()),
    path('<int:news_id>/comments/<slug>', views.CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('statuses/', views.StatusListCreateAPIView.as_view()),
    path('statuses/<slug>', views.StatusRetrieveUpdateDestroyAPIView.as_view()),
    path('<int:news_id>/<slug>', views.NewsStatusListAPIView.as_view()),
    path('<int:news_id>/comments/<int:comment_id>/<slug>', views.CommentStatusListCreateAPIView.as_view()),
]
