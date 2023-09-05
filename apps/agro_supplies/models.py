#from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel

# Create your models here.


from django.db import models


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
