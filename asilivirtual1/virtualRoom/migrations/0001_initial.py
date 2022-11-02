# Generated by Django 4.1.2 on 2022-10-28 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Height')),
                ('shoulders', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Shoulders')),
                ('burst', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Burst')),
                ('waist', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Waist')),
                ('hips', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Hips')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
