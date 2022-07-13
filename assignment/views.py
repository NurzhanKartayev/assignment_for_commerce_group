from typing import Tuple

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from assignment.models import Employee, Boss

from assignment.serializer import EmployeeSerializer, BossSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    filter_backends: Tuple = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    permission_classes = [IsAuthenticated]
    http_method_names = ('get', 'post', 'put', 'delete', 'patch')
    pagination_class = None
    ordering_fields: Tuple = ('salary', 'position')
    search_fields = ['salary', 'position', 'boss__name']


class BossViewSet(ModelViewSet):
    serializer_class = BossSerializer
    queryset = Boss.objects.all()
    filter_backends: Tuple = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    permission_classes = [IsAuthenticated]
    http_method_names = ('get', 'post', 'put', 'delete', 'patch')
    pagination_class = None
    ordering_fields: Tuple = ('name', )

