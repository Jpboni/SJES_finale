# Generated by Django 3.2.4 on 2022-12-30 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20221230_0300'),
        ('page', '0001_initial'),
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='course_code',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='pages',
            field=models.ManyToManyField(to='page.Page'),
        ),
    ]
