from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializers import MemberSerializer, MemberListSerializer
from .models import Member

# Create your views here.
@api_view(['GET'])
def members_list(request):
    members = Member.objects.all()
    serializer = MemberListSerializer(members, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_member(request):
    serializer = MemberSerializer(data=request.data)  # data=  으로 작성
    if serializer.is_valid(raise_exception=True):  # raise_exeption=True 해야, 에러 관련 응답 JSON이 나온다.
        serializer.save()
    return Response(serializer.data)