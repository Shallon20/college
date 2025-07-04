# Generated by Django 5.2 on 2025-05-21 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_jobsinternshipsads'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('icon_class', models.CharField(max_length=100)),
                ('leader_name', models.CharField(max_length=100)),
                ('leader_contact', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='sports/')),
                ('captain_name', models.CharField(blank=True, max_length=100)),
                ('captain_contact', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
