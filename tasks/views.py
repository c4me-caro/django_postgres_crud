from django.shortcuts import render,redirect
from tasks.models import Task

# Create your views here.
def list_tasks(req):
    tasks = Task.objects.all()
    return render(req, 'list_tasks.html', {'tasks':tasks})

def create_tasks(req):
    try:
        completed = True if (req.POST['completed'] == 'on') else False
    except:
        completed = False
    Task(title=req.POST['title'], description=req.POST['description'], completed=completed).save()
    return redirect("/tasks/")

def delete_tasks(req, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("/tasks/")

def update_tasks(req, id):
    task = Task.objects.get(id=id)
    return render(req, 'update_tasks.html', {'task':task})

def back_update_tasks(req, id):
    task = Task.objects.get(id=id)
    task.delete()
    
    try:
        completed = True if (req.POST['completed'] == 'on') else False
    except:
        completed = False
    Task(title=req.POST['title'], description=req.POST['description'], completed=completed).save()
    
    return redirect("/tasks/")