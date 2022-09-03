from rest_framework import serializers
from .models import Customer, Comment
from django.utils import timezone


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


def check_date(date):
    if date > timezone.now():
        raise serializers.ValidationError("date in future")


# class CommentSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     content = serializers.CharField(max_length=200)
#     created = serializers.DateTimeField(validators=[check_date, ])
#
#     def create(self, validated_data):
#         return Comment.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.email = validated_data.get('email')
#         instance.content = validated_data.get('content')
#         instance.created = validated_data.get('created')
#         instance.save()
#         return instance

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = "__all__"
        fields = ['id', 'email', 'created', 'content']

    def validate_content(self, value):
        if "Copyright Codify" not in value:
            raise serializers.ValidationError("Comment should contain copyright")
        return value

    def validate_email(self, value):
        if not value.endswith(".kg"):
            raise serializers.ValidationError("Email should be in .kg zone")
        return value

    def validate(self, data):
        if data['email'] not in data['content']:
            raise serializers.ValidationError("Email should be in content")
        return data
