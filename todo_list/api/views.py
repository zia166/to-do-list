from rest_framework.decorators import api_view
from rest_framework.views import Response
from app1.models import Task,Topic
from .serializers import TaskSerializer,TopicSerializer

@api_view(['GET'])
def getData(request):
    tasks=Task.objects.all()
    topics=Topic.objects.all()
    serializer=TaskSerializer(tasks, many=True)
    # serializer=TopicSerializer(topics,many=True)
    return Response(serializer.data)