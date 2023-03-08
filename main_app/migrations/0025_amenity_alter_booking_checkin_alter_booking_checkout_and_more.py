# Generated by Django 4.1.7 on 2023-03-08 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_alter_booking_checkin_alter_booking_checkout_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('icon', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkin',
            field=models.DateField(default=datetime.datetime(2023, 3, 8, 17, 59, 8, 398764), verbose_name='Checkin Date'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout',
            field=models.DateField(default=datetime.datetime(2023, 3, 8, 17, 59, 8, 398767), verbose_name='Checkout Date'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 3, 8, 17, 59, 8, 398755), verbose_name='Booking Date'),
        ),
        migrations.AddField(
            model_name='listing',
            name='amenities',
            field=models.ManyToManyField(to='main_app.amenity'),
        ),
    ]