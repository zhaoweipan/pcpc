from django.shortcuts import get_object_or_404,render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect,Http404

from .models import Sightings

def map(request):
    sightings=Sightings.objects.all()[:100]
    template=loader.get_template('sightings/map.html')
    context={
        'sightings':sightings,
    }
    return HttpResponse(template.render(context,request))
    
def IndexView(request):
    # print(len(Sightings.objects.all()))
    sightings_list=Sightings.objects.all()[::-1][:10]
    template=loader.get_template('sightings/index.html')
    context={
        'sightings_list':sightings_list,
    }
    return HttpResponse(template.render(context,request))
    
def UpdateView(request,Unique_Squirrel_Id):
    squirrel=Sightings.objects.get(Unique_Squirrel_Id=Unique_Squirrel_Id)
    print(request.method)
    if request.method == 'DELETE':
        squirrel.delete()
    elif request.method == 'POST':
        squirrel.Latitude=request.POST.get('Latitude',None)
        squirrel.Longitude=request.POST.get('Longitude',None)
        squirrel.Unique_Squirrel_Id=request.POST.get('Unique_Squirrel_Id',None)
        squirrel.Shift=request.POST.get('Shift',None)
        squirrel.Date=request.POST.get('Date',None)
        squirrel.Age=request.POST.get('Age',None)
        squirrel.Primary_Fur_Color=request.POST.get('Primary_Fur_Color',None)
        squirrel.Location=request.POST.get('Location',None)
        squirrel.Specific_Location=request.POST.get('Specific_Location',None)
        squirrel.Running=request.POST.get('Running',None)
        squirrel.Chasing=request.POST.get('Chasing',None)
        squirrel.Climbing=request.POST.get('Climbing',None)
        squirrel.Eating=request.POST.get('Eating',None)
        squirrel.Foraging=request.POST.get('Foraging',None)
        squirrel.Other_Activities=request.POST.get('Other_Activities',None)
        squirrel.Kuks=request.POST.get('Kuks',None)
        squirrel.Quaas=request.POST.get('Quaas',None)
        squirrel.Moans=request.POST.get('Moans',None)
        squirrel.Tail_flags=request.POST.get('Tail_flags',None)
        squirrel.Tail_twitches=request.POST.get('Tail_twitches',None)
        squirrel.Approaches=request.POST.get('Approaches',None)
        squirrel.Indifferent=request.POST.get('Indifferent',None)
        squirrel.Runs_from=request.POST.get('Runs_from',None)

        squirrel.save()
    return render(request,'sightings/squirrel.html',{'squirrel':squirrel})
    pass
    
    
    
def AddView(request):
    
    try:
        Latitude=request.POST['Latitude']
        Longitude=request.POST['Longitude']
        Unique_Squirrel_Id=request.POST['Unique_Squirrel_Id']
        Shift=request.POST['Shift']
        Date=request.POST['Date']
        Age=request.POST['Age']
        Primary_Fur_Color=request.POST['Primary_Fur_Color']
        Location=request.POST['Location']
        Specific_Location=request.POST['Specific_Location']
        Running=request.POST['Running']
        Chasing=request.POST['Chasing']
        Climbing=request.POST['Climbing']
        Eating=request.POST['Eating']
        Foraging=request.POST['Foraging']
        Other_Activities=request.POST['Other_Activities']
        Kuks=request.POST['Kuks']
        Quaas=request.POST['Quaas']
        Moans=request.POST['Moans']
        Tail_flags=request.POST['Tail_flags']
        Tail_twitches=request.POST['Tail_twitches']
        Approaches=request.POST['Approaches']
        Indifferent=request.POST['Indifferent']
        Runs_from=request.POST['Runs_from']
        
        Sightings.objects.create(
                        Latitude=Latitude,
                        Longitude=Longitude,
                        Unique_Squirrel_Id=Unique_Squirrel_Id,
                        Shift=Shift,
                        Date=Date,
                        Age=Age,
                        Primary_Fur_Color=Primary_Fur_Color,
                        Location=Location,
                        Specific_Location=Specific_Location,
                        Running=Running,
                        Chasing=Chasing,
                        Climbing=Climbing,
                        Eating=Eating,
                        Foraging=Foraging,
                        Other_Activities=Other_Activities,
                        Kuks=Kuks,
                        Quaas=Quaas,
                        Moans=Moans,
                        Tail_flags=Tail_flags,
                        Tail_twitches=Tail_twitches,
                        Approaches=Approaches,
                        Indifferent=Indifferent,
                        Runs_from=Runs_from,)
                        


                        
    except Exception as e:
        print(e)
    return render(request,'sightings/add.html',)
    

    
def DeleteView(request,Unique_Squirrel_Id):
    squirrel=Sightings.objects.get(Unique_Squirrel_Id=Unique_Squirrel_Id)
    squirrel.delete()
    pass
    
def StatsView(request):
    Running_Count_True=Sightings.objects.filter(Running=True).count()
    Running_Count_False=Sightings.objects.filter(Running=False).count()
    
    Chasing_Count_True=Sightings.objects.filter(Chasing=True).count()
    Chasing_Count_False=Sightings.objects.filter(Chasing=False).count()
    
    Climbing_Count_True=Sightings.objects.filter(Climbing=True).count()
    Climbing_Count_False=Sightings.objects.filter(Climbing=False).count()
    
    Eating_Count_True=Sightings.objects.filter(Eating=True).count()
    Eating_Count_False=Sightings.objects.filter(Eating=False).count()
    
    Foraging_Count_True=Sightings.objects.filter(Foraging=True).count()
    Foraging_Count_False=Sightings.objects.filter(Foraging=False).count()
    
    context={
        'Running':{'True':Running_Count_True,'False':Running_Count_False},
        'Chasing':{'True':Chasing_Count_True,'False':Chasing_Count_False},
        'Climbing':{'True':Climbing_Count_True,'False':Climbing_Count_False},
        'Eating':{'True':Eating_Count_True,'False':Eating_Count_False},
        'Foraging':{'True':Foraging_Count_True,'False':Foraging_Count_False}
        
    }
    # print(context)
    return render(request,'sightings/stats.html',{'context':context})
    
    
    pass
