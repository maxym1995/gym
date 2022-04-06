# Generated by Django 4.0.3 on 2022-04-06 16:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0003_alter_staff_year_of_birth_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainings',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainings',
            name='end_time',
            field=models.IntegerField(choices=[(1, '01:00'), (2, '02:00'), (3, '03:00'), (4, '04:00'), (5, '05:00'), (6, '06:00'), (7, '07:00'), (8, '08:00'), (9, '09:00'), (10, '10:00'), (11, '11:00'), (12, '12:00'), (13, '13:00'), (14, '14:00'), (15, '15:00'), (16, '16:00'), (17, '17:00'), (18, '18:00'), (19, '19:00'), (20, '20:00'), (21, '21:00'), (22, '22:00'), (23, '23:00'), (24, '24:00')], default=13),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainings',
            name='max_participants',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainings',
            name='start_time',
            field=models.IntegerField(choices=[(1, '01:00'), (2, '02:00'), (3, '03:00'), (4, '04:00'), (5, '05:00'), (6, '06:00'), (7, '07:00'), (8, '08:00'), (9, '09:00'), (10, '10:00'), (11, '11:00'), (12, '12:00'), (13, '13:00'), (14, '14:00'), (15, '15:00'), (16, '16:00'), (17, '17:00'), (18, '18:00'), (19, '19:00'), (20, '20:00'), (21, '21:00'), (22, '22:00'), (23, '23:00'), (24, '24:00')], default=11),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_to_trainer', models.CharField(max_length=256, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_app.members')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_app.trainings')),
            ],
        ),
    ]