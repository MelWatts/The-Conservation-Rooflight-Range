# Generated by Django 3.2 on 2022-03-17 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_alter_stories_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('size', models.TextField(blank=True, null=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stories.category')),
            ],
            options={
                'verbose_name_plural': 'Story',
            },
        ),
    ]
