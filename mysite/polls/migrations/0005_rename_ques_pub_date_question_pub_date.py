# Generated by Django 4.1 on 2022-08-25 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_rename_pub_date_question_ques_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='ques_pub_date',
            new_name='pub_date',
        ),
    ]