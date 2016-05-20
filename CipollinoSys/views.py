from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TaskForm
from django.shortcuts import redirect


def index(request):
    return  render(request, 'CipollinoSys/index.html', {})

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_owner = request.user
            task.save()
            return redirect('CipollinoSys/view_task', pk=task.pk)


    else:
        form = TaskForm()
    return render(request, 'CipollinoSys/new_task.html', {'form' : form } )

def view_task(request):
    return HttpResponseRedirect(request.)

def all_tasks(request):
    return HttpResponseRedirect('/all_tasks/')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TaskForm(request.POST)
        print ('1 if')
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            task = form.save(commit = False)
            task.task_owner = request.user
            task.save()
            print ('2 if')
            return redirect('blog.views.post_detail', pk=task.pk)

    # if a GET (or any other method) we'll create a blank form
    else:
        print ('else')
        form = TaskForm()

    return render(request, 'CipollinoSys/name.html', {'form': form})



