from django.contrib.auth.models import User, Group
from .models import Post
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class BlogSerializer(serializers.ModelSerializer):
    #photo_url = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('post_id', 'username', 'title','post_type','country','state','city','date','num_of_people','theme','description','image')



    def create(self, validated_data):

        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.post_id = validated_data.get('post_id', instance.post_id)
        instance.username = validated_data.get('username', instance.username)
        instance.title = validated_data.get('title', instance.title)
        instance.country = validated_data.get('country', instance.country)
        instance.state = validated_data.get('state', instance.state)
        instance.city = validated_data.get('city', instance.city)
        instance.date = validated_data.get('date', instance.date)
        instance.num_of_people = validated_data.get('num_of_people', instance.num_of_people)
        instance.theme = validated_data.get('theme', instance.theme)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

