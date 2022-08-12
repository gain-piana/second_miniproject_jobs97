# Generated by Django 3.2 on 2022-08-10 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobsTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=200)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
            ],
        ),
    ]
