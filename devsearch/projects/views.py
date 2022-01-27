from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def projects(request):
    # msg = 'Hello, you are on the projects page'
    page = 'aloo'
    number = 10
    context = {'pagex':page, 'number': number}
    # return render(request, 'projects/projects.html', {'pagex':page})

    return render(request, 'projects/projects.html', context)

# def project(request, pk):
#     return HttpResponse('SINGLE PROJECT' + ' ' + str(pk) )

def project(request, pk):
    
    return render(request, 'projects/single-projects.html')