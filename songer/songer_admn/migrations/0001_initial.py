# Generated by Django 2.1.7 on 2019-03-24 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('album_id', models.IntegerField(primary_key=True, serialize=False)),
                ('released_on', models.DateField()),
                ('label', models.CharField(max_length=40)),
                ('cover_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('band_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1000)),
                ('formed', models.CharField(max_length=30)),
                ('image_url', models.CharField(max_length=40)),
                ('website_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BandMember',
            fields=[
                ('member_id', models.IntegerField(primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=1000)),
                ('image_url', models.CharField(max_length=40)),
                ('band_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songer_admn.Band')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.IntegerField(primary_key=True, serialize=False)),
                ('genre_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.IntegerField(primary_key=True, serialize=False)),
                ('news_desc', models.CharField(max_length=1000)),
                ('cover_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Single',
            fields=[
                ('single_id', models.IntegerField(primary_key=True, serialize=False)),
                ('single_name', models.CharField(max_length=200)),
                ('cover_url', models.CharField(max_length=200)),
                ('singer', models.CharField(max_length=30)),
                ('album_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songer_admn.Album')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.IntegerField(primary_key=True, serialize=False)),
                ('song_name', models.CharField(max_length=200)),
                ('album_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songer_admn.Album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='genre_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songer_admn.Genre'),
        ),
    ]
