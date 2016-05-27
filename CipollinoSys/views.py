from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import TaskForm
from .models import Task, Results
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
import datetime




def all_tasks(request):

    user = request.user
    tasks = Task.objects.filter(published_date__lte=timezone.now()).filter(task_performer = user).order_by('published_date')
    print (tasks)
    return render(request, 'CipollinoSys/all_tasks.html', {'tasks': tasks})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.task_owner = request.user
            task.save()
            return redirect('CipollinoSys.views.view_task', pk=task.pk)


    else:
        form = TaskForm()
    return render(request, 'CipollinoSys/new_task.html', {'form' : form } )

def view_task(request, pk):

    task = get_object_or_404(Task, pk=pk)
    return render(request, 'CipollinoSys/view_task.html', {'task': task } )


def edit_task(request, pk):
        task = get_object_or_404(Task, pk=pk)
        time = task.wasted_time
        if request.method == "POST":
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                task = form.save(commit=False)
                task.task_owner = request.user
                task.published_date = timezone.now()
                result = Results.objects.create(task_name = task, task_performer = request.user, wasted_time = task.wasted_time)
                result.save()
                time = + task.wasted_time
                task.wasted_time = time
                task.save()

                return redirect('CipollinoSys.views.view_task', pk=task.pk)
        else:
            form = TaskForm(instance=task)
        return render(request, 'CipollinoSys/edit_task.html', {'form': form})


#def log_in(request):
#    print('0')
#    if request.method == "POST":
#        form = AuthenticationForm(data=request.POST)
#        print('1')
#        if form.is_valid():
#            print('2')
#            username = request.POST.get('username')
#            password = request.POST.get('password')
#            user = authenticate(username=username, password=password)
#            if user is not None:
#                print ('3')
#                if user.is_active:
#                    print ('4')
#                    login(request, user)
#                    return render(request,'CipollinoSys.views.all_tasks')

#                else:
#                    print ('5')
#                    return redirect('CipollinoSys.views.error')
#
#            else:
#                print ('6')
#                return redirect('CipollinoSys.views.error')
#
#    else:
#        print ('7')
#        form = AuthenticationForm()
#    return render(request, 'CipollinoSys/log_in.html', {'form' : form } )

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        print (form.is_valid(), form.errors, type(form.errors))
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user.is_active:
                login(request, user)
                return redirect('CipollinoSys.views.all_tasks')
        else:
            return redirect('CipollinoSys.views.error')
    else:
        form = AuthenticationForm()
    return render(request, 'CipollinoSys/log_in.html', {'form':form})


def error(request):
    return render(request, 'CipollinoSys/error.html')

def logout(request):
    auth.logout(request)
    # Перенаправление на страницу входа
    return redirect('CipollinoSys.views.log_in')



def users(request):
    results = []
    results.append(Results.objects.distinct('task_performer').count())
    results.append(Results.objects.distinct('task_performer'))


    return render(request, 'CipollinoSys/users.html', {'results' : results})


def view_statistic(request, pk):

    user = get_object_or_404(User, pk=pk)
    print (user)
    results = []
    results.append(user.username)
    results.append(Results.objects.filter(task_performer = user))
    results.append(Results.objects.filter(task_performer = user).count())
    results.append(str(Task.objects.exclude(deadline__gt=datetime.date(2016, 5, 26), task_performer = user).count()))
    results.append(Task.objects.filter(status='Выполнено',task_performer = user).count())
    results.append((Task.objects.distinct('wasted_time').count())*9)



    return render(request, 'CipollinoSys/view_statistic.html', {'results': results } )


def task_stat(request):
    tresult = []
    print (Task.objects.filter(status = 'Новая').count())
    tresult.append(str(Task.objects.filter(status = 'Новая').count()))
    tresult.append(Task.objects.filter(status='Выполнено').count())
    tresult.append(str(Task.objects.exclude(deadline__gt = datetime.date(2016, 5, 26)).count()))

    print (tresult[2])


    return render(request, 'CipollinoSys/task_stat.html', {'tresult': tresult })