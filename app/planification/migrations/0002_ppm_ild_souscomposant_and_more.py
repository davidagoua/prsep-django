# Generated by Django 5.1.6 on 2025-03-06 07:12

import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("planification", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PPM",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                ("file", models.FileField(blank=True, null=True, upload_to="")),
                ("label", models.CharField(max_length=100)),
                ("status", models.IntegerField(default=0)),
            ],
            options={
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="ild",
            name="souscomposant",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ildsouscomposants",
                to="planification.souscomposantprojet",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="souscomposantprojet",
            name="composant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="souscomposants",
                to="planification.composantprojet",
            ),
        ),
    ]
