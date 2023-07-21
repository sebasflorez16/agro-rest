# Generated by Django 4.2.2 on 2023-07-18 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("RRHH", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contractoremployee",
            name="rut",
            field=models.CharField(unique=True, verbose_name="RUT"),
        ),
        migrations.AlterField(
            model_name="historicalcontractoremployee",
            name="rut",
            field=models.CharField(db_index=True, verbose_name="RUT"),
        ),
    ]
