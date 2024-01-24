from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Plan, Workplace


class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        fields = '__all__'

    def validate(self, attrs):
        instance = Workplace(**attrs)
        try:
            instance.clean()
        except ValidationError as error:
            raise serializers.ValidationError(error.args[0])
        else:
            return attrs


class PlanSerializer(serializers.ModelSerializer):
    workplaces = WorkplaceSerializer(many=True)
    class Meta:
        model = Plan
        fields = '__all__'
        read_only_fields = ['width', 'height']


class PlanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username']
