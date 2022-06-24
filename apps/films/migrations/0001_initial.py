# Generated by Django 4.0.5 on 2022-06-22 13:18

import ckeditor_uploader.fields
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
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.SlugField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComingSoon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='coming_soon/')),
                ('trailer', models.FileField(upload_to='trailer/', verbose_name='трейлер')),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='название фильма')),
                ('name_ru', models.CharField(max_length=250, null=True, verbose_name='название фильма')),
                ('name_en', models.CharField(max_length=250, null=True, verbose_name='название фильма')),
                ('country', models.CharField(max_length=100, verbose_name='страна')),
                ('country_ru', models.CharField(max_length=100, null=True, verbose_name='страна')),
                ('country_en', models.CharField(max_length=100, null=True, verbose_name='страна')),
                ('year', models.IntegerField(verbose_name='год')),
                ('age_restriction', models.IntegerField(verbose_name='возрастное ограничение')),
                ('description', models.TextField(verbose_name='описание')),
                ('description_ru', models.TextField(null=True, verbose_name='описание')),
                ('description_en', models.TextField(null=True, verbose_name='описание')),
                ('poster', models.ImageField(upload_to='films_image/', verbose_name='постер')),
                ('trailer', models.FileField(upload_to='trailer/', verbose_name='трейлер')),
                ('url', models.SlugField(null=True, unique=True)),
                ('actors', models.ManyToManyField(related_name='actors', to='films.actor', verbose_name='актеры')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.category', verbose_name='категории')),
                ('date', models.ManyToManyField(to='films.date', verbose_name='дата и время ')),
                ('director', models.ManyToManyField(related_name='director', to='films.director', verbose_name='директор')),
                ('genre', models.ManyToManyField(to='films.genre', verbose_name='Жанры')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('image', models.ImageField(blank=True, null=True, upload_to=' news_images/', verbose_name='Картина')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('description_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Описание')),
                ('description_en', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Описание')),
                ('url', models.SlugField(null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='цена билета для взрослых')),
                ('price_child', models.IntegerField(blank=True, null=True, verbose_name='цена билета для детей ')),
                ('movie_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.CharField(max_length=1)),
                ('sites_number', models.IntegerField()),
                ('movie_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=11)),
                ('time_pub', models.DateTimeField(auto_now_add=True)),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.movie', verbose_name='фильм')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='EndingSoon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('ticket_choice', models.CharField(choices=[('Детский', 'Детский'), ('Взрослый', 'Взрослый')], max_length=50, verbose_name='Билет')),
                ('sites', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.sites')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.ticket')),
            ],
        ),
    ]
