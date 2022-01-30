# Generated by Django 3.2.7 on 2022-01-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_course_online_course_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='online_course_status',
        ),
        migrations.AddField(
            model_name='course',
            name='course_level',
            field=models.CharField(choices=[('مبتدی', 'Beginner'), ('متوسط', 'Intermediate'), ('حرفه ای', 'Proffessional')], default='مبتدی', max_length=100),
        ),
        migrations.AddField(
            model_name='course',
            name='course_status',
            field=models.CharField(choices=[('پیش ثبت نام', 'Pre Registration'), ('در حال برگزاری', 'Running'), ('برگزار شده', 'Done')], default='در حال برگزاری', max_length=100),
        ),
    ]