
from rest_framework import serializers


class AdditionSerializer(serializers.Serializer):
    num1 = serializers.IntegerField(required=True, error_messages={'required': 'Number is mandatory'})
    num2 = serializers.IntegerField(required=True, error_messages={'required': 'Number is mandatory'})
    num3 = serializers.IntegerField(required=True, error_messages={'required': 'Number is mandatory'})

