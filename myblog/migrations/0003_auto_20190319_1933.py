# Generated by Django 2.0.2 on 2019-03-19 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20190319_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newblog',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='newblog',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
