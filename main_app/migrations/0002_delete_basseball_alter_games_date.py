# Generated by Django 5.1.4 on 2025-01-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Basseball',
        ),
        migrations.AlterField(
            model_name='games',
            name='date',
            field=models.DateField(verbose_name='game date'),
        ),
    ]
