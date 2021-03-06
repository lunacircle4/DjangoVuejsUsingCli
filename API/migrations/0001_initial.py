# Generated by Django 2.2.1 on 2019-05-27 09:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('published_date', models.DateField(default=django.utils.timezone.now)),
                ('updated_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
