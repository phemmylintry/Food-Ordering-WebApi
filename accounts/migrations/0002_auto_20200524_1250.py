# Generated by Django 3.0.6 on 2020-05-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phoneNumber',
            field=models.IntegerField(blank=True),
        ),
    ]