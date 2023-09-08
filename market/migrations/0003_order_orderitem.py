# Generated by Django 4.2.4 on 2023-08-23 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0002_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=150)),
                ('lname', models.CharField(max_length=160)),
                ('email', models.CharField(max_length=160)),
                ('phone', models.CharField(max_length=160)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=160)),
                ('state', models.CharField(max_length=160)),
                ('country', models.CharField(max_length=160)),
                ('pincode', models.CharField(max_length=160)),
                ('total_price', models.FloatField()),
                ('payment_mode', models.CharField(max_length=150)),
                ('payment_id', models.CharField(max_length=250, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('Out For Shipping', 'Out For Shipping'), ('Completed', 'Completed')], default='pending', max_length=150)),
                ('message', models.TextField()),
                ('tracking_no', models.CharField(max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.product')),
            ],
        ),
    ]
