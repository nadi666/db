# Generated by Django 4.1 on 2023-08-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_db', '0004_plan_subjectplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='work',
            field=models.CharField(choices=[('мастер', 'мастер'), ('учитель', 'учитель')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='course',
            field=models.CharField(choices=[('два года', 'два года'), ('три месяца', 'три месяца'), ('год (после 9)', 'год (после 9)'), ('год (после 9 и 11)', 'год (после 9 и 11)')], max_length=50, null=True, unique=True),
        ),
    ]