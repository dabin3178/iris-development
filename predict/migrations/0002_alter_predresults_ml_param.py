# Generated by Django 4.0.4 on 2022-06-06 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predresults',
            name='ml_param',
            field=models.CharField(default='default', max_length=200),
        ),
    ]
