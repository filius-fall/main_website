# Generated by Django 4.0.4 on 2022-05-28 14:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_banner_image_alter_post_date_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_post',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 28, 14, 21, 40, 957247, tzinfo=utc)),
        ),
    ]
