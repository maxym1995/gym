# Generated by Django 4.0.3 on 2022-04-09 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gym_app', '0007_rename_member_reservations_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainings',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='gym_app.staff'),
        ),
        migrations.CreateModel(
            name='Trainers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_type', models.IntegerField(choices=[(0, 'Personal'), (1, 'GCT'), (2, 'Pilates'), (3, 'Stretching'), (4, 'K1'), (5, 'MMA'), (6, 'Box')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]