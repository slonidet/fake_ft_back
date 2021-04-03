from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from users.models import User, Adapter
from users.serializers import UserSerializer, AdapterSerializer


class AdapterViewSet(viewsets.ModelViewSet):
    queryset = Adapter.objects.all()
    serializer_class = AdapterSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     # serial_number = data['serial_number']
    #     # code = data['code']
    #     # try:
    #     #     Adapter.objects.get(serial_number=serial_number, code=code)
    #     # except Adapter.DoesNotExist:
    #     #     raise ValidationError('Adapter with given serial nubmer and code was not found')
    #     return super(UserViewSet, self).create(request, *args, **kwargs)
