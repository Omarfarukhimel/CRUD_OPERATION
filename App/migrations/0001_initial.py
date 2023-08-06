# Generated by Django 4.2.4 on 2023-08-04 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default='default_pic/default_pic.jpg', null=True, upload_to='profile_pic/')),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('age', models.PositiveIntegerField()),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.TextField(max_length=20)),
                ('address', models.TextField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=9)),
                ('religion', models.CharField(choices=[('Muslim', 'Muslim'), ('Hindu', 'Hindu'), ('Christian', 'Christian'), ('Buddha', 'Buddha')], max_length=9)),
            ],
        ),
    ]
