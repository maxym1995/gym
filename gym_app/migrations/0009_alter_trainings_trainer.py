# Generated by Django 4.0.3 on 2022-04-09 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0008_alter_trainings_trainer_trainers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainings',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='gym_app.trainers'),
        ),
    ]
