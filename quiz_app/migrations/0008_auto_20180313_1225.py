# Generated by Django 2.0.2 on 2018-03-13 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0007_answers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answers',
            new_name='Answer',
        ),
    ]