# Generated by Django 3.0.8 on 2020-07-08 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='service',
            field=models.CharField(choices=[('Hair Cut Only', 'Hair Cut Only'), ('Hair Cut and Wash', 'Hair Cut and Wash'), ('Colouring', 'Colouring'), ('Perming', 'Perming'), ('Straightening', 'Straightening'), ('Treatment', 'Treatment')], max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time_slot',
            field=models.CharField(choices=[('8', '0800 to 0900'), ('9', '0900 to 1000'), ('10', '1000 to 1100'), ('11', '1100 to 1200'), ('12', '1200 to 1300'), ('13', '1300 to 1400'), ('14', '1400 to 1500'), ('15', '1500 to 1600'), ('16', '1600 to 1700'), ('17', '1700 to 1800'), ('18', '1800 to 1900'), ('19', '1900 to 2000')], max_length=2),
        ),
    ]
