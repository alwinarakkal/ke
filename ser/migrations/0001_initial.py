# Generated by Django 2.2.6 on 2019-11-01 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aut', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('flat_number', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('item1', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aut', models.CharField(max_length=255)),
                ('flat_number', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qu', models.IntegerField()),
                ('r', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ser.Item')),
                ('t', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ser.orders')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='t',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ser.orders'),
        ),
    ]
