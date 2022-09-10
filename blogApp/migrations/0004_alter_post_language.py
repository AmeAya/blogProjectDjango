# Generated by Django 4.1.1 on 2022-09-10 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_alter_post_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='language',
            field=models.CharField(choices=[('EN', 'English'), ('RU', 'Russian'), ('KZ', 'Kazakh'), ('FR', 'French'), ('GR', 'Germanic')], default='EN', max_length=2),
        ),
    ]
