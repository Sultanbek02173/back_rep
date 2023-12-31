# Generated by Django 4.2.4 on 2023-08-28 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('status', models.BooleanField(default=True, verbose_name='Статус публикации')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Commets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='Имя пользователя')),
                ('text', models.CharField(max_length=300, verbose_name='Текст коментария')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_commet', to='posts.post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
                'ordering': ('-created',),
            },
        ),
    ]
