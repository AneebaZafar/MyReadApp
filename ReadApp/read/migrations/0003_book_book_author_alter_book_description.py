# Generated by Django 5.0.6 on 2024-08-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_author',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(blank=True, default='', max_length=5000, null=True),
        ),
    ]
