from rest_framework import serializers

from .models import Link


class CodeSerializer(serializers.ModelSerializer):
    code = serializers.CharField()

    class Meta:
        fields = ('code',)
        model = Link
