# Generated by Django 4.0.3 on 2022-04-06 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.TextField(),
        ),
    ]
