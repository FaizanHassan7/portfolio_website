# Generated by Django 4.2.11 on 2024-08-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('Punjab', 'Punjab'), ('Sindh', 'Sindh'), ('KPK', 'KPK'), ('Balochistan', 'Balochistan')], max_length=20)),
                ('zip_code', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
    ]