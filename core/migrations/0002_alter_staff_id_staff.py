# Generated by Django 4.1.3 on 2022-11-15 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='id_staff',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
