# Generated by Django 4.0 on 2022-01-04 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Користувач', help_text="Введіть своє ім'я", max_length=20, verbose_name="Ім'я")),
                ('last_name', models.CharField(help_text='Введіть своє прізвище', max_length=20, verbose_name='Прізвище')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='auth.user')),
            ],
        ),
    ]
