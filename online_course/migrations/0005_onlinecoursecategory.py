# Generated by Django 3.2.7 on 2022-01-25 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_course', '0004_auto_20220118_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineCourseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('online_course_category', models.CharField(max_length=100)),
            ],
        ),
    ]