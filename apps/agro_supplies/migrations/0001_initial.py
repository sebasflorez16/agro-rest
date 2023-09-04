# Generated by Django 4.2.2 on 2023-08-16 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Variety",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("state", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "created_date",
                    models.DateField(
                        auto_now_add=True, verbose_name="Fecha de Creación"
                    ),
                ),
                (
                    "modified_date",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Modificacion"
                    ),
                ),
                (
                    "deleted_date",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Eliminacion"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("lote", models.CharField(max_length=50)),
                ("siembra", models.JSONField()),
                ("vigor", models.CharField(max_length=100)),
                ("tillering", models.CharField(max_length=100)),
                ("overturning", models.CharField(max_length=200)),
                ("herbicide_susceptibility", models.JSONField()),
                ("health", models.JSONField()),
                ("nutrition", models.JSONField()),
                ("harvest", models.CharField(max_length=100)),
                ("environmental_requirements", models.CharField(max_length=200)),
                ("general_recommendations", models.TextField()),
                ("ica_producer_record", models.CharField(max_length=100)),
                ("record_holder", models.CharField(max_length=100)),
                ("documentation_name", models.CharField(max_length=100)),
                ("documentation_link", models.URLField()),
            ],
            options={
                "verbose_name": "Variedad",
                "verbose_name_plural": "Variedades",
            },
        ),
        migrations.CreateModel(
            name="HistoricalVariety",
            fields=[
                ("id", models.IntegerField(blank=True, db_index=True)),
                ("state", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "created_date",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Fecha de Creación"
                    ),
                ),
                (
                    "modified_date",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Fecha de Modificacion"
                    ),
                ),
                (
                    "deleted_date",
                    models.DateField(
                        blank=True, editable=False, verbose_name="Fecha de Eliminacion"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("lote", models.CharField(max_length=50)),
                ("siembra", models.JSONField()),
                ("vigor", models.CharField(max_length=100)),
                ("tillering", models.CharField(max_length=100)),
                ("overturning", models.CharField(max_length=200)),
                ("herbicide_susceptibility", models.JSONField()),
                ("health", models.JSONField()),
                ("nutrition", models.JSONField()),
                ("harvest", models.CharField(max_length=100)),
                ("environmental_requirements", models.CharField(max_length=200)),
                ("general_recommendations", models.TextField()),
                ("ica_producer_record", models.CharField(max_length=100)),
                ("record_holder", models.CharField(max_length=100)),
                ("documentation_name", models.CharField(max_length=100)),
                ("documentation_link", models.URLField()),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Variedad",
                "verbose_name_plural": "historical Variedades",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]