# Generated by Django 5.2 on 2025-04-16 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_alumno_fecha_anotado"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alumno",
            name="curso",
            field=models.CharField(
                choices=[
                    ("Python", "Python"),
                    ("Django", "Django"),
                    ("JavaScript", "JavaScript"),
                ],
                max_length=20,
            ),
        ),
    ]
