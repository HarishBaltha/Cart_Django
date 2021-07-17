# Generated by Django 3.2.4 on 2021-06-25 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Appshop', '0008_auto_20210625_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('No', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Design', models.CharField(max_length=100)),
                ('File', models.FileField(upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='LoginModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=30, unique=True)),
                ('Password', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Username', models.CharField(max_length=30, unique=True)),
                ('Email', models.EmailField(max_length=20, unique=True)),
                ('Contact', models.IntegerField()),
                ('Password', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tot', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TwitterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=30, unique=True)),
                ('Password', models.CharField(max_length=15, unique=True)),
            ],
        ),
    ]