# Generated by Django 3.0.5 on 2020-08-11 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='strecsvdatamodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=450)),
                ('rating', models.CharField(max_length=400)),
                ('reviews', models.CharField(max_length=400)),
                ('type', models.CharField(max_length=400)),
                ('hq', models.CharField(max_length=400)),
                ('employees', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'strecsvdatamodel',
            },
        ),
    ]
