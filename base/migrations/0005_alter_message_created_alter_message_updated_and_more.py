# Generated by Django 4.1.5 on 2023-02-11 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_alter_message_updated_alter_room_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="message",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="room",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="room",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
