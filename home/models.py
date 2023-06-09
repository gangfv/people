from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок', blank=False)
    text = models.TextField(verbose_name='Текст статьи', blank=False)
    slug = models.SlugField(blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информационная страница'
        verbose_name_plural = 'Информационные страница'


class New(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок', blank=False)
    text = models.TextField(verbose_name='Текст Новости', blank=False)
    desc = models.TextField(verbose_name='Подробности Новости', blank=False)
    date = models.DateField(verbose_name='Дата создания', blank=False)
    img = models.FileField(upload_to='', blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'