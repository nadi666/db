# Generated by Django 4.1 on 2023-08-06 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_db', '0007_remove_subjectplan_plan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectplan',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student_db.plan'),
        ),
    ]
