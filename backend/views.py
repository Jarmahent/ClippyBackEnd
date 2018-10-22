from django.shortcuts import render
from rest_framework import viewsets
from backend.serializers import CopyData, CopyDataSerializer
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core import serializers
from json import loads



class CopyDataViewSet(viewsets.ModelViewSet):
    queryset = CopyData.objects.all()
    serializer_class = CopyDataSerializer



@api_view(['GET', 'POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticatedOrReadOnly,))
def CopyDataView(request):
    if request.method == 'GET':
        query = CopyData.objects.all().filter(user_id=request.user.id)
        print(request.user.id)
        serializer = CopyDataSerializer(query, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        mutable_dict = request.POST.copy()
        mutable_dict['user'] = request.user.id
        serializer = CopyDataSerializer(data=mutable_dict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required
@api_view(['GET'])
def GenerateToken(request):
    current_user = request.user
    try:
        generated_token = Token.objects.create(user=current_user)
        return JsonResponse({
            'auth_token': f'{generated_token.key}'
        })
    except Exception as e:
        existing_token = Token.objects.all().filter(user_id=current_user.id)
        parsed_token = loads(serializers.serialize("json", existing_token))
        key = parsed_token[0]["pk"]
        return Response({

            "error": f"{e}",
            "description": "This client probably already has a generated token...",
            "client_name": request.user.username,
            "pregenerated_token": f"{key}"
        })
