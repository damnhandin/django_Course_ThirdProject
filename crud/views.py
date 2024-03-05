from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound

from crud.forms import UserForm
from crud.models import Person


# получение данных из БД и загрузка index.html
def index(request):
    people = Person.objects.all()
    user_form = UserForm()
    return render(request, "index.html", {"people": people, "user_form": user_form})


# сохранение данных в БД
def create(request):
    if request.method == "POST":
        person = Person()
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
        return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")








# удаление данных из бд
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")