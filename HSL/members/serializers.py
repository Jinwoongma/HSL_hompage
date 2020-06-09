from rest_framework import serializers
from .models import Member

class MemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(use_url=True)
    class Meta:
        model = Member
        fields = ('name', 'photo', 'course', 'work_space', 'is_graduate')
        read_only_fields = ['id', ]