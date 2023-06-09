# Generated by Django 4.1.7 on 2023-04-14 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_article_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, verbose_name='Текст Новости')),
                ('date', models.DateField(blank=True, verbose_name='Дата создания')),
                ('img', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(blank=True, verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Заголовок'),
        ),
    ]
