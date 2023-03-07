from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact,Course,Staff

# Create your views here.

def mainhome(request):
    return render (request,'mainhome.html')

def courses(request):
    courses={
    'course':Course.objects.all()
    }
    return render(request,'courses.html',courses)

def trainers(request):
    return render(request,'trainers.html')


def contact(request):
    if request.method == 'POST':
        if request.POST['name'] is not None:
            enq=Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phno=request.POST['phno'])
            enq.save()
            dicts={'out':1,'name':request.POST['name']}
            return render(request,'contact.html',dicts)
    return render (request,'contact.html')


def login(request):
    if request.method == 'POST':
        print('//////////')
        email = request.POST['email']
        password = request.POST['password']
        try:
            check_user = Staff.objects.get(email=email,password=password)
            request.session['email'] = check_user.email
            request.session['name'] = check_user.name
            request.session['phno'] = check_user.phno
            return redirect('index')
        except Staff.DoesNotExist:
            messages.error(request,'invalid data')
            return redirect('login')
    return render (request,'login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phno = request.POST['phno']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password==password2:
            if Staff.objects.filter(email = email).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            else:
                customer = Staff.objects.create(name=name,email=email,phno=phno,password=password)
                customer.save()
                messages.info(request,'user created')
                return redirect('login')
        else:
            messages.info(request,'password does not match')
            return redirect('signup')
    else:
        return render (request,'signup.html')

def forgpass(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if Staff.objects.filter(email=email).exists():
            Staff.objects.filter(email=email).update(password=password)
            return redirect('login')
        else:
            messages.error(request,'invalid data')
            return redirect('forgpass')
    return render(request,'forgetpass.html')

def logout(request):
    request.session.pop('email',None)
    request.session.pop('name',None)
    request.session.pop('phno',None)
    return render (request,'mainhome.html')


