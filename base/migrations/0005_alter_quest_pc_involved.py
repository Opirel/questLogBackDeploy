# Generated by Django 5.0.3 on 2024-04-01 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_questtest_remove_quest_pc_involved_quest_pc_involved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='pc_involved',
            field=models.ManyToManyField(default='[]', to='base.playercharacter'),
        ),
    ]
