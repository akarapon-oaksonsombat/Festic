# Generated by Django 3.1.5 on 2021-02-14 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=400)),
                ('img_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=12)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.eventdetail')),
            ],
        ),
    ]
