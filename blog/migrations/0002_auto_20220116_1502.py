# Generated by Django 3.2.7 on 2022-01-16 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_alt',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, null=True, upload_to='store_image/blog_image/'),
        ),
    ]
