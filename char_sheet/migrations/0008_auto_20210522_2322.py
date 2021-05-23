# Generated by Django 3.1.7 on 2021-05-22 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('char_sheet', '0007_auto_20210522_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_class',
            name='special_ability',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='char_sheet.abilities'),
        ),
        migrations.AlterField(
            model_name='job_class',
            name='weapon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='char_sheet.items'),
        ),
        migrations.AlterField(
            model_name='race',
            name='special_ability',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='char_sheet.abilities'),
        ),
    ]
