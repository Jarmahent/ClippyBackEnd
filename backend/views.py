from rest_framework import viewsets
from backend.serializers import CopyData, CopyDataSerializer
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core import serializers
from django.conf import settings
from json import loads
from django.http import QueryDict


class CopyDataViewSet(viewsets.ModelViewSet):
    queryset = CopyData.objects.all()
    serializer_class = CopyDataSerializer



@receiver(post_save, sender=settings.AUTH_USER_MODEL) # Automatically generates key
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



@api_view(['GET', 'POST'])
@authentication_classes((TokenAuthentication, SessionAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly,))
def CopyDataView(request):
    if request.method == 'GET':
        query = CopyData.objects.all().filter(user_id=request.user.id)
        print(request.user.id)
        serializer = CopyDataSerializer(query, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = loads(request.body)
        data['user'] = request.user.id
        
        qdict = QueryDict(mutable=True)
        qdict.update(data)

        serializer = CopyDataSerializer(data=qdict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required
@api_view(['GET'])
def GenerateToken(request):
    current_user = request.user
    generated_token = Token.objects.get_or_create(user=current_user)
    print(generated_token)
    return Response({
        'auth_token': f'{generated_token[0]}'
    })
