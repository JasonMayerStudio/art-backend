# Generated by Django 2.1.2 on 2018-10-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20181015_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officeblock',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
