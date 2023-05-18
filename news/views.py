from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from .models import News, Comment, Status, NewsStatus, CommentStatus
from .serializers import NewsSerializer, CommentSerializer, StatusSerializer,\
    NewsStatusSerializer, CommentStatusSerializer
from .permissions import IsAuthorOrIsAuthenticated, IsAdmin
from .paginations import NewsNumberPagination


class NewsListCreateAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsNumberPagination
    permission_classes = [IsAuthorOrIsAuthenticated, ]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', ]
    ordering_fields = ['created', ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.author.user)


class NewsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthorOrIsAuthenticated, ]


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthorOrIsAuthenticated, ]

    def get_queryset(self):
        return super().get_queryset().filter(news_id=self.kwargs['news_id'])


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrIsAuthenticated, ]

    def get_queryset(self):
        return super().get_queryset().filter(news_id=self.kwargs['news_id'])


class StatusListCreateAPIView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAdmin, ]


class StatusRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAdmin, ]


class NewsStatusListAPIView(generics.ListAPIView):
    queryset = NewsStatus.objects.all()
    serializer_class = NewsStatusSerializer
    permission_classes = [IsAuthorOrIsAuthenticated, ]

    def get(self, request, **kwargs):
        if request.method == 'GET':
            if self.request.status == self.request.data:
                return Response('You already added status')
            else:
                return Response('Status added')


class CommentStatusListCreateAPIView(generics.ListAPIView):
    queryset = CommentStatus.objects.all()
    serializer_class = CommentStatusSerializer
    permission_classes = [IsAuthorOrIsAuthenticated, ]

    def get(self, request, **kwargs):
        if request.method == 'GET':
            if self.request.status == self.request.data:
                return Response('You already added status')
            else:
                return Response('Status added')


