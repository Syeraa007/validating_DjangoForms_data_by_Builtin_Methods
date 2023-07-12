# Generated by Django 4.2.1 on 2023-07-12 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('loc', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('remail', models.EmailField(max_length=254)),
                ('url', models.URLField()),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
    ]
