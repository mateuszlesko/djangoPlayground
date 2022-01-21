# Generated by Django 4.0 on 2022-01-21 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('posts', '0003_alter_comment_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitedPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likeIt', models.BooleanField(verbose_name='czy miejsce spodobało się')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post', verbose_name='odwiedzone miejsce')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
