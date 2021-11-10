# Generated by Django 3.2.8 on 2021-11-07 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20211107_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(default=0)),
                ('dislike', models.IntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user', verbose_name='Автор')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.question', verbose_name='Вопрос')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(default=0)),
                ('dislike', models.IntegerField(default=0)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.answer', verbose_name='Ответ')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user', verbose_name='Автор')),
            ],
        ),
    ]
