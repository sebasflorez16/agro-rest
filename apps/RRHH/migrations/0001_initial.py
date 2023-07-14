# Generated by Django 4.2.2 on 2023-07-14 21:03

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
            name="Department",
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
                ("name", models.CharField(max_length=50, verbose_name="Nombre")),
                ("description", models.TextField(verbose_name="Descripción")),
            ],
            options={
                "verbose_name": "Departamento",
                "verbose_name_plural": "Departamentos",
            },
        ),
        migrations.CreateModel(
            name="Position",
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
                ("name", models.CharField(max_length=50, verbose_name="Nombre")),
                ("description", models.TextField(verbose_name="Descripción")),
            ],
            options={
                "verbose_name": "Cargo",
                "verbose_name_plural": "Cargos",
            },
        ),
        migrations.CreateModel(
            name="HistoricalPosition",
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
                ("name", models.CharField(max_length=50, verbose_name="Nombre")),
                ("description", models.TextField(verbose_name="Descripción")),
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
                "verbose_name": "historical Cargo",
                "verbose_name_plural": "historical Cargos",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalEmployee",
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
                (
                    "identification_number",
                    models.CharField(
                        db_index=True,
                        max_length=20,
                        verbose_name="Número de Identificación",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Nombre")),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Apellidos"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, verbose_name="Correo Electrónico"
                    ),
                ),
                (
                    "phone",
                    models.BigIntegerField(
                        blank=True, default=0, null=True, verbose_name="Telefono"
                    ),
                ),
                ("address", models.CharField(max_length=100, verbose_name="Dirección")),
                (
                    "image",
                    models.TextField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Imagen de Perfil",
                    ),
                ),
                ("fingerprint", models.BinaryField(blank=True, null=True)),
                (
                    "salary",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=8,
                        verbose_name="Salario",
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fecha de Nacimiento"
                    ),
                ),
                (
                    "date_of_hire",
                    models.DateField(null=True, verbose_name="Fecha de Contratación"),
                ),
                ("is_staff", models.BooleanField(default=False)),
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
                    "department",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="RRHH.department",
                        verbose_name="Departamento",
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
                (
                    "position",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="RRHH.position",
                        verbose_name="Cargo",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Empleado",
                "verbose_name_plural": "historical Empleados",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalDepartment",
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
                ("name", models.CharField(max_length=50, verbose_name="Nombre")),
                ("description", models.TextField(verbose_name="Descripción")),
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
                "verbose_name": "historical Departamento",
                "verbose_name_plural": "historical Departamentos",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="Employee",
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
                (
                    "identification_number",
                    models.CharField(
                        max_length=20,
                        unique=True,
                        verbose_name="Número de Identificación",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Nombre")),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Apellidos"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, verbose_name="Correo Electrónico"
                    ),
                ),
                (
                    "phone",
                    models.BigIntegerField(
                        blank=True, default=0, null=True, verbose_name="Telefono"
                    ),
                ),
                ("address", models.CharField(max_length=100, verbose_name="Dirección")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="perfil",
                        verbose_name="Imagen de Perfil",
                    ),
                ),
                ("fingerprint", models.BinaryField(blank=True, null=True)),
                (
                    "salary",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=8,
                        verbose_name="Salario",
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fecha de Nacimiento"
                    ),
                ),
                (
                    "date_of_hire",
                    models.DateField(null=True, verbose_name="Fecha de Contratación"),
                ),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "department",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="RRHH.department",
                        verbose_name="Departamento",
                    ),
                ),
                (
                    "position",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="RRHH.position",
                        verbose_name="Cargo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Empleado",
                "verbose_name_plural": "Empleados",
            },
        ),
        migrations.CreateModel(
            name="Attendance",
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
                ("date", models.DateField()),
                ("check_in_time", models.TimeField(blank=True, null=True)),
                ("check_out_time", models.TimeField(blank=True, null=True)),
                ("attended", models.BooleanField(default=False)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="RRHH.employee"
                    ),
                ),
            ],
            options={
                "verbose_name": "Asistencia",
                "verbose_name_plural": "Asistencias",
            },
        ),
    ]