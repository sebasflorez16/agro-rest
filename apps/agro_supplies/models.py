from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel

# Create your models here.


from django.db import models

class Variety(BaseModel):
    name = models.CharField(max_length=100)
    lote = models.CharField(max_length=50)
    siembra = models.JSONField()
    vigor = models.CharField(max_length=100)
    tillering = models.CharField(max_length=100)
    overturning = models.CharField(max_length=200)
    herbicide_susceptibility = models.JSONField()
    health = models.JSONField()
    nutrition = models.JSONField()
    harvest = models.CharField(max_length=100)
    environmental_requirements = models.CharField(max_length=200)
    general_recommendations = models.TextField()
    ica_producer_record = models.CharField(max_length=100)
    record_holder = models.CharField(max_length=100)
    documentation_name = models.CharField(max_length=100)
    documentation_link = models.URLField()

    historical = HistoricalRecords()

    #Maneja el historial de los usuarions que han hecho cambios
    @property
    def _history_user(self):  #Registra que usuario ha hecho el cambio
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
