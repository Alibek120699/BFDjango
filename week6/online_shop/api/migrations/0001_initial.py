# Generated by Django 2.2.10 on 2020-03-02 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OfflineProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=1000)),
                ('desc', models.TextField(max_length=500)),
                ('count', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('discount', models.IntegerField(default=10)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OnlineProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=1000)),
                ('desc', models.TextField(max_length=500)),
                ('count', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('needs_delivery', models.BooleanField(default=False)),
                ('delivery_address', models.CharField(max_length=100)),
                ('delivery_price', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'abstract': False,
            },
        ),
    ]
