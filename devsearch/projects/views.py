from django.shortcuts import render
from django.http import HttpResponse
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


def projects(request):
    # msg = 'Hello, you are on the projects page'
    page = 'aloo'
    number = 10
    context = {'pagex':page, 'number': number,'projects':projectsList}
    # return render(request, 'projects/projects.html', {'pagex':page})

    return render(request, 'projects/projects.html', context)

# def project(request, pk):
#     return HttpResponse('SINGLE PROJECT' + ' ' + str(pk) )

def project(request, pk):
    
    return render(request, 'projects/single-projects.html')