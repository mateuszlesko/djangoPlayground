# Generated by Django 4.0 on 2022-01-04 07:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('content', models.TextField()),
                ('address', models.CharField(max_length=64)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, default='default.png', upload_to='images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('comments', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.comment')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.place', verbose_name='place where it is')),
            ],
        ),
    ]
