from rest_framework import serializers

from .models import Post, PostHistory


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "name",
            "description",
            "keywords",
            "url",
            "created_at",
            "created_by_ip",
        ]
        read_only_fields = ["created_at", "created_by_ip"]


class PostHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostHistory
        fields = ["id", "post", "action", "timestamp", "ip_address", "data_snapshot"]
        read_only_fields = ["timestamp", "ip_address"]
