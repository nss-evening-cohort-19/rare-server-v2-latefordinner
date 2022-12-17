# Generated by Django 4.1.4 on 2022-12-17 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('category_id', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('publication_date', models.DateField()),
                ('image_url', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=300)),
                ('approved', models.BooleanField()),
            ],
        ),
    ]
