# Generated by Django 4.1.7 on 2023-03-31 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_enrollment_t'),
    ]

    operations = [
        migrations.CreateModel(
            name='PLO_T',
            fields=[
                ('ploID', models.AutoField(primary_key=True, serialize=False)),
                ('ploNo', models.IntegerField()),
                ('details', models.CharField(max_length=255)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.program_t')),
            ],
        ),
    ]
