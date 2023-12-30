from django.shortcuts import render
from movie.models import Movies
from movie.forms import movieform

def addmovie(request):
    form=movieform()
    if (request.method == "POST"):
        form = movieform(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()
            return viewmovie(request)
    return render(request, 'addmovie.html', {'form': form})

def viewmovie(request):
    m = Movies.objects.all()
    return render(request, 'home.html', {'movie':m})

def viewbyid(request,p):
    m=Movies.objects.get(id=p)
    return render(request,'view.html',{'movie':m})

def editbyid(request,p):
    m=Movies.objects.get(id=p)
    form = movieform(instance=m)
    if (request.method == "POST"):
        form = movieform(request.POST,request.FILES,instance=m)
        if (form.is_valid()):
            form.save()
            return viewmovie(request)
    return render(request, 'addmovie.html', {'form': form})

def deletebyid(request,p):
    m=Movies.objects.get(id=p)
    m.delete()
    return viewmovie(request)









