# Generated by Django 5.1.6 on 2025-03-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("planification", "0020_exercice_montant_total_exercice_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="tache",
            name="status_execution",
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
