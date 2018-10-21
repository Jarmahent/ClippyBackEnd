from django.shortcuts import render
from rest_framework import viewsets
from backend.serializers import CopyData, CopyDataSerializer
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.dispatch import receiver
from django.db.models.signals import post_save



class CopyDataViewSet(viewsets.ModelViewSet):
    queryset = CopyData.objects.all()
    serializer_class = CopyDataSerializer



@api_view(['GET', 'POST'])
# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated))
def CopyDataView(request):
    if request.method == 'GET':
        query = CopyData.objects.all()
        serializer = CopyDataSerializer(query, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CopyDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
