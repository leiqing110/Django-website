# Generated by Django 2.2 on 2019-04-30 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP01', '0018_delete_huiyuan'),
    ]

    operations = [
        migrations.AddField(
            model_name='admininfo',
            name='email',
            field=models.CharField(default='123', max_length=20),
        ),
    ]