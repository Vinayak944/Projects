# Generated by Django 2.1 on 2023-09-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('discription', models.CharField(max_length=2083)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
