# Generated by Django 4.1.7 on 2023-03-26 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usershorturl',
            name='clicks',
            field=models.PositiveBigIntegerField(default=0, verbose_name='Clicks Count'),
        ),
    ]