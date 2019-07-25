# Generated by Django 2.0 on 2019-06-07 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='description',
            field=models.TextField(default='kaisa hai'),
        ),
        migrations.AddField(
            model_name='album',
            name='time',
            field=models.DecimalField(decimal_places=2, default=25.91, max_digits=20),
            preserve_default=False,
        ),
    ]