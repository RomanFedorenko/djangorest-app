# Generated by Django 5.1.6 on 2025-02-24 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empId', models.IntegerField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('salary', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
