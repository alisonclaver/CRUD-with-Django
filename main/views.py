from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def homepage(request):
    peoples = People.objects.all()
    print('Saved')

    context = {'peoples':peoples}
    return render(request, 'main/home.html', context)


def person_page(request, pk):
    people = People.objects.get(id=pk)
    form = PeopleForm(instance=people)

    if request.method == 'POST':
        form = PeopleForm(request.POST, request.FILES, instance=people)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'people':people, 'form':form}
    return render(request, 'main/person.html', context)


def delete_view(request, pk):
    people = People.objects.get(id=pk)
    people.delete()
    return redirect('home')


def create_page(request):
    if request.method == 'POST':
        form = PeopleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PeopleForm()
    
    context = {'form':form}
    return render(request, 'main/create_person.html', context)


