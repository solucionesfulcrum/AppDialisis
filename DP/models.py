from django.db import models

# Create your models here.
class paciente(models.Model):
    tipo_doc = models.CharField(max_length=30)
    num_doc = models.CharField(max_length=15)
    ape_pat = models.CharField(max_length=30)
    ape_mat = models.CharField(max_length=30)
    nombres = models.CharField(max_length=40)
    fecha_nac = models.DateField()
    sexo = models.CharField(max_length=10)
    estado = models.CharField(max_length=5, default=1)
    tipoTrata = models.CharField(max_length=5)
    

    def __str__(self):
        return self.nombres + self.ape_pat + self.ape_mat

class usuario(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    nombre_user = models.CharField(max_length=40)
    pass_user = models.CharField(max_length=256)
    estado = models.CharField(max_length=5, default=1)
    primSesion = models.CharField(max_length=5)

    def __str__(self):
        return self.nombre_user

class dp_diario(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    ultrafil = models.IntegerField()
    pres_art = models.IntegerField()
    pres_art_diast = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    user_reg = models.CharField(max_length=40, default='USER')
    fecha_reg = models.DateField(auto_now_add=True)
    user_mod = models.CharField(max_length=40, default='USER')
    fecha_mod = models.DateField(auto_now=True)
    user_eli = models.CharField(max_length=40, default='USER')
    fecha_eli = models.DateField(auto_now=True)


class examenLaboratorio(models.Model):
    centro = models.CharField(max_length=4, null=True, blank=True)
    periodo = models.CharField(max_length=6, null=True, blank=True)    
    area = models.CharField(max_length=40, null=True, blank=True)  
    servicio = models.CharField(max_length=20, null=True, blank=True)  
    actividad = models.CharField(max_length=40, null=True, blank=True)  
    subactividad = models.CharField(max_length=40, null=True, blank=True)  
    acto_medico = models.CharField(max_length=10, null=True, blank=True)  
    fecha_atencion = models.CharField(max_length=10, null=True, blank=True)  
    fecha_solicitud = models.CharField(max_length=10, null=True, blank=True)  
    fecha_cita = models.CharField(max_length=10, null=True, blank=True)  
    fecha_resultado = models.CharField(max_length=10, null=True, blank=True)  
    num_solicitud = models.CharField(max_length=10, null=True, blank=True)  
    dni_solicita  = models.CharField(max_length=10, null=True, blank=True)
    prof_solicita = models.CharField(max_length=100, null=True, blank=True)
    tipexamen = models.CharField(max_length=10, null=True, blank=True)
    arealab = models.CharField(max_length=20, null=True, blank=True)
    sede = models.CharField(max_length=20, null=True, blank=True)
    examen = models.CharField(max_length=10, null=True, blank=True)
    descexamen = models.CharField(max_length=200, null=True, blank=True)
    dni_profesional = models.CharField(max_length=10, null=True, blank=True)
    profesional = models.CharField(max_length=100, null=True, blank=True)
    dni_paciente = models.CharField(max_length=15, null=True, blank=True)
    h_c = models.CharField(max_length=10, null=True, blank=True)
    paciente = models.CharField(max_length=100, null=True, blank=True)
    telefonos = models.CharField(max_length=50, null=True, blank=True)
    annos = models.CharField(max_length=3, null=True, blank=True)
    meses = models.CharField(max_length=2, null=True, blank=True)
    dias = models.CharField(max_length=2, null=True, blank=True)
    sexo = models.CharField(max_length=6, null=True, blank=True)
    tipo_paciente = models.CharField(max_length=20, null=True, blank=True)
    cas_adscripcion = models.CharField(max_length=6, null=True, blank=True)
    diagnostico = models.CharField(max_length=10, null=True, blank=True)
    des_diagn = models.CharField(max_length=100, null=True, blank=True)
    tip_diagn = models.CharField(max_length=10, null=True, blank=True)
    resultado = models.CharField(max_length=20, null=True, blank=True)
    categoria_resul = models.CharField(max_length=50, null=True, blank=True)
    fecha_registro = models.CharField(max_length=10, null=True, blank=True)  
    usuario_registro = models.CharField(max_length=20, null=True, blank=True)
    informe_resultado = models.CharField(max_length=200, null=True, blank=True)
    orden_plantilla = models.CharField(max_length=6, null=True, blank=True)
    desc_plantilla = models.CharField(max_length=40, null=True, blank=True)
    valor_resultado = models.CharField(max_length=20, null=True, blank=True)
    unidadvalor = models.CharField(max_length=40, null=True, blank=True)
    observresultado = models.CharField(max_length=40, null=True, blank=True)
    usario_modifica = models.CharField(max_length=20, null=True, blank=True)
    fecha_modifica = models.CharField(max_length=10, null=True, blank=True)  
    centro_origen_solicitud = models.CharField(max_length=4, null=True, blank=True)
    codresul_covid = models.CharField(max_length=6, null=True, blank=True)
    resultado_covid = models.CharField(max_length=40, null=True, blank=True)
    hora_registro = models.CharField(max_length=20, null=True, blank=True)
    autogenerado = models.CharField(max_length=20, null=True, blank=True)
    desc_topico = models.CharField(max_length=40, null=True, blank=True)

class archivo(models.Model):
     descripcion = models.CharField(max_length=30, null=True, blank=True)
     documento = models.FileField(upload_to='archivos/')