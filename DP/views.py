from django.contrib.auth.models import User, Group
from DP.models import dp_diario, paciente, usuario, examenLaboratorio
from rest_framework import viewsets, permissions, filters
from DP.serializers import Dp_DiarioSerializer, PacienteSerializer, UsuarioSerializer, examenLaboratorioSerializer

# Create your views here.
class PacienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombres']

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre_user']

class Dp_DiarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = dp_diario.objects.all()
    serializer_class = Dp_DiarioSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['ultrafil']

class examenLaboratorioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = examenLaboratorio.objects.all()
    serializer_class = examenLaboratorioSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['centro']
