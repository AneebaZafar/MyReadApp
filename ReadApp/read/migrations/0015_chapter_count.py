# Generated by Django 5.0.6 on 2024-11-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read', '0014_reading_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
