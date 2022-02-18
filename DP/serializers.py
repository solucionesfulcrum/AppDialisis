from django.contrib.auth.models import User, Group
from DP.models import dp_diario, paciente, usuario, examenLaboratorio
from rest_framework import serializers

class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = paciente
        fields = '__all__'

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    datosPaciente = PacienteSerializer(source = "paciente", read_only=True)
    class Meta:
        model = usuario
        fields = '__all__'

class Dp_DiarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = dp_diario
        fields = '__all__'

class examenLaboratorioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = examenLaboratorio
        fields = '__all__'