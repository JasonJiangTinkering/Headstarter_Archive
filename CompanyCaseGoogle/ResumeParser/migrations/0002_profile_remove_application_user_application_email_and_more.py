# Generated by Django 4.0.6 on 2022-07-07 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ResumeParser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resumeadmin', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='application',
            name='user',
        ),
        migrations.AddField(
            model_name='application',
            name='email',
            field=models.CharField(default='del@gmail.com', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='first_name',
            field=models.CharField(default='de', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='last_name',
            field=models.CharField(default='del', max_length=30),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]