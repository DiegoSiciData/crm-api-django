from rest_framework import viewsets, filters, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Client
from .serializers import ClientSerializer
from .permissions import IsOwner
from .pagination import ClientPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer


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
        return Client.objects.all()

    def perform_create(self, serializer):
        print("User >>>",self.request.user)
        serializer.save(owner=self.request.user)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Usuario creado correctamente"},
            status=status.HTTP_201_CREATED
        )

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
        })