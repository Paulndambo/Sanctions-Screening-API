from rest_framework import serializers
from .models import SanctionList

class SanctionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanctionList
        fields = "__all__"