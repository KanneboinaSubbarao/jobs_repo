# Generated by Django 4.1.4 on 2024-02-05 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_alter_hydjobs_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bngjobs',
            name='address',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='punejobs',
            name='address',
            field=models.CharField(max_length=128),
        ),
    ]
