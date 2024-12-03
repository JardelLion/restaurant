from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Client
from .serializers import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @action(detail=False, methods=['post'], url_path='create')
    def create_client(self, request, *args, **kwargs):
        """
        Permite a criação de um cliente apenas em /api/clients/create.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def create(self, request, *args, **kwargs):
        """
        Bloqueia a criação de clientes em qualquer outra rota.
        """
        return Response(
            {"detail": "Use /api/clients/create para criar novos clientes."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
