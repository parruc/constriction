# Generated by Django 2.2b1 on 2019-02-16 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseinvestment',
            name='price',
            field=models.IntegerField(),
        ),
    ]
