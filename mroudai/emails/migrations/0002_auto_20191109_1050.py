# Generated by Django 2.2.5 on 2019-11-09 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactme',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contactme',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contactme',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contactme',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contactme',
            name='subject',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
