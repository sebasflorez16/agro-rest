from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
import uuid
from simple_history.models import HistoricalRecords


# Create your models here.

# Modelo cliente para django-tenants
class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)
    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)  # Universal Unique Identifiquer


class Domain(DomainMixin):
    pass


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado', default=True)
    created_date = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de Modificacion', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Fecha de Eliminacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Bases'

    def __str__(self):
        pass


class EmployeesBase(models.Model):
    PAYMENT_CHOICES = [
        ('hourly', 'Pago por Hora'),
        ('daily', 'Pago por Día'),
        ('contract', 'Pago por Contrato'),
    ]

    id = models.AutoField(primary_key=True)
    identification_number = models.BigIntegerField('Número de Identificación', unique=True)
    identification_image = models.ImageField('Copia Cedula', upload_to='cv-contractor/', blank=True, null=True)
    first_name = models.CharField('Nombres', max_length=100)
    last_name = models.CharField('Apellidos', max_length=100)
    address = models.CharField('Dirección', max_length=200)
    phone = models.BigIntegerField('Teléfono')
    email = models.EmailField('Correo Electrónico', blank=True, null=True)
    state = models.BooleanField('Estado', default=True)
    cv = models.ImageField('CV', upload_to='cv-contractor/', blank=True, null=True)
    professional_id = models.BigIntegerField('Numero Tarjeta Profesional', blank=True, null=True)
    professional_image = models.ImageField('Copia Tarjeta Profesional', upload_to='cv-contractor/', blank=True,
                                           null=True)
    health_certificate = models.ImageField('Afiliacion de Eps', upload_to='cv-contractor', blank=True, null=True)
    social_security = models.ImageField('Seguridad Social', upload_to='cv-contractor', blank=True, null=True)
    fingerprint = models.BinaryField(null=True, blank=True)
    start_date = models.DateField('Fecha de Inicio del Contrato')
    end_date = models.DateField('Fecha de Fin del Contrato')
    payment_type = models.CharField('Tipo de Pago', max_length=10, choices=PAYMENT_CHOICES)
    payment_value = models.DecimalField('Valor de Pago', max_digits=8, decimal_places=2)
    created_date = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de Modificacion', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Fecha de Eliminacion', auto_now=True, auto_now_add=False)
    historical = HistoricalRecords(inherit=True)  # Esto hace que los modelos que hereden de este sepa que es abstrac
    # y tambien para que hereden toda su funcionalidad

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
        abstract = True
        verbose_name = 'Empleado Base'
        verbose_name_plural = 'Empleados Bases'

    def __str__(self):
        pass
