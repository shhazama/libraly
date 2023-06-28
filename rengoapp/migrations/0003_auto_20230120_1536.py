# Generated by Django 3.2 on 2023-01-20 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rengoapp', '0002_auto_20230113_0540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='社名')),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planet', models.CharField(blank=True, max_length=100, null=True, verbose_name='拠点')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rengoapp.comp')),
            ],
        ),
        migrations.AlterField(
            model_name='report',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rengoapp.planet'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]