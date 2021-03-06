# Generated by Django 3.2.6 on 2021-08-12 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='author',
        ),
        migrations.RemoveField(
            model_name='project',
            name='card_img',
        ),
        migrations.RemoveField(
            model_name='project',
            name='repo_link',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tag',
        ),
        migrations.AlterField(
            model_name='project',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='blog.post'),
        ),
    ]
