from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from posts.models import Group, Post
from .permissions import AuthorOnlyAccess
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthorOnlyAccess]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [AuthorOnlyAccess]

    def object_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.object_post())

    def get_queryset(self):
        return self.object_post().comments.all()
