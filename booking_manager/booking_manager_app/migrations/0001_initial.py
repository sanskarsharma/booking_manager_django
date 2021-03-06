# Generated by Django 2.1.2 on 2018-10-14 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('row', models.CharField(max_length=4)),
                ('seat_number', models.IntegerField()),
                ('is_aisle_seat', models.BooleanField(default=False)),
                ('is_reserved', models.BooleanField(default=False)),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='booking_manager_app.Screen')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
