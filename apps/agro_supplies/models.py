#from django.db import models
from simple_history.models import HistoricalRecords
from apps.RRHH.models import Employee
from apps.base.models import BaseModel


# Create your models here.


from django.db import models

#Por el momento esto lo vamos a utilizar como un listado de semillas para luego hacer una integracion. de resto 
class Variety(BaseModel):
    name = models.CharField(max_length=100)
    lote = models.CharField(max_length=50)
    siembra = models.JSONField(blank=True, null=True)
    vigor = models.CharField(max_length=100, blank=True, null=True)
    tillering = models.CharField(max_length=100, blank=True, null=True)
    overturning = models.CharField(max_length=200, blank=True, null=True)
    herbicide_susceptibility = models.JSONField(blank=True, null=True)
    health = models.JSONField(blank=True, null=True)
    nutrition = models.JSONField(blank=True, null=True)
    harvest = models.CharField(max_length=100, blank=True, null=True)
    environmental_requirements = models.CharField(max_length=200, blank=True, null=True)
    general_recommendations = models.TextField(blank=True, null=True)
    ica_producer_record = models.CharField(max_length=100, blank=True, null=True)
    record_holder = models.CharField(max_length=100, blank=True, null=True)
    documentation_name = models.CharField(max_length=100, blank=True, null=True)
    documentation_link = models.URLField(blank=True, null=True)

    historical = HistoricalRecords()

    # Maneja el historial de los usuarions que han hecho cambios
    @property
    def _history_user(self):  # Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'Variedad'
        verbose_name_plural = 'Variedades'

    def __str__(self):
        return self.name

    @classmethod
    def create_from_seed_data(cls, seed_data):
        name = seed_data['fields']['name']
        lote = seed_data['fields']['lote']
        properties = seed_data['fields']

        variety = cls(name=name, lote=lote, properties=properties)
        variety.save()

        return variety
    
# Modelos de proveedores y suministros

class Company(BaseModel):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    rut = models.CharField(max_length=20, verbose_name="RUT")
    addres = models.CharField(max_length=60, verbose_name="Dirección", blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):  # Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.name

class Supplier(BaseModel):
    name = models.CharField(max_length=50, verbose_name="Nombre del Proveedor")
    company = models.ForeignKey(Company, verbose_name="Empresa del Proveedor", on_delete=models.CASCADE, blank=True, null=True)
    code = models.CharField(verbose_name="Codigo del Proveedor (Opcional)", blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):  # Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=20, verbose_name="Nombre de la categoria")
    description = models.TextField(max_length=100, verbose_name="Descripción", blank=True, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):  # Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

class SubCategory(BaseModel):
    name = models.CharField(max_length=20, verbose_name="Nombre de la Subcategoria")
    description = models.CharField(max_length=100)
    historical = HistoricalRecords()

    @property
    def _history_user(self):  # Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'Subcategoria'
        verbose_name_plural = 'Subcategorias'

    def __str__(self):
        return self.name



class Warehouse(BaseModel):
    name = models.CharField(max_length=255)
    ubication = models.CharField(max_length=255)
    capacity = models.IntegerField()
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def _history_user(self):  # Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'Acopio'
        verbose_name_plural = 'Acopios'

    def __str__(self):
        return self.name

# Por el momento se puede manejar cualquier tipo de insumo en este modelo como pesticidas, abonos etc
class Supply(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Nombre del suministro")
    category = models.ForeignKey(Category, related_name="categoria", on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, related_name="subcategoria", on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company, related_name="empresa", on_delete=models.CASCADE, blank=True, null=True)
    supplier = models.ForeignKey(Supplier, related_name="vendedor", on_delete=models.CASCADE, blank=True, null=True)
    stock = models.IntegerField(verbose_name="Cantidad")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    meassure_unit = models.CharField(max_length=20, verbose_name="Unidad de medida")
    warehouse = models.ManyToManyField(Warehouse)

    @property
    def _history_user(self):  # Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'

    def __str__(self):
        return self.name

# Modelos de equipamiento agricola.

class CategoryEquipment(BaseModel):
    name = models.CharField(max_length=20, verbose_name="Nombre del equipo")
    description = models.CharField(max_length=100, verbose_name="Descripcion del equipo", blank=True, null=True)

    @property
    def _history_user(self):  # Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'Categoria del equipo'
        verbose_name_plural = 'Categoria de los equipos'

    def __str__(self):
        return self.name
    

class SubcategoryEquipment(BaseModel):
    name = models.CharField(max_length=20, verbose_name="Nombre del equipo")
    description = models.CharField(max_length=100, verbose_name="Descripcion del equipo", blank=True, null=True)
    category = models.ForeignKey(CategoryEquipment, verbose_name="Categoria Padre", on_delete=models.CASCADE)

    @property
    def _history_user(self):  # Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'Subcategoria del equipo'
        verbose_name_plural = 'Subcategoria de los equipos'

    def __str__(self):
        return self.name


class ToolAndEquipment(BaseModel):
    TYPE_STATE = [
        ('disponible', 'Disponible'),
        ('en uso', 'En uso'),
        ('en reparación', 'En reparación'),
    ]
    
    name = models.CharField(max_length=30, verbose_name="Nombre del Equipo")
    description = models.TextField(max_length=100, blank=True, null=True, verbose_name="Descripción")
    category = models.ForeignKey(CategoryEquipment, verbose_name="Categoria de la herramienta", on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubcategoryEquipment, on_delete=models.CASCADE, verbose_name="Subcategoria de la herramienta", blank=True, null=True)
    type = models.CharField(max_length=50, verbose_name="Tipo de herramienta", blank=True, null=True)
    amount = models.IntegerField(verbose_name="Cantidad Disponible")
    state = models.CharField(max_length=20, choices=TYPE_STATE)
    store = models.ForeignKey(Warehouse, related_name='herramientas', on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def _history_user(self):  # Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'Equipo y/o Herramienta'
        verbose_name_plural = 'Equipos y/o Herramientas'

    def __str__(self):
        return self.name
    

class ToolAssignment(BaseModel):
    tool = models.ForeignKey(ToolAndEquipment, related_name='asignaciones', on_delete=models.CASCADE, verbose_name="Herramienta")
    employee = models.ForeignKey(Employee, related_name='asignaciones', on_delete=models.CASCADE, verbose_name="Empleado")
    fecha_asignacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Asignación")
    fecha_devolucion = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Devolución")
    estado = models.CharField(max_length=20, choices=ToolAndEquipment.TYPE_STATE, verbose_name="Estado", default='en uso')

    @property
    def _history_user(self):  # Registra que usuario ha hecho el cambio
            return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value
        
    class Meta:
        verbose_name = "Asignación de Herramienta"
        verbose_name_plural = "Asignaciones de Herramientas"

    def __str__(self):
        return f'{self.tool.name} asignada a {self.employee.name} {self.employee.last_name} {self.employee.identification_number}'



