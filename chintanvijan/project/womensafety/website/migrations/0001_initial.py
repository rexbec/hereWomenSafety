# Generated by Django 2.2.7 on 2019-11-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
            ],
        ),
    ]
