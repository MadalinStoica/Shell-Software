# Generated by Django 4.1.2 on 2022-10-10 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cui',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]