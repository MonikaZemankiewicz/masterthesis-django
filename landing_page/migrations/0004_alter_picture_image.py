# Generated by Django 4.2.2 on 2023-07-18 01:37

from django.db import migrations
import optimized_image.fields


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0003_alter_picture_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=optimized_image.fields.OptimizedImageField(default='1.jpg', upload_to=''),
        ),
    ]
