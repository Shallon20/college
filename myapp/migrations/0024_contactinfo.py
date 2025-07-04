# Generated by Django 5.2 on 2025-05-29 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('website', models.URLField(blank=True)),
                ('icon', models.ImageField(upload_to='contact_icons/')),
                ('office_hours', models.TextField(blank=True)),
            ],
        ),
    ]
