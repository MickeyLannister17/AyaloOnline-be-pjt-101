# Generated by Django 3.2.4 on 2021-07-07 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayaloapp', '0002_auto_20210705_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelleesee',
            name='VerificationField',
            field=models.BigIntegerField(),
        ),
    ]
