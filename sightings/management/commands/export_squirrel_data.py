from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sightings
import csv

class Command(BaseCommand):
    help = 'export data to csv file'

    def add_arguments(self, parser):
        parser.add_argument('file_path',nargs=1,type=str)

    def handle(self, *args, **options):
        # print(options)
        with open(options['file_path'][0],'w') as f:
            f.write('Latitude,Longitude,Unique_Squirrel_Id,Shift,Date,Age,Primary_Fur_Color,Location,Specific_Location,Running,Chasing,Climbing,Eating,Foraging,Other_Activities,Kuks,Quaas,Moans,Tail_flags,Tail_twitches,Approaches,Indifferent,Runs_from\n')
            
            for query in Sightings.objects.all():
                line = '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (query.Latitude,query.Longitude,query.Unique_Squirrel_Id,query.Shift,query.Date,query.Age,query.Primary_Fur_Color,query.Location,query.Specific_Location,query.Running,query.Chasing,query.Climbing,query.Eating,query.Foraging,query.Other_Activities,query.Kuks,query.Quaas,query.Moans,query.Tail_flags,query.Tail_twitches,query.Approaches,query.Indifferent,query.Runs_from,)
                f.write(line)
                
                
if __name__ == "__main__":
    main()
    print('Done!')
    
