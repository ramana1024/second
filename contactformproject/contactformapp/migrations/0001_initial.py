# Generated by Django 3.0.3 on 2020-02-11 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=100)),
                ('sal', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
