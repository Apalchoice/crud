from django.shortcuts import render
from django.http import HttpResponse
from .models import People


# Create your views here.
def home(request):
    return render(request, 'home.html')


def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        school = request.POST.get('school')
        email = request.POST.get('email')

    person = People(name=name, school=school, email=email)
    person.save()
    # print(name,school)
    return HttpResponse("success")


def people(request):
    d = People.objects.all()
    context = {"data": d}
    return render(request, 'people.html', context)


def delete(request, id):
    aa = People.objects.get(id=id)
    aa.delete()
    return HttpResponse('delete successful')


def update(request, id):
    l = People.objects.get(id=id)
    return render(request, 'edit.html', {'l': l})
