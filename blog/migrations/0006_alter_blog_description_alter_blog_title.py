# Generated by Django 4.2.7 on 2024-01-27 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.CharField(default='description', max_length=2000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='title', max_length=200),
        ),
    ]