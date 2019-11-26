from rest_framework import serializers

from api.article.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        read_only_fields = [
            'created_at',
            'edited_at'
        ]
        fields = [
            'author',
            'title',
            'body',
        ] + read_only_fields
