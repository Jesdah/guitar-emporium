# Generated by Django 3.2 on 2023-10-18 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guitars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('guitar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guitars.guitar')),
            ],
        ),
    ]
