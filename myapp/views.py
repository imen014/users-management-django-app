from django.shortcuts import render

from myapp.forms import MyFirstForm
from myapp.models import TestModel1


def myfirstView(request):
    return render(request, 'myapp/myfirstView.html')

def showForm(request):
    my_form = MyFirstForm()
    return render(request,
                  'myapp/form1.html',
                  {'my_form':my_form})

def post_showForm(request):
    my_form = MyFirstForm()
    saved_form = TestModel1()
    if request.method == 'POST':
        my_form = MyFirstForm(request.POST)
        if my_form.is_valid():
            username = my_form.cleaned_data['username']
            password = my_form.cleaned_data['password']
            email = my_form.cleaned_data['email']
            
            saved_form.username = username
            saved_form.password = password
            saved_form.email = email
            saved_form.save()
            message = "form saved succefully !"
        else:
            message = "form invalide !"
            my_form = MyFirstForm()
    else:
        message="verify method !"

    return render(request,
                  'myapp/form_result.html',
                  {'message':message,
                   'username':username,
                   'email': email})

def get_objects_from_db(request):
    instances = TestModel1.objects.all()
    return render(request,
                  'myapp/instances_from_db.html',
                  {'instances':instances})   

def getUserFromDb(request, id):
    user = TestModel1.objects.get(id=id)
    return render(request,
                  'myapp/getUser.html',
                  {'user':user})





def showUpdateForm(request, id):
    instance_to_update = TestModel1.objects.get(id=id)
    my_form = MyFirstForm(instance=instance_to_update)
    return render(request,
                  'myapp/form_modify.html',
                  {'my_form':my_form,
                   'instance_to_update':instance_to_update})

def updateUserForm(request, id):
    instance_to_update = TestModel1.objects.get(id=id)
    my_form = MyFirstForm(instance_to_update)
    
    if request.method == 'POST':
        
        if my_form.is_valid():
            newUsername = my_form.cleaned_data['username']
            newPassword = my_form.cleaned_data['password']
            newEmail = my_form.cleaned_data['email']
            
            instance_to_update.username = newUsername
            instance_to_update.password = newPassword
            instance_to_update.email = newEmail
            instance_to_update.save()
            message = "form modified succefully !"
        else:
            message = "form invalide !"
            my_form = MyFirstForm()
    else:
        message="verify method !"

    return render(request,
                  'myapp/update_form_result.html',
                  {'message':message,
                   'username':newUsername,
                   'email': newEmail})