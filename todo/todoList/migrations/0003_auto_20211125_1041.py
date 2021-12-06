# Generated by Django 3.2.9 on 2021-11-25 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0002_alter_todo_added_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='done_at',
            field=models.DateTimeField(),
        ),
    ]