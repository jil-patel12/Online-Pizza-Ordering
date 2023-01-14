# Generated by Django 3.0.6 on 2020-12-24 13:06

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
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=150, null=True)),
                ('contact_email', models.EmailField(max_length=150, null=True)),
                ('contact_message', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='menu1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('image1', models.ImageField(upload_to='menu/image')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user_extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120)),
                ('phone_no', models.CharField(max_length=10)),
                ('Date_of_birth', models.DateField()),
                ('user_address1', models.TextField()),
                ('user_address2', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=25)),
                ('Countary', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]