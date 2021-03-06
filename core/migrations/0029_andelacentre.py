# Generated by Django 2.0.1 on 2018-10-02 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20180906_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='AndelaCentre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centre_name', models.CharField(max_length=25, unique=True)),
                ('country', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Andela Centres',
            },
        ),
    ]
