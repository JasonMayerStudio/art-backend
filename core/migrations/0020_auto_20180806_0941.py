# Generated by Django 2.0.1 on 2018-08-06 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_asset_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeWorkspace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('section',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                   to='core.OfficeFloorSection')),
            ],
            options={
                'verbose_name': 'Office Workspace',
            },
        ),
        migrations.AlterUniqueTogether(
            name='officeworkspace',
            unique_together={('name', 'section')},
        ),
    ]
