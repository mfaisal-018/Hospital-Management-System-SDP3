# Generated by Django 3.0.5 on 2021-07-06 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20210706_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointmentDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
