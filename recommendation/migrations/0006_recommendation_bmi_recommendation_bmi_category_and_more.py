# Generated by Django 5.1.3 on 2025-02-13 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0005_remove_recommendation_bmi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='bmi',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='bmi_category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='meal_calories',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='recommended_calories',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
