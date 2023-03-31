# Generated by Django 4.1.7 on 2023-03-31 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section_T',
            fields=[
                ('sectionID', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('sectionNo', models.IntegerField(default=1)),
                ('semester', models.CharField(choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Autumn', 'Autumn')], max_length=30)),
                ('course', models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='app.course_t')),
                ('faculty', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
