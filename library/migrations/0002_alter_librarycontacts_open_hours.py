# Generated by Django 5.2 on 2025-06-01 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarycontacts',
            name='open_hours',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
