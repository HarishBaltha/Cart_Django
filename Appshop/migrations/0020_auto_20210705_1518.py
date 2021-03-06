# Generated by Django 3.2.4 on 2021-07-05 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appshop', '0019_alter_product_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AdminModel',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='cartproduct',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartproduct',
            name='product',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.DeleteModel(
            name='LoginModel',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='RegisterModel',
        ),
        migrations.DeleteModel(
            name='Total',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartProduct',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
