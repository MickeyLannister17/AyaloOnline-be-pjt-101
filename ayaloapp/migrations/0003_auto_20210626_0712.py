# Generated by Django 3.2.4 on 2021-06-26 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayaloapp', '0002_customsignupcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email address'),
        ),
        migrations.DeleteModel(
            name='CustomSignupCode',
        ),
    ]
