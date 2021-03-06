# Generated by Django 3.0.8 on 2020-07-25 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200723_1658'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['created_at'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.Category', verbose_name='Категория'),
        ),
    ]
