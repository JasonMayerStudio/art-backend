# Generated by Django 2.1.2 on 2018-10-15 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_andelacentre'),
    ]

    operations = [
        migrations.AddField(
            model_name='officeblock',
            name='location',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.PROTECT,
                to='core.AndelaCentre'),
        ),
        migrations.AlterUniqueTogether(
            name='officeblock',
            unique_together={('name', 'location')},
        ),
    ]
