# users/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    # Campo extra para que el formulario pida contraseña
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'password',
        ]
    
        extra_kwargs = {
        'password': {'write_only': True, 'style': {'input_type': 'password'}}
    }

    def create(self, validated_data):
        # Usamos create_user para que la contraseña se guarde encriptada
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data, password=password)
        return user

    def update(self, instance, validated_data):
        # Si viene contraseña, la actualizamos con set_password
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

    

