# Generated by Django 4.0.3 on 2022-04-13 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0014_alter_trainings_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainings',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
