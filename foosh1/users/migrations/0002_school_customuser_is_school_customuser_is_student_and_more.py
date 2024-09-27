# Generated by Django 4.2.9 on 2024-04-08 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="School",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="название"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="customuser",
            name="is_school",
            field=models.BooleanField(default=False, verbose_name="школа"),
        ),
        migrations.AddField(
            model_name="customuser",
            name="is_student",
            field=models.BooleanField(default=False, verbose_name="ученик"),
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="имя")),
                (
                    "surname",
                    models.CharField(max_length=100, verbose_name="фамилия"),
                ),
                (
                    "patronymic",
                    models.CharField(max_length=100, verbose_name="отчество"),
                ),
                (
                    "school",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="users.school",
                        verbose_name="школа",
                    ),
                ),
            ],
        ),
    ]
