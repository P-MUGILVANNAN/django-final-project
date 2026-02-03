from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Book

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id","username","email","password"]

    def create(self,validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        
        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect Password")
        
        refresh = RefreshToken.for_user(user)

        return{
            "message":"Login Successful",
            "username":user.username,
            "email":user.email,
            "access":str(refresh.access_token),
            "refresh":str(refresh)
        }
    

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"