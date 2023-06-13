from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import SanctionList
from .serializers import SanctionListSerializer
# Create your views here.
class SanctionListViewSet(ModelViewSet):
    queryset = SanctionList.objects.all()
    serializer_class = SanctionListSerializer