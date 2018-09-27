from django.shortcuts import render, redirect
import data.models as models
import data.forms as forms
from django.urls import reverse

# Create your views here.
def portfolio(request):
    projects = models.Project.objects.all()
    return render(request, 'data/portfolio.html',{'projects':projects})

def addproject(request):
    project_form = forms.ProjectForm()

    if request.method == 'POST':
        
        project_form = forms.ProjectForm(request.POST, request.FILES)

        if project_form.is_valid():
            project = models.Project()
            project.title = request.POST.get('title')
            project.description = request.POST.get('description')
            project.image = project_form.cleaned_data['image']
            project.link = request.POST.get('link')
            project.save()

            return redirect(reverse('portfolio'))

    return render(request,'data/add_project.html', {'form':project_form})

def person(request):
    people = models.Person.objects.all()
    return render(request, 'data/person.html',{'people':people})

def addperson(request):
    person_form = forms.PersonForm()

    if request.method == 'POST':
        person_form = forms.PersonForm(request.POST)
        if person_form.is_valid:
            person_form.save()

            """person = models.Person()
            person.firstname = request.POST.get('firstname')
            person.lastname = request.POST.get('lastname')
            person.save()"""

            return redirect('/person/')

    return render(request, 'data/add_person.html',{'form':person_form})