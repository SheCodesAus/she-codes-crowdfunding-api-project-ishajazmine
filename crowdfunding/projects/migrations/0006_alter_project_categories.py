# Generated by Django 4.0.2 on 2022-03-22 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_category_oneoffpayment_alter_project_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(blank=True, to='projects.Category'),
        ),
    ]
