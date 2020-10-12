from rest_framework.serializers import ModelSerializer

from spends.models import SpendCategory


class SpendCategorySerializer(ModelSerializer):
    class Meta:
        model = SpendCategory
        fields = "__all__"
