# Generated by Django 3.2.9 on 2021-11-07 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EduDistrict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubDistrict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('no_schools', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.district')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('udise', models.CharField(max_length=11)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('edudistrict', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.edudistrict')),
            ],
        ),
        migrations.AddField(
            model_name='edudistrict',
            name='subdistrict',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.subdistrict'),
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.state'),
        ),
    ]
