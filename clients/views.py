from rest_framework import viewsets, filters, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Client
from .serializers import ClientSerializer
from .permissions import IsOwner
from .pagination import ClientPagination


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'first_name',
        'last_name',
        'email'
    ]
    ordering_fields = ['created_at', 'first_name', 'last_name']
    ordering = ['-created_at']
    pagination_class = ClientPagination

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
