from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sightings
import pandas as pd

class Command(BaseCommand):
    help = 'import data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('file_path',nargs=1,type=str)

    def handle(self, *args, **options):
        # print(options)
        df=pd.read_csv(options['file_path'][0])
        # print(df.columns)
        for index,row in df.iterrows():
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