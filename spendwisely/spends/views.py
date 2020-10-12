from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from spends.models import SpendCategory
from spends.serializers import SpendCategorySerializer


class SpendCategoryViewSet(ModelViewSet):
    queryset = SpendCategory.objects.all()
    serializer_class = SpendCategorySerializer

