# Generated by Django 3.2.16 on 2023-06-15 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('info_perso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competences',
            name='competence',
            field=models.CharField(max_length=240),
        ),
        migrations.CreateModel(
            name='ProfileText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.TextField(blank=True, null=True, verbose_name='Profile')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
