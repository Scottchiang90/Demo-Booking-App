# Generated by Django 3.0.8 on 2020-07-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_booking_preferred_stylist'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('1', 'Stylist'), ('2', 'Senior Stylist'), ('3', 'Director')], default='12', max_length=2),
            preserve_default=False,
        ),
    ]
