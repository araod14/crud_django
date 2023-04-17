from django.shortcuts import render, redirect
from .models import Task
from .form import CreateNew

#04p161abs no arranca en manual
#04v104
createnew = CreateNew()
# Create your views here.

    
def create_task (request):
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
    
def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html',
                  {
                    'tasks': tasks
                  }
        )

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("/")