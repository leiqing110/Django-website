# Generated by Django 2.2 on 2019-04-30 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP01', '0014_auto_20190430_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Huiyuan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('pwd', models.CharField(default='123', max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
