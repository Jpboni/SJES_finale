# Generated by Django 3.2.4 on 2022-12-31 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_alter_postfilecontent_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['-title'], 'verbose_name_plural': 'Page'},
        ),
    ]
