from rest_framework import serializers
from movie_app.models import Director, Movie, Review
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "id name count_movies".split()


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "text stars movie".split()


class MovieSerializers(serializers.ModelSerializer):
    director = DirectorSerializers()
    reviews = ReviewSerializers(many=True)

    class Meta:
        model = Movie
        fields = "id title description duration director reviews rating".split()


class DirectorCountSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = "movie_count".split()

    def get_movie_count(self, movie):
        return movie.all().count()


class DirectorObjectSerializer(serializers.Serializer):
    name = serializers.CharField()


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=100)
    director_obj = serializers.IntegerField(required=False)

    @property
    def director_data_movie(self):
        dict_ = {"name": self.validated_data.get("name")}
        return dict_

    def validate_directors(self, director):
        if Review.objects.filter(id=director).count() == 0:
            raise ValidationError("director not found!! ")
        return director


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    duration = serializers.IntegerField(max_value=1000)
    director = serializers.IntegerField()

    @property
    def movie_data_director(self):
        dict_ = {
            "title": self.validated_data.get("title"),
            "description": self.validated_data.get("description", ""),
            "duration": self.validated_data.get("duration", ""),
            "director_id": self.validated_data.get("director"),
        }
        return dict_


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=100)
    movie = serializers.IntegerField(required=False, allow_null=True, default=None)
    stars = serializers.IntegerField(min_value=1, max_value=5)

    @property
    def review_data_without(self):
        dict_ = {
            "text": self.validated_data.get("text"),
            "movie": self.validated_data.get("movie"),
            "stars": self.validated_data.get("stars"),
        }
        return dict_

    def validate_movie_id(self, movie_id):
        if Review.objects.filter(id=movie_id).count() == 0:
            raise ValidationError("Movie not found")
        return movie_id



class UserValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        if User.objects.filter(username=username):
            raise ValidationError('User already exists!!!')
        return username

class UserAuthorizationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()