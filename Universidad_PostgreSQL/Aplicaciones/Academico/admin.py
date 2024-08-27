from django.contrib import admin
from .models import Curso, Docente

# Register your models here.
admin.site.register(Docente)


#admin.site.register(Curso)
   #clase herededa cursoadmin para personalizar panel de administración:
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    #list_display = ('id', 'nombre', 'creditos') #MUESTRA LAS COLUMNAS ID, NOMBRE Y CREDITOS
    # ordering = ('creditos', 'nombre') #ORDENA POR CREDITOS Y NOMBRE
    #search_fields = ('nombre', 'creditos') #HABILITA DONDE ESTABA ACTION , UN SEARCH PARA BUSCAR POR NOMBRE O CREDITOS
    # list_editable = ('nombre',) #PERMITE EDITAR SOLO LOS NOMBRES
    list_filter = ('creditos',) #APARECE LA OPCION DE FILTRAR POR CREDITOS
    #list_per_page = 3 # Paginación #MUESTRA SOLAMENTE TRES REGISTROS POR PAGINA
    # exclude = ('creditos',) #EXCLUYE CREDITOS, NO LOS MUESTRA

    #Este es para agregar opciones avanzadas para el campo creditos, en lugar de mostrarlo directo aparece como opciones avanzadas
    """
        fieldsets = (
        (None, {
            'fields': ('nombre',)
        }),
        ('Advanced options', {
            'classes': ('collapse', 'wide', 'extrapretty'),
            'fields': ('creditos',)
        })
    )
        """
    """def datos(self, obj):
        return obj.nombre.upper() # para ver los nombres en mayuscula

    datos.short_description = "CURSO (MAYÚS)"# para cambiar nombre de la columna nombre
    datos.empty_value_display = "???" # si llegara a existir campo vacio que se vea con tres signos de interrogación
    datos.admin_order_field = 'nombre' ## al hacer click en nombre se ordene alfabeticamente
    """
