# Generated by Django 3.2.7 on 2022-01-16 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_title', models.CharField(max_length=120)),
                ('slider_content', models.TextField(default='')),
                ('slider_image', models.ImageField(blank=True, null=True, upload_to='store_image/sliders_image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]