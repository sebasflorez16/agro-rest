
"""
Dentro de esta app vamos a registrar los lotes relacionado con rrhh, gestion de cultivos, las labores agricolas que debe ir relacionado con empleados,

"""
from django.db import models
from apps.base.models import BaseModel

from apps.RRHH.models import Employee
from apps.agro_supplies.models import Supply, ToolAndEquipment, Variety
from django.contrib.gis.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
STATE_CHOICE = [
    ('sowing', 'Siembra'),
    ('growth', 'Crecimiento'),
    ('flowering', 'Floracion'),
    ('fruiting', 'Fructificación'),
    ('harvest', 'Cosecha')
    
]

"""STATE_LOT_CHOICE = [
    ('active', 'Activo'),
    ('inactive', 'Inactivo'),
    ('in preparation', 'En preparaciòn'),
]"""

STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('in_progress', 'En Progreso'),
        ('completed', 'Completada'),
        ('cancelled', 'Cancelada'),
    ]


#Vamos a manejar este modelo como intermedio entre los insumos y la actividad agricola para sumarlos al cultivo y el lote y ver la cantidad de
#insumos que se usan por actividad, esto para la contalidad y reportes.


# se define las relaciones como cadena de texto ya que son dependencias circulares.
class AgricultureWork(BaseModel):
    title = models.CharField(max_length=50, verbose_name='Nombre')
    price = models.FloatField(verbose_name='Precio', help_text="Precio a pagar por labor", blank=True, null=True)
    description = models.CharField(max_length=100, verbose_name='Descripción', blank=True, null=True)
    manager = models.ForeignKey('RRHH.Employee', on_delete=models.CASCADE, verbose_name='Encargado') #Se debe especificar de esta forma la app y el modelo a cual se hace referencia por que es un reverse_lazy
    employees = models.ManyToManyField('RRHH.Employee', related_name='trabajos', verbose_name='Trabajadores', blank=True)# Si requiere mas de un empleado ademas del manager.
    insumos = models.ForeignKey('agro_supplies.Supply', on_delete=models.CASCADE, blank=True)
    tool_and_equipment = models.ForeignKey('agro_supplies.ToolAndEquipment', on_delete=models.CASCADE, verbose_name='Herramientas y Equipos', blank=True, null=True)
    work_hours = models.FloatField(verbose_name='Horas de Trabajo', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='Estado')
    work_crop = models.ForeignKey('Crop', on_delete=models.CASCADE, verbose_name='Cultivo')
    work_lot = models.ForeignKey('Lot', on_delete=models.CASCADE, verbose_name='Lote')
    historical = HistoricalRecords()

    @property
    def _history_user(self):  # Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'Trabajo Agricola'
        verbose_name_plural = 'Trabajos Agricolas'

    def __str__(self):
        return self.title


class AgriculturalApplication(BaseModel):
    activity = models.ForeignKey('AgricultureWork', on_delete=models.CASCADE, verbose_name='Actividad')
    insumo = models.ForeignKey('agro_supplies.Supply', on_delete=models.CASCADE, verbose_name='Insumo')
    quantity = models.FloatField(verbose_name='Cantidad')
    historical = HistoricalRecords()

    @property
    def _history_user(self):  # Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'Aplicación Agricola'
        verbose_name_plural = 'Aplicación Agricola'

    def __str__(self):
        return self.activity
    


class Crop(BaseModel):
    common_name = models.CharField(max_length=20, verbose_name='Nombre Común')
    scientific_name = models.CharField(max_length=30, verbose_name='Nombre Cientifico', blank=True, null=True)
    description = models.CharField(max_length=100, verbose_name='Descripción', blank=True, null=True)
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE, verbose_name='Variedad', blank=True, null=True)
    crop_cycle = models.IntegerField(verbose_name='Ciclo del cultivo en dias', blank=True, null=True)
    agriculture_work = models.ForeignKey(AgricultureWork, verbose_name='crops', on_delete=models.CASCADE, blank=True, null=True)
    planting_time = models.DateField(verbose_name='Fecha de siembra')
    harvest_time = models.DateField(verbose_name='Fecha estimada de cosecha')
    expected_performance = models.CharField(max_length=100, blank=True, null=True, verbose_name='Rendimiento Esperado')
    state = models.CharField(verbose_name='Estado', choices=STATE_CHOICE)
    observations = models.TextField(verbose_name='Observaciones', blank=True, null=True)
    historical = HistoricalRecords()


    # Maneja el historial de los usuarions que han hecho cambios
    @property
    def _history_user(self):  # Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'Cultivo'
        verbose_name_plural = 'Cultivos'

    def __str__(self):
        return self.common_name

#Modelo intermedio par manejar los estados de los lotes de como esta el lote a simple vista.
class StateLot(BaseModel):
    title = models.CharField(max_length=20, verbose_name='Titulo', help_text='Nombre el estado actual de la parcela')
    description = models.CharField(max_length=50, verbose_name='Descripciòn', blank=True, null=True)
    historical = HistoricalRecords()

    # Maneja el historial de los usuarions que han hecho cambios
    @property
    def _history_user(self):  # Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'Estado del Lote'


class Lot(BaseModel):
    name = models.CharField(max_length=20, verbose_name='Nombre', help_text='Identifica por nombre o numero del lote')
    descriptions = models.CharField(max_length=50, verbose_name='Description', help_text='Agrega caracteristicas relevantes del cultivo', blank=True, null=True)
    manager = models.ManyToManyField(Employee, verbose_name='Encargado', blank=True)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, verbose_name='Cultivo', blank=True, null=True)
    area = models.IntegerField(verbose_name='Area', help_text='Indica el nùmero de hectareas del area', blank=True, null=True)
    ubication = models.PolygonField(srid=4326, blank=True, null=True)
    soil_type = models.CharField(max_length=20, verbose_name='Tipo de suelo', help_text='Especifica si es arenoso, arcillozo, etc')
    topography = models.CharField(max_length=20, verbose_name='Topografìa', help_text='Indica si es plano, inclinido, etc')
    state = models.ForeignKey(StateLot, on_delete=models.CASCADE, verbose_name='Estado')
    agriculture_work = models.ManyToManyField(AgricultureWork, related_name='agricultural_works',verbose_name='lots', blank=True)
    historical = HistoricalRecords()

    # Maneja el historial de los usuarions que han hecho cambios
    @property
    def _history_user(self):  # Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'

    def __str__(self):
        return self.name

