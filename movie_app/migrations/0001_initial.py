from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Режиссер',
                'verbose_name_plural': 'Режиссер',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Названия')),
                ('descriptions', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('duration', models.IntegerField(default=0, verbose_name='Продолжительность')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movie_app.director', verbose_name='Режиссер')),
            ],
            options={
                'verbose_name': 'Кино',
                'verbose_name_plural': 'Кино',
                'ordering': ['title', 'descriptions', 'created_at', 'updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movie_app.movie')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
