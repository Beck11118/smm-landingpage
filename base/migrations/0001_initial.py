# Generated by Django 4.0.5 on 2022-06-26 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.IntegerField()),
                ('date_until', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('company', models.BooleanField(default=False)),
                ('company_name', models.CharField(blank=True, max_length=200, null=True)),
                ('inn', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('priority', models.IntegerField(default=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.course')),
            ],
        ),
    ]
