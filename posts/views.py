from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post

class PostList(ListCreateAPIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # queryset = Post.objects.all()
    # serializer_class = PostSerializer
    pass

class PostDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthorOrReadOnly,)
    # queryset = Post.objects.all()
    # serializer_class = PostSerializer
    pass
