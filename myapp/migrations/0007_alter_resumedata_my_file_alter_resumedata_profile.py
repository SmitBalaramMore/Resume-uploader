# Generated by Django 5.0.6 on 2024-06-13 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_resumedata_genders_alter_resumedata_job_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumedata',
            name='my_file',
            field=models.FileField(blank=True, upload_to='Doc/'),
        ),
        migrations.AlterField(
            model_name='resumedata',
            name='profile',
            field=models.ImageField(blank=True, upload_to='profileimg/'),
        ),
    ]
