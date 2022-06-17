# Generated by Django 4.0.4 on 2022-06-07 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RED', '0002_qurans_ayats'),
    ]

    operations = [
        migrations.CreateModel(
            name='chapter_ayats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_id', models.IntegerField()),
                ('chapter_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='qurans_ayats',
            name='ayats',
        ),
        migrations.RemoveField(
            model_name='qurans_ayats',
            name='chapter_name',
        ),
        migrations.AddField(
            model_name='qurans_ayats',
            name='ayat_no',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='qurans_ayats',
            name='sura_no',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='qurans_ayats',
            name='surah_name',
            field=models.CharField(default=None, max_length=24),
        ),
        migrations.AlterField(
            model_name='qurans_ayats',
            name='chapter_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RED.chapter_ayats'),
        ),
    ]