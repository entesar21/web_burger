# Generated by Django 3.2.7 on 2022-01-18 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='chapter_related_to',
            new_name='related_to_online_course',
        ),
        migrations.RenameField(
            model_name='episode',
            old_name='episode_related_to',
            new_name='related_to_chapter',
        ),
        migrations.RenameField(
            model_name='onlinecourse',
            old_name='online_course_name',
            new_name='online_course_title',
        ),
        migrations.RemoveField(
            model_name='onlinecourse',
            name='online_course_date',
        ),
    ]
