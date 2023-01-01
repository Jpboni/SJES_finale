# Generated by Django 3.2.4 on 2022-12-30 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20221230_0300'),
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postfilecontent',
            options={'verbose_name_plural': 'Materials'},
        ),
        migrations.RemoveField(
            model_name='page',
            name='user',
        ),
        migrations.RemoveField(
            model_name='postfilecontent',
            name='user',
        ),
        migrations.AddField(
            model_name='page',
            name='course_code',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postfilecontent',
            name='course_code',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.course'),
            preserve_default=False,
        ),
    ]