from django.contrib import admin
from DP.models import dp_diario, usuario, paciente, examenLaboratorio

# Register your models here.

class pacienteAdmin(admin.ModelAdmin):
    list_display = ('tipo_doc', 'num_doc', 'ape_pat', 'ape_mat', 'nombres', 'fecha_nac', 'sexo', 'estado','tipoTrata')    

class usuarioAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'nombre_user', 'pass_user', 'estado', 'primSesion')

class dp_diarioAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'ultrafil', 'pres_art', 'pres_art_diast', 'peso', 'user_reg', 'fecha_reg', 'user_mod', 'fecha_mod', 'user_eli', 'fecha_eli')

class examenLaboratorioAdm(admin.ModelAdmin):
    list_display = ('centro','periodo','area','servicio','actividad','subactividad','acto_medico','fecha_atencion','fecha_solicitud','fecha_cita','fecha_resultado','num_solicitud','dni_solicita','prof_solicita','tipexamen','arealab','sede','examen','descexamen','dni_profesional','profesional','dni_paciente','h_c','paciente','telefonos','annos','meses','dias','sexo','tipo_paciente','cas_adscripcion','diagnostico','des_diagn','tip_diagn','resultado','categoria_resul','fecha_registro','usuario_registro','informe_resultado','orden_plantilla','desc_plantilla','valor_resultado','unidadvalor','observresultado','usario_modifica','fecha_modifica','centro_origen_solicitud','codresul_covid','resultado_covid','hora_registro','autogenerado','desc_topico')

admin.site.register(paciente, pacienteAdmin)
admin.site.register(usuario, usuarioAdmin)
admin.site.register(dp_diario, dp_diarioAdmin)
admin.site.register(examenLaboratorio, examenLaboratorioAdm)