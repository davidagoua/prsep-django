# Generated by Django 5.1.6 on 2025-03-18 01:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("programme", "0005_action_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="composantesprogram",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
