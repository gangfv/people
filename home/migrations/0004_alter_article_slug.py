# Generated by Django 4.1.7 on 2023-04-14 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(choices=[('about_the_movement', 'о Движении'), ('news', 'Новости'), ('members_of_the_movement', 'Участники движения'), ('legal_volunteers', 'Волонтёры правового просвещения')]),
        ),
    ]
