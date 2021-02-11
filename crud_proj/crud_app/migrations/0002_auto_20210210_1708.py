# Generated by Django 3.1.2 on 2021-02-10 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=80)),
                ('rollnumber', models.CharField(max_length=10)),
                ('student_class', models.IntegerField()),
                ('student_age', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]