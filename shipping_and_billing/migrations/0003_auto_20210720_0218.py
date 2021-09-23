# Generated by Django 3.2.4 on 2021-07-19 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_and_billing', '0002_auto_20210720_0206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping_detail',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='shipping_detail',
            name='last_name',
        ),
        migrations.AddField(
            model_name='shipping_detail',
            name='name',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
