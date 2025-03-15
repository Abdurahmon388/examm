# Generated by Django 5.1.7 on 2025-03-15 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configApp', '0003_remove_group_students_remove_student_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='is_graduated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='is_studying',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(blank=True, related_name='student_courses', to='configApp.course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='student_groups', to='configApp.group'),
        ),
    ]
