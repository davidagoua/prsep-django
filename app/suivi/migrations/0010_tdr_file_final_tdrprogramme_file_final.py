# Generated by Django 5.1.7 on 2025-03-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("suivi", "0009_rename_tdr_commentairetdr_content_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="tdr",
            name="file_final",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="tdr",
                verbose_name="TDR fin d'activité",
            ),
        ),
        migrations.AddField(
            model_name="tdrprogramme",
            name="file_final",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="tdr",
                verbose_name="TDR fin d'activité",
            ),
        ),
    ]
