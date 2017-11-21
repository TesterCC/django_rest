#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group

from rest_framework import viewsets

from api.serializers import UserSerializer, GroupSerializer


# config swagger

from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas


@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Python Swagger API')
    return response.Response(generator.get_schema(request=request))

# end config swagger


# ViewSets定义视图的展现形式
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


