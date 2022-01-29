from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


# Create your views here.

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


# def projects(request):
#     # msg = 'Hello, you are on the projects page'
#     page = 'aloo'
#     number = 10
#     context = {'pagex':page, 'number': number,'projects':projectsList}
#     # return render(request, 'projects/projects.html', {'pagex':page})

#     return render(request, 'projects/projects.html', context)

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

# def project(request, pk):
#     return HttpResponse('SINGLE PROJECT' + ' ' + str(pk) )

# def project(request, pk):
#     projectObj = None
#     for i in projectsList:
#         if i ['id'] == pk:
#             projectObj = i

#     return render(request, 'projects/single-projects.html', {'project': projectObj})

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all() 
    print('projectObj:', projectObj)
    return render(request, 'projects/single-projects.html', {'project': projectObj, 'tags': tags })