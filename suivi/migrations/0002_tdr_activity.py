# Generated by Django 5.1.6 on 2025-03-13 01:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("planification", "0023_alter_tache_depends_on"),
        ("suivi", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tdr",
            name="activity",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="planification.tache",
                verbose_name="Activité",
            ),
        ),
    ]
