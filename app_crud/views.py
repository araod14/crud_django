from django.shortcuts import render, redirect
from .models import Task
from .form import CreateNew


createnew = CreateNew()
# Create your views here.
def index(request):
#    return render(request, 'index.html')

#def create_new(request):
    if request.method == 'GET':
        return render(request, 'index.html',
                      {
                        'form':createnew
                      }
                      )
    else:
        Task.objects.create(
            title = request.POST['title'],
            description = request.POST['description']
        )
        return redirect('/')