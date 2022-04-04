# Generated by Django 4.0.3 on 2022-04-03 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('year_of_birth', models.IntegerField(max_length=4)),
                ('type', models.CharField(choices=[(0, 'Trainer'), (1, 'Recepctionist'), (2, 'Director'), (3, 'Accountant')], max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='members',
            name='sex',
            field=models.IntegerField(choices=[(0, 'Female'), (1, 'Male')]),
        ),
        migrations.CreateModel(
            name='Trainings',
            fields=[
                ('name', models.CharField(choices=[(0, 'Personal'), (1, 'GCT'), (2, 'Pilates'), (3, 'Stretching'), (4, 'K1'), (5, 'MMA'), (6, 'Box')], max_length=64)),
                ('trainer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='gym_app.staff')),
            ],
        ),
    ]