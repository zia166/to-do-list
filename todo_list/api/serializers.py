from rest_framework import serializers
from app1.models import Task,Topic


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'