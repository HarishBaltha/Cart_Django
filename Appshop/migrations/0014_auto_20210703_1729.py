# Generated by Django 3.2.4 on 2021-07-03 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appshop', '0013_adminmodel_loginmodel_registermodel_total_twittermodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AdminModel',
        ),
        migrations.DeleteModel(
            name='LoginModel',
        ),
        migrations.DeleteModel(
            name='RegisterModel',
        ),
        migrations.DeleteModel(
            name='Total',
        ),
        migrations.DeleteModel(
            name='TwitterModel',
        ),
    ]
