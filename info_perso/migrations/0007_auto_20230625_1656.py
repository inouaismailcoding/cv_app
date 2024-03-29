# Generated by Django 3.2.16 on 2023-06-25 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_perso', '0006_auto_20230623_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='debut',
            field=models.DateField(blank=True, null=True, verbose_name='date Debut'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='entreprise',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='titre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='ville',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
