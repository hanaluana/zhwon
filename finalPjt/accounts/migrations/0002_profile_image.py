# Generated by Django 2.1.7 on 2019-05-13 05:36

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to=''),
        ),
    ]
