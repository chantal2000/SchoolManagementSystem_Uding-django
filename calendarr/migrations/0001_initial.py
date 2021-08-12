# Generated by Django 3.2.4 on 2021-08-11 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=12)),
                ('event_Id', models.CharField(max_length=20)),
                ('event_name', models.CharField(max_length=30)),
                ('event_duration', models.CharField(max_length=20)),
                ('event_planner', models.CharField(max_length=30)),
                ('event_approval', models.CharField(max_length=30)),
                ('event_participants', models.CharField(max_length=50)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
            ],
        ),
    ]