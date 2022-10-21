from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news.models import Article, Journalist


class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    # author = JournalistSerializer(read_only=True)
    # author = serializers.StringRelatedField()

    class Meta:
        model = Article
        exclude = ("id",)
        # fields = "__all__" # we want all the fields of our model
        # fields = ("title", "description", "body") # we want to choose a couple of fields!

    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        return timesince(publication_date, now)

    def validate(self, data):
        """ check that description and title are different 
        https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
        """
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and Description must be different from one another!")
        return data

    def validate_title(self, value):
        """ check that title is at least 30 chars long
        https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
        """
        if len(value) < 30:
            raise serializers.ValidationError("The title has to be at least 30 chars long!")
        return value


class JournalistSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True,
                                                   read_only=True,
                                                   view_name="article-detail")
    # articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Journalist
        fields = "__all__"


# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         print(validated_data)
#         return Article.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', 
#                                                   instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.publication_date = validated_data.get('publication_data', 
#                                                        instance.publication_date)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         """ check that description and title are different 
#         https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
#         """
#         if data["title"] == data["description"]:
#             raise serializers.ValidationError("Title and Description must be different from one another!")
#         return data

#     def validate_title(self, value):
#         """ check that title is at least 60 chars long
#         https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
#         """
#         if len(value) < 60:
#             raise serializers.ValidationError("The title has to be at least 60 chars long!")
#         return value
