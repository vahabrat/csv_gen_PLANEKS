# Generated by Django 3.1.5 on 2021-01-26 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_gen', '0002_auto_20210126_2127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fakephonenumber',
            old_name='phone_number',
            new_name='fake_phone_number',
        ),
        migrations.AlterField(
            model_name='schema',
            name='schema_delimiter',
            field=models.CharField(choices=[(',', ','), ('%', '%'), ('!', '!'), ('/', '/')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='schema',
            name='schema_string_character',
            field=models.CharField(choices=[('"', '"'), ('&', '&'), ('@', '@')], max_length=1, null=True),
        ),
    ]
