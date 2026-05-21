from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, generics
from .models import Task
from .serializers import TaskSerializer, RegisterSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user).order_by('created_at')
        
        completed = self.request.query_params.get('completed')
        search = self.request.query_params.get('search')
        priority = self.request.query_params.get('priority')
        due_date = self.request.query_params.get('due_date')
        
        if completed is not None:
            if completed.lower() == 'true':
                queryset = queryset.filter(completed=True)
            elif completed.lower() == 'false':
                queryset = queryset.filter(completed=False)
                
        if search:
            queryset = queryset.filter(title__icontains=search)
            
        if priority:
            queryset = queryset.filter(priority=priority)
            
        if due_date:
            queryset = queryset.filter(due_date=due_date)
            
        return queryset
    
    @action(detail=False, methods=['get'])
    def summary(self, request):
        queryset = self.get_queryset()
        
        total_tasks = queryset.count()
        completed_tasks = queryset.filter(completed=True).count()
        pending_tasks = queryset.filter(completed=False).count()
        high_priority_tasks = queryset.filter(priority='high').count()
        
        data = {
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_task': pending_tasks,
            'high_priority_tasks': high_priority_tasks,
        }
        
        return Response(data)
    
    @action(detail=True, methods=['patch'], url_path='mark-completed')
    def mark_completed(self, request, pk=None):
        task = self.get_object()
        task.completed = True
        task.save()
        
        serializer = self.get_serializer(task)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]