# Generated by Django 2.1 on 2020-08-02 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200725_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='message',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='message_html',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
    ]