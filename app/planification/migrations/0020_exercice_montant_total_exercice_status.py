# Generated by Django 5.1.6 on 2025-03-09 10:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("planification", "0019_exercice_tache_exercice"),
    ]

    operations = [
        migrations.AddField(
            model_name="exercice",
            name="montant_total",
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="exercice",
            name="status",
            field=models.IntegerField(default=0),
        ),
    ]
