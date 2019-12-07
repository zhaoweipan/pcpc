from django.shortcuts import get_object_or_404,render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .models import Sightings
from .forms import SightingsForm
def map(request):
    sightings=Sightings.objects.all()[:100]
    template=loader.get_template('sightings/map.html')
    context={
            'sightings':sightings,
        }
    return HttpResponse(template.render(context,request))
def all_squirrels(request):
    squirrels = Sightings.objects.all()
    context = {
            'squirrels':squirrels
            }
    return render(request,'sightings/all.html',context)
def squirrels_details(request,Unique_Squirrel_Id):
    squirrel = Sightings.objects.get(id=Unique_Squirrel_Id)
    return HttpResponse(f"hi,i'm {squirrel.Unique_Squirrel_Id}")
def UpdateView(request,Unique_Squirrel_Id):
    squirrel=Sightings.objects.get(Unique_Squirrel_Id=Unique_Squirrel_Id)
    if request.method == 'POST':
        form = SightingsForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{Unique_Squirrel_Id}')
        else:
            context= {'form': form,
                      'error': 'The form was not valid. Please do it again.'}
            return render(request,'sightings/edit.html' , context)
    else:
        form = SightingsForm(instance=squirrel)
        context = {'form': form,
                  'instance': squirrel}
        return render(request, 'sightings/edit.html', context)
def AddView(request):
    if request.method =='POST':
        form = SightingsForm(request.POST)
        #check data with form
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/all.html')
        else:
            context= {'form': form,
                      'error': 'The form was not valid. Please do it again.'}
            return render(request,'sightings/edit.html' , context)
    else:
        form = SightingsForm()
    context = {
            'form':form,
    }
    return render(request,'sightings/add.html',context)
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
