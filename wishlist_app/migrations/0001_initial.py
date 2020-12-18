# Generated by Django 3.1.4 on 2020-12-18 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='product_img')),
                ('brand', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('reviewScore', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Fav_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='wishlist_app.client')),
                ('product', models.ManyToManyField(related_name='wishlist', to='wishlist_app.Product')),
            ],
            options={
                'unique_together': {('client',)},
            },
        ),
    ]
