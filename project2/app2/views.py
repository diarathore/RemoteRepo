from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from .models import RegistrationData,UploadFetch,ProductData
from .forms import RegistrationForm,LoginForm,UploadFetchForm,Inserting_data,Updating_data,Deleting_data
from django.http.response import HttpResponse

def registration_view(request):
    if request.method=='POST':
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
           firstname= request.POST.get('firstname')
           lastname= request.POST.get('lastname')
           username= request.POST.get('username')
           password= request.POST.get('password')
           location= request.POST.get('location')
           mobile= request.POST.get('mobile')
           email= request.POST.get('email')

           data=RegistrationData(
               firstname=firstname,
               lastname=lastname,
               username=username,
               password=password,
               location=location,
               mobile=mobile,
               email=email
           )
           data.save()
           lform=LoginForm()
           return render(request,'login.html',{'lform':lform})
        else:
            return HttpResponse("No Data")
    else:
        rform=RegistrationForm()
        return render(request,'register.html',{'rform':rform})

def login_view(request):
    if request.method=='POST':
        lform=LoginForm(request.POST)
        if lform.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')

            uname=RegistrationData.objects.filter(username=username)
            pwd=RegistrationData.objects.filter(password=password)

            if uname and pwd :
                return redirect(upload_fetch_view)
            else:
                return HttpResponse("Login Failed")
        else:
            return HttpResponse("User Invaild Data")
    else:
        lform=LoginForm()
        return render(request,'login.html',{'lform':lform})


def upload_fetch_view(request):
    if request.method == "POST":
        form = UploadFetchForm(request.POST, request.FILES)
        if form.is_valid():
            name = request.POST.get('name')
            img = form.cleaned_data.get('upload_img')

            data = UploadFetch(name=name, upload_img=img)
            data.save()
            form = UploadFetchForm()
            return render(request, 'home.html', {'form': form})
    else:
        form = UploadFetchForm()
        return render(request, 'home.html', {'form': form})


def images(request):
    imgs = UploadFetch.objects.all()
    return render(request, 'disp_data.html', {'imgs': imgs})

def contact_view(request):
        if request.method == 'POST':
            iform = Inserting_data(request.POST)
            if iform.is_valid():
                product_id = request.POST.get('product_id')
                product_name = request.POST.get('product_name')
                product_class = request.POST.get('product_class')
                product_color = request.POST.get('product_color')
                product_cost = request.POST.get('product_cost')

                data1 = ProductData(
                    product_id=product_id,
                    product_name=product_name,
                    product_class=product_class,
                    product_color=product_color,
                    product_cost=product_cost
                )
                data1.save()
                iform = Inserting_data()
                return render(request, 'contact.html', {'iform': iform})
            else:
                return HttpResponse("User Invaild Data")

        else:
            iform = Inserting_data()
            return render(request, 'contact.html', {'iform': iform})

def about_view(request):
    return render(request,'about.html')

def table_view(request):
    product = ProductData.objects.all()
    paginator = Paginator(product, 3)
    page = request.GET.get('page')
    product = paginator.get_page(page)
    return render(request, 'table.html', {'product': product})

def feedback_view(request):
    product = ProductData.objects.all()
    return render(request, 'feedback.html', {'product': product})

def edit(request, id):
    if request.method=="POST":
        eform=Updating_data(request.POST,instance=id)
        if eform.is_valid():
            eform.save()
            return render(request,'table.html')
        else:
            eform=Updating_data(instance=id)
            return render(request,'update.html',{'eform':eform})

def update_view(request,id):
            pdata =ProductData.objects.get(pid=id)
            pdata.product_id=request.POST['product_id']
            pdata.product_name=request.POST['product_name']
            pdata.product_class=request.POST['product_class']
            pdata.product_color=request.POST['product_color']
            pdata.product_cost=request.POST['product_cost']
            pdata.save()
            return render(request,"update.html",{'pdata':pdata})

def delete_view(request):
    if request.method=="POST":
        dform=Deleting_data(request.POST)
        if dform.is_valid():
            product_id=request.POST.get('product_id')
            pdata=ProductData.objects.filter(product_id=product_id)
            if pdata:
               pdata.delete()
               dform=Deleting_data()
               return render(request,'delete.html',{'dform':dform})
            else:
               return HttpResponse("Invalid Product Id")
        else:
            return HttpResponse("User Invalid Data")
    else:
        dform=Deleting_data()
        return render(request,'delete.html',{'dform':dform})