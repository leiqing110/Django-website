# Generated by Django 2.2 on 2019-04-24 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP01', '0008_goods_goods_type'),
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
        migrations.AlterField(
            model_name='goods_type',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]