from django.shortcuts import render,redirect
from django.views import View
from account.models import Contact,Staff
from home.models import Students
from .forms import StudentForm
from django.contrib import messages
# Create your views here.

class Index(View):
    def get(self,request):
        return render(request,'home.html')

class Enquiry(View):
    def get(self,request):
        enquiry=Contact.objects.all()
        return render(request,'enquiry.html',{'customer':enquiry})

class Showstaffs(View):
    def get(self,request):
        staffs=Staff.objects.all()
        return render(request,'showstaff.html',{'allstaffs':staffs})

class Addstudent(View):
    def get(self,request):
        std1=StudentForm()
        return render(request,'addstudents.html',{'form':std1})
    def post(self,request):
        std1=StudentForm(request.POST)
        if std1.is_valid():
            std1.save()
            student=Students.objects.all()
            return render(request,'showstudents.html',{'form':student})
        else:
            messages.info(request,'student is not valid')
            return redirect('Addstudent')

class Showstudents(View):
    def get(self,request):
        students=Students.objects.all()
        return render(request,'showstudents.html',{'form':students})

class Editstudent(View):
    def get(self,request):
        edit1=request.GET['edit']
        student_details=Students.objects.filter(student_id=edit1)
        return render(request,'editstudent.html',{'student':student_details})
    def post(self,request):
        stdid=request.POST['id']
        stdname=request.POST['name']
        stdph=request.POST['phone']
        stdemail=request.POST['email']
        stdaddress=request.POST['address']
        stdplace=request.POST['place']
        Students.objects.filter(student_id=stdid).update(student_name=stdname,student_phone=stdph,student_email=stdemail,student_address=stdaddress,student_place=stdplace)
        student=Students.objects.all()
        return render(request,'showstudents.html',{'form':student})

class Deletestudent(View):
    def get(self,request):
        deletestd=request.GET['edit']
        Students.objects.filter(student_id=deletestd).delete()
        student=Students.objects.all()
        return render(request,'showstudents.html',{'form':student})



class Profile(View):
    def get(self,request):
        if request.session['email'] is not None:
            customer = Staff.objects.filter(email=request.session['email'])
        return render(request,'profile.html',{'customer':customer})
    def post(self,request):
        print('///////////')
        edit1 = request.session['email']
        if request.method == 'POST':
            username=request.POST['name']
            phone=request.POST['phone']
            Staff.objects.filter(email=edit1).update(name=username,phno=phone)
            customer = Staff.objects.filter(email=request.session['email'])
            return render(request,'profile.html',{'customer':customer})


