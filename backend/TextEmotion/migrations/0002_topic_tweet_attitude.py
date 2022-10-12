# Generated by Django 4.1.2 on 2022-10-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TextEmotion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('name', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Topics',
            },
        ),
        migrations.AddField(
            model_name='tweet',
            name='attitude',
            field=models.CharField(max_length=50, null=True),
        ),
    ]