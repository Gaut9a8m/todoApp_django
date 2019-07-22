from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.utils import timezone
# Create your views here.

def home(request):
    if request.method == 'POST':
        if request.POST['task']:
            tasks = Task()
            tasks.task = request.POST['task']
            tasks.time = timezone.datetime.now()
            tasks.complete = False
            tasks.save()
            return redirect('home')
    else:
        alltask = Task.objects
        return render(request, 'task/home.html', {'alltask':alltask})



def taskcompleted(request, id):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk = id)
        task.complete = True
        task.save()
        return redirect('home')

def delete(request, id):
    if request.method == 'POST':
        deleted = Task.objects.filter(id=id)
        print(deleted)
        deleted.delete()
        return redirect('home')
