# Generated by Django 3.2.4 on 2021-07-05 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productlisting_api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('Date_of_order', models.DateField(auto_now_add=True)),
                ('Time_of_order', models.TimeField(auto_now_add=True)),
                ('Delivery', models.CharField(choices=[('Pick-up', 'Pick-up'), ('House delivery', 'House delivery')], max_length=256)),
                ('Date_of_return', models.DateTimeField()),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productlisting_api.product')),
            ],
        ),
    ]
