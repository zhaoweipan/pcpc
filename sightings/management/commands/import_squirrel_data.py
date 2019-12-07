from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sightings
import csv
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.reader(fp)
            next(reader)
            for item in reader:
                for i in (15,16,17,18,19,21,22,23,24,25,26,27,28):
                    if item[i] == 'false':
                        item[i] = False
                    else:
                        item[i] = True
            data = list(reader)
        for row in data:
            Sightings.objects.create(
                        Longitude = row['Y'],
                        Latitude = row['X'],
                        Unique_Squirrel_Id = row['Unique Squirrel ID'],
                        Shift = row['Shift'],
                        Date = row['Date'],
                        Age = row['Age'],
                        Primary_Fur_Color = row['Primary Fur Color'],
                        Location = row['Location'],
                        Specific_Location = row['Specific Location'],
                        Running = row['Running'],
                        Chasing = row['Chasing'],
                        Climbing = row['Climbing'],
                        Eating = row['Eating'],
                        Foraging = row['Foraging'],
                        Other_Activities = row['Other Activities'],
                        Kuks = row['Kuks'],
                        Quaas = row['Quaas'],
			Moans = row['Moans'],
                        Tail_flags = row['Tail flags'],
                        Tail_twitches = row['Tail twitches'],
                        Approaches = row['Approaches'],
                        Indifferent = row['Indifferent'],
                        Runs_from = row['Runs from'],)
if __name__ == "__main__":
    main()
print('Done!')

