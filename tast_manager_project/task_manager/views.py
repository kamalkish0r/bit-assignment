from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User  
from .permissions import IsOwner

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(f'\n\ncreated by : {obj.user} accessed by : {request.user}')
        return obj.user == request.user

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        print(f'\n\n{self.request.user} is requesting tasks.. TaskListCreateView.get_queryset')
        return Task.objects.filter(user=self.request.user)  # Filter tasks by the requesting user

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner] 
    authentication_classes = [TokenAuthentication]
    serializer_class = TaskSerializer

    def get_queryset(self):
        print(f'\n\n{self.request.user} is requesting tasks.. TaskDetailView.get_queryset')
        try:
            queryset = Task.objects.filter(user=self.request.user)  # Filter tasks by the requesting user
            print(f'\n\nqueryset : {queryset}')
            return queryset
        except Task.DoesNotExist:
            raise NotFound('Task not found')
        except Exception as e:
            print(f'\n\nError in TaskDetailView.get_queryset : {e}')

    def get_object(self):
        try:
            task = super().get_object()
            if task.user != self.request.user:
                raise PermissionDenied('You do not have permission to access this task.')
            return task
        except Task.DoesNotExist:
            raise NotFound('Task not found')
    

class CustomAuthTokenLogin(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })
    

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()  
    permission_classes = ()
    serializer_class = UserSerializer
    model = User
    fields = ('username', 'password')

    def perform_create(self, serializer):
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        data = {'token': token.key}
        return Response(data)