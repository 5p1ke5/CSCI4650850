# Generated by Django 5.2 on 2025-04-19 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net_petz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='food',
            field=models.IntegerField(default=0),
        ),
    ]
