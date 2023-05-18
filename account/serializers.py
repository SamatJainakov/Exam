from rest_framework import serializers

from .models import User, Author


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=30, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        print(data)
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Пароли не совпадают!')
        return data

    def validate_password(self, value):
        special_chars = '[!@#$%^&*(),.?":{}|<>]'
        if len(value) < 8:
            raise serializers.ValidationError('Пароль должен содержать как минимум 8 символов!')
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError('Пароль должен содержать хотя бы одну цифру')
        if not any(char.islower() for char in value) or not any(char.isupper() for char in value):
            raise serializers.ValidationError('Пароль должен содержать одну одну заглавную и одну прописную букву')
        if not any(char in special_chars for char in value):
            raise serializers.ValidationError(f'Пароль должен содержать хотя бы '
                                              f'один специальный символ: {special_chars}')
        return value

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        try:
            author = Author.objects.create(
                user=user
            )
        except Exception as e:
            user.delete()
            raise e
        else:
            author.username = user.username
        return author






