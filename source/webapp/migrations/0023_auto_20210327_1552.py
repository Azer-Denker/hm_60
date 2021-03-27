# Generated by Django 2.2 on 2021-03-27 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0022_tipe_project_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipe',
            old_name='project_id',
            new_name='project_pk',
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(verbose_name='Дата начала'),
        ),
    ]
