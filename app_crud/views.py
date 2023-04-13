from django.shortcuts import render, redirect
from .models import Task
from .form import CreateNew


createnew = CreateNew()
# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html',
                  {
                    'tasks': tasks
                  }
        )
    
def create_task (request):
    if request.method == 'GET':
        return render(request, 'new_task.html',
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

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("/index/")