from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True)
    password2 = serializers.CharField(write_only=True,required=True)

    class Meta:
        model = CustomUser
        fields = ['id',"first_name","last_name","username","email",'role','password','password2']
        read_only_fields =['id']
    def validate(self,data):
        password = data.get("password")
        password2 = data.get("password2")
        email = data.get("email")
        role = data.get("role")
        if len(password) < 8:
            raise serializers.ValidationError({"password": "Password must be at least 8 characters."})
        if password != password2:
            raise serializers.ValidationError({"password2": "Passwords do not match."})

        if not email.endswith("@gmail.com"):
            raise serializers.ValidationError({"email": "Invalid Gmail"})
        if role not in [r[0] for r in CustomUser.ROLES]:
            raise serializers.ValidationError({"role": "Invalid user role."})
        return data
    
    def create(self,validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        user.password= make_password(password)
        user.save()
        return user
    def update(self, instance, validated_data):
        validated_data.pop("password2",None)
        password=validated_data.pop("password",None)
        for attr, value in validated_data.items():
            setattr(instance,attr,value)
        if password:
            instance.password = make_password(password)
        instance.save()
        return instance
        
        
