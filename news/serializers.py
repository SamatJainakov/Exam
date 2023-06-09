from rest_framework import serializers

from .models import *


class NewsSerializer(serializers.ModelSerializer):
    get_status = serializers.ReadOnlyField()

    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = ['author', ]


class CommentSerializer(serializers.ModelSerializer):
    get_status = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'


class NewsStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsStatus
        fields = '__all__'


class CommentStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentStatus
        fields = '__all__'
