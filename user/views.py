from django.shortcuts import render
from http import *
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    nbdata=newbatches.objects.all().order_by('-id')
    sdata=slider.objects.all().order_by('-id')
    mydict={"nbdata":nbdata,"sd":sdata,}
    return render(request,'user/index.html',mydict)

def contact(request):
    if request.method=="POST":
        a=request.POST.get('name')
        b= request.POST.get('email')
        c= request.POST.get('mobile')
        d= request.POST.get('msg')
        contactus(name=a,email=b,mobile=c,message=d).save()
        return HttpResponse("<script>alert('Thanks for contacting with us..');location.href='/user/contact'</script>")
    return render(request,'user/contact.html')

def registration(request):
    bdata=studentbatch.objects.all()
    md={"bdata":bdata,}
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        passwd=request.POST.get('passwd')
        college=request.POST.get('college')
        course=request.POST.get('course')
        pyear=request.POST.get('pyear')
        picture=request.FILES['fu']
        batch=request.POST.get('batch')
        x=signup.objects.filter(email=email).count()
        if x==0:
            signup(name=name,email=email,mobile=mobile,passwd=passwd,college=college,course=course,pyear=pyear,profile=picture,status='Pending', batchid=batch).save()
            return HttpResponse("<script>alert('You are registered successfully..'); location.href='/registration/'</script>")
        else:
            return HttpResponse("<script>alert('you are already registered..'); location.href='/registration/'</script>")
    return render(request,'user/registration.html',md)

def home(request):
    return render(request,'user/home.html')

def aboutus(request):
    return render(request,'user/about.html')

def batches(request):
    bdata=newbatches.objects.all()
    md={'bdata':bdata}
    return render(request,'user/batches.html',md)

def facility(request):
    return render(request,'user/facility.html')

def ourplacement(request):
    clg=request.GET.get('college')
    year=request.GET.get('year')
    if clg is not None and year is not None:
        pdata= placement.objects.filter(college=clg,session=year) 
    else:
        pdata=placement.objects.all()
    collegedata=college.objects.all().order_by('-id')
    sdata=session_year.objects.all().order_by('-id')
    md={"cdata":collegedata,"pdata":pdata,"sdata":sdata}
    return render(request,'user/placement.html',md)

def feedback(request):
    return render(request,'user/feedback.html')

def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        passwd=request.POST.get('passwd')
        x=signup.objects.filter(passwd=passwd,email=email).count()
        if x==1:
            request.session['user']=email
            y=signup.objects.filter(email=email,passwd=passwd)
            request.session['userpic']=str(y[0].profile)
            request.session['username']=str(y[0].name)
            request.session['batchid']=str(y[0].batchid)
            return HttpResponse("<script>location.href='/student/index/'</script>")
        else:
            return HttpResponse("<script>alert('Your username or password is inacorrect..');location.href='/user/login/'</script>")
    return render(request,'user/login.html')