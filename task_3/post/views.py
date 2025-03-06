from rest_framework import permissions, viewsets
from rest_framework.exceptions import PermissionDenied

from .models import Post, PostHistory
from .serializers import PostHistorySerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(created_by_ip=self.request.META.get("REMOTE_ADDR"))
        PostHistory.objects.create(
            post=serializer.instance,
            action=PostHistory.Action.CREATE,
            ip_address=self.request.META.get("REMOTE_ADDR"),
            data_snapshot=PostSerializer(serializer.instance).data,
        )

    def perform_update(self, serializer):
        if serializer.instance.created_by_ip != self.request.META.get("REMOTE_ADDR"):
            raise PermissionDenied("You can only modify your own posts.")

        serializer.save()
        PostHistory.objects.create(
            post=serializer.instance,
            action=PostHistory.Action.UPDATE,
            ip_address=self.request.META.get("REMOTE_ADDR"),
            data_snapshot=PostSerializer(serializer.instance).data,
        )

    def perform_destroy(self, instance):
        if instance.created_by_ip != self.request.META.get("REMOTE_ADDR"):
            raise PermissionDenied("You can only delete your own posts.")

        data_snapshot = PostSerializer(instance).data
        instance.delete()
        PostHistory.objects.create(
            post_id=data_snapshot["id"],
            action=PostHistory.Action.DELETE,
            ip_address=self.request.META.get("REMOTE_ADDR"),
            data_snapshot=data_snapshot,
        )


class PostHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PostHistory.objects.all()
    serializer_class = PostHistorySerializer
