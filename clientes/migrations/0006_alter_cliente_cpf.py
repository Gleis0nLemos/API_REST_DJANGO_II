# Generated by Django 4.1.3 on 2022-11-17 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_alter_cliente_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
