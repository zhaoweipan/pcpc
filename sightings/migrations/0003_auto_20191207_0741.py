# Generated by Django 2.2.7 on 2019-12-07 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0002_auto_20191204_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sightings',
            name='Age',
            field=models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('Other', 'Other')], default='Other', help_text='Age', max_length=10),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Approaches',
            field=models.BooleanField(default=False, help_text='Approaches'),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Chasing',
            field=models.BooleanField(default=False, help_text='Chasing'),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Climbing',
            field=models.BooleanField(default=False, help_text='Climbing'),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Date',
            field=models.CharField(help_text='Date', max_length=10),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Eating',
            field=models.BooleanField(default=False, help_text='Eating'),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Foraging',
            field=models.BooleanField(default=False, help_text='Foraging'),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Indifferent',
            field=models.BooleanField(default=False, help_text='Indifferent'),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Kuks',
            field=models.BooleanField(default=False, help_text='Kuks'),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Latitude',
            field=models.DecimalField(decimal_places=10, help_text='Latitude', max_digits=100),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Location',
            field=models.CharField(choices=[('Above Ground', 'Above Ground'), ('Ground Plane', 'Ground Plane'), ('Other', 'Other')], default='Other', help_text='Location', max_length=30),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Longitude',
            field=models.DecimalField(decimal_places=10, help_text='Longitude', max_digits=100),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Moans',
            field=models.BooleanField(default=False, help_text='Moans'),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Other_Activities',
            field=models.CharField(help_text='Other_Activities', max_length=100),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Primary_Fur_Color',
            field=models.CharField(choices=[('Black', 'Black'), ('Cinnamon', 'Cinnamon'), ('Gray', 'Gray'), ('Other', 'Other')], default='Other', help_text='Primary_Fur_Color', max_length=30),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Quaas',
            field=models.BooleanField(default=False, help_text='Quaas'),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Running',
            field=models.BooleanField(default=False, help_text='Running'),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Runs_from',
            field=models.BooleanField(default=False, help_text='Runs_from'),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Shift',
            field=models.CharField(choices=[('PM', 'PM'), ('AM', 'AM')], max_length=100),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Specific_Location',
            field=models.CharField(help_text='Specific_Location', max_length=100),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Tail_flags',
            field=models.BooleanField(default=False, help_text='Tail_flags'),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Tail_twitches',
            field=models.BooleanField(default=False, help_text='Tail_twitchs'),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Unique_Squirrel_Id',
            field=models.CharField(help_text='Unique_Squirrel_Id', max_length=100),
        ),
    ]
