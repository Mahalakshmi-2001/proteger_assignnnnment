from rest_framework import serializers
from .models import *


class AssetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assets
        fields = '__all__'