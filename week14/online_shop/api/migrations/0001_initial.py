# Generated by Django 2.2.10 on 2020-04-19 20:40

import api.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('duration', models.PositiveIntegerField()),
                ('extra_description', models.FileField(blank=True, null=True, upload_to='product_files', validators=[api.validators.validate_extension])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShopStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Shop',
                'verbose_name_plural': 'Shops',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=10)),
                ('img', models.ImageField(blank=True, null=True, upload_to='product_files', validators=[api.validators.validate_file_size])),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='api.ShopStore')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceOrder',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Order')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Service')),
            ],
            bases=('api.order',),
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Order')),
                ('delivery_price', models.PositiveIntegerField(default=0)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Product')),
            ],
            bases=('api.order',),
        ),
    ]