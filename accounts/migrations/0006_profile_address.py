# Generated by Django 2.2.7 on 2021-07-14 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210713_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default=1, max_length=50, verbose_name='المدينة :'),
            preserve_default=False,
        ),
    ]
