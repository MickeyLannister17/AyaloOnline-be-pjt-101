# Generated by Django 3.2.4 on 2021-07-02 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ayaloapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Name of product')),
                ('location', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(verbose_name='/media')),
                ('price', models.IntegerField(verbose_name='Rental fee')),
                ('picture', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('Leesee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ayaloapp.modelleesee')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productlisting_api.category', verbose_name='Category')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='ProductBookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productlisting_api.product')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]