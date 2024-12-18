# Generated by Django 5.1.3 on 2024-12-05 21:26

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet_log', '0006_uploadedmealphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='file',
            field=models.ImageField(default='/media/default_image.png', storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='UploadedMealPhoto',
        ),
    ]
