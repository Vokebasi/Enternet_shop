from django.shortcuts import render
from rest_framework import generics
from .serializers import CommentSerializer
from .permissions import IsCommentAuthor
from .models import Comment


class CreateCommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    serializer_classes = [IsCommentAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RetrieveEditDestroyCommentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    serializer_classes = [IsCommentAuthor]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
