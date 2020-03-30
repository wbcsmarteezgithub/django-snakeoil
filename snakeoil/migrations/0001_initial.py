# Generated by Django 2.2 on 2020-03-30 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeoUrl',
            fields=[
                ('head_title', models.CharField(blank=True, max_length=55, verbose_name='head title')),
                ('meta_description', models.TextField(blank=True, max_length=160, verbose_name='meta description')),
                ('url', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'SEO URL',
                'verbose_name_plural': 'SEO URLs',
            },
        ),
    ]
