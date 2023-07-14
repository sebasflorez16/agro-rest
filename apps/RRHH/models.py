from django.db import models
from datetime import datetime
from simple_history.models import HistoricalRecords
from apps .base.models import BaseModel

# Create your models here.

class Department(BaseModel):
    name = models.CharField('Nombre', max_length=50)
    description = models.TextField('Descripción')
    historical = HistoricalRecords()

    #Maneja el historial de los usuarions que han hecho cambios
    @property
    def _history_user(self):  #Registra que usuario ha hecho el cambio
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.name
    


class Position(BaseModel):
    name = models.CharField('Nombre',max_length=50)
    description = models.TextField('Descripción')
    historical = HistoricalRecords()

    @property
    def _history_user(self):  
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value


    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
    
    def __str__(self):
        return self.name
    

class Employee(BaseModel):
    identification_number = models.CharField('Número de Identificación', max_length=20, unique=True)
    name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    email = models.EmailField('Correo Electrónico')
    phone = models.BigIntegerField('Telefono', blank=True, null=True, default=0)
    address = models.CharField('Dirección', max_length=100)
    image = models.ImageField('Imagen de Perfil', upload_to='perfil', blank=True, null=True)
    cv = models.ImageField('Hoja de Vida', upload_to='cv/', blank=True, null=True)
    fingerprint = models.BinaryField(null=True, blank=True)
    salary = models.DecimalField('Salario', max_digits=8, decimal_places=2, default=0.0, blank=False, null=False,)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True,  verbose_name='Departamento')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Cargo', null=True)
    date_of_birth = models.DateField('Fecha de Nacimiento', blank=True, null=True,)
    date_of_hire = models.DateField('Fecha de Contratación', blank=False, null=True,)
    is_staff = models.BooleanField(default=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.change_by

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value


    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def employee_age(date_of_birth):
        today = datetime.today()
        age = date_of_birth - today.year
        if today.month < date_of_birth.month or (today.month == date_of_birth.month and today.day < date_of_birth.day):
            age -= 1
        return age 

    
    def __str__(self):
        return f"{self.name}{self.last_name}"


class TemporaryEmployee(BaseModel):
    pass


class ContractorEmployee(BaseModel):

    PAYMENT_CHOICES = [
        ('hourly', 'Pago por Hora'),
        ('daily', 'Pago por Día'),
        ('contract', 'Pago por Contrato'),
    ]

    first_name = models.CharField('Nombres', max_length=100)
    last_name = models.CharField('Apellidos', max_length=100)
    address = models.CharField('Dirección', max_length=200)
    phone = models.BigIntegerField('Teléfono', max_length=20)
    email = models.EmailField('Correo Electrónico')
    cv = models.ImageField('CV', upload_to='cv-contractor/', blank=True, null=True)
    identification_number = models.BigIntegerField('Número de Identificación', max_length=20, unique=True)
    identification_image = models.ImageField('Copia Cedula', upload_to='cv-contractor/', blank=True, null=True)
    professional_id = models.BigIntegerField('Numero Tarjeta Profesional', blank=True, null=True)
    professional_image = models.ImageField('Copia Tarjeta Profesional', upload_to='cv-contractor/', blank=True, null=True)
    rut = models.IntegerField('RUT', max_length=20, unique=True)
    image_rut = models.ImageField('Copia Rut', upload_to='cv-contractor/', blank=True, null=True)
    health_certificate = models.ImageField('Afiliacion de Eps', upload_to='cv-contractor', blank=True, null=True)
    social_security = models.ImageField('Seguridad Social', upload_to='cv-contractor', blank=True, null=True)
    fingerprint = models.BinaryField(null=True, blank=True)
    start_date = models.DateField('Fecha de Inicio del Contrato')
    end_date = models.DateField('Fecha de Fin del Contrato')
    payment_type = models.CharField('Tipo de Pago', max_length=10, choices=PAYMENT_CHOICES)
    payment_value = models.DecimalField('Valor de Pago', max_digits=8, decimal_places=2)
    historical = HistoricalRecords()


    @property
    def _history_user(self):
        return self.change_by
    

    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value


    def calculate_contract_value(self, hours=None, days=None):
        if self.payment_type == 'hourly' and hours is not None:
            return self.payment_value * hours
        elif self.payment_type == 'daily' and days is not None:
            return self.payment_value * days
        elif self.payment_type == 'contract':
            return self.payment_value
        else:
            return None

    class Meta:
        verbose_name = 'Contratista'
        verbose_name_plural = 'Contratistas'
    
    def __str__(self):
        return self.identification_number


    



"""Se registra esta parte pero queda para hacer la conexion con el SDK de un lector de huellas para la asistencia biometrica"""

class Attendance(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    check_in_time = models.TimeField(null=True, blank=True)
    check_out_time = models.TimeField(null=True, blank=True)
    attended = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = "Asistencias"

    def __str__(self):
        return f"{self.employee.name} - {self.date}"


