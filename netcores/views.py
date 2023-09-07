from django.shortcuts import render,HttpResponse,HttpResponseRedirect, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.


def signup(request):
    
    if request.method == 'POST':
        fm = signUp(request.POST)
        uname = request.POST.get('username')
        upass = request.POST.get('password')
            
    #         singUpObj = signUp(username = uname, password = upass)
    #         singUpObj.save()
    #     else:    
    #         fm = signUp()
    return render(request, 'login.html')



def login_view(request):
    
    if not request.user.is_authenticated:   
        if request.method == 'POST':
            fm = UserLogin( request = request, data = request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                userObj = authenticate(username=uname, password =upass)
                if userObj is not None:
                    login(request,userObj)
                    return HttpResponseRedirect('/dashboard/')     
        else:
            fm = UserLogin()
        return render(request,'login.html', {'form' :fm})

    else:
        return HttpResponseRedirect('/dashboard/')    
    
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')    
    
    
    
    
def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')    
    else:
        return HttpResponseRedirect('/')

def add_invoice(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            clientFm = ClientForm(request.POST)

            if clientFm.is_valid():
                comp = clientFm.cleaned_data['company_name']
                gst = clientFm.cleaned_data['gst_number']
                cntry = clientFm.cleaned_data['country']
                sts = clientFm.cleaned_data['state']
                add = clientFm.cleaned_data['address']

                obj = Client(company_name=comp,gst_number=gst,country=cntry,state=sts,address=add)
                obj.save()

                messages.success(request,"Your 'Client' form has been saved successfully.")

                clientFm = ClientForm()

        else:
            clientFm = ClientForm()  

        return render(request,'addInvoice.html',{'clientFm':clientFm})   



    else:
        return HttpResponseRedirect('/')
  

def add_invoice2(request):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            serviceFm = ServicesForm(request.POST)

            if serviceFm.is_valid():
                cname = serviceFm.cleaned_data['client']
                ser = serviceFm.cleaned_data['description']
                qty = serviceFm.cleaned_data['quantity']
                amt = serviceFm.cleaned_data['amount']
                

                serobj = Services(client=cname, description=ser,quantity=qty,amount=amt)
                serobj.save()

                messages.success(request,"Your 'Client' form has been saved successfully.")

                serviceFm = ServicesForm()

        else:
            serviceFm = ServicesForm()  

        return render(request,'addinvoice.html',{'serviceFm':serviceFm})   



    else:
        return HttpResponseRedirect('/')  
    


def serviceProvider(request):
    allCompany = Company.objects.all()
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = ServiceProviderForm(request.POST)
            if fm.is_valid():
                cnm = fm.cleaned_data['client']    
                comp = fm.cleaned_data['company_name']    
                hby = fm.cleaned_data['handle_by']    
                em = fm.cleaned_data['email']    
                ph = fm.cleaned_data['phone']    
                acc = fm.cleaned_data['account_number']    
                ifsc = fm.cleaned_data['ifsc_code']    
                bnk = fm.cleaned_data['bank_name']    
                gst = fm.cleaned_data['gst_number'] 
                
                obj = Company(client=cnm, company_name=comp, handle_by=hby, email = em, phone= ph,
                              account_number= acc, ifsc_code = ifsc, bank_name = bnk, gst_number = gst)
                
                obj.save()
                messages.success(
                    request,'Your form has been saved successfully.'
                )
                fm = ServiceProviderForm()
        else:
            fm = ServiceProviderForm()
            
        return render(request,'company.html', {'form': fm, 'data':allCompany})    
            
    else:
        return HttpResponseRedirect('/')

def update_company(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Company.objects.get(pk = id)
            fm = ServiceProviderForm(request.POST, instance=obj)
            if fm.is_valid():
                fm.save()
                messages.success(
                    request,"Successfully updated, you can go back"
                )
        else:
            obj = Company.objects.get(pk = id)
            fm = ServiceProviderForm(instance = obj)
        
        return render(request,'update_comp.html', {'form':fm})            
    
    else:
        return HttpResponseRedirect('/')
    
    
    
    

def delete_company(request, id):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            obj = Company.objects.get(pk=id)
            obj.delete()
        return HttpResponseRedirect('/service_provider/')    
    
    else:
        return HttpResponseRedirect('/')        
            

    
    
    
def all_list(request):
    if request.user.is_authenticated:
        allclient = Client.objects.all()
        
        return render(request,'reviewInvoice.html', {'allclient':allclient})                    
    
    else:
        return HttpResponseRedirect('/')
    
def update_client(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Client.objects.get(pk = id)
            fm = ClientForm(request.POST, instance=obj)
            if fm.is_valid():
                fm.save()
                messages.success(
                    request,"Successfully updated, you can go back"
                )
        else:
            obj = Client.objects.get(pk = id)
            fm = ClientForm(instance = obj)
        
        return render(request,'update_client.html', {'form':fm})            
    
    else:
        return HttpResponseRedirect('/')
  


    
def delete_client(request, id):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            obj = Client.objects.get(pk=id)
            obj.delete()
        return HttpResponseRedirect('/all_list/')    
    
    else:
        return HttpResponseRedirect('/')    
    
    
    
def review(request,pk):
    if request.user.is_authenticated:
        
        clientData = Client.objects.get(id = pk)
        
        try:
            companyData = Company.objects.get(client_id = pk)
        except Company.DoesNotExist:
            companyData = {'Key':'val'}
            
            
        try :
            servicesData = Services.objects.filter(client_id = pk)
        except Services.DoesNotExist:
            servicesData = {'Key':'val'}
            
            
            
        context = {'clientData':clientData, 'companyData':companyData
                   ,'servicesData':servicesData}
        
        
        return render (request,'review.html', context)
    
    else:
        return HttpResponseRedirect('/')       


def update_services(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Services.objects.get(pk = id)
            fm = ServicesForm(request.POST, instance=obj)
            if fm.is_valid():
                fm.save()
                messages.success(
                    request,"Successfully updated, you can go back"
                )
        else:
            obj = Services.objects.get(pk = id)
            fm = ServicesForm(instance = obj)
        
        return render(request,'update_client.html', {'form':fm})            
    
    else:
        return HttpResponseRedirect('/')
  

    

def delete_services(request, id):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            obj = Services.objects.get(pk=id)
            obj.delete()
        return HttpResponseRedirect('/review/')    
    
    else:
        return HttpResponseRedirect('/')    
     
    


def invoice_report(request):
    if request.user.is_authenticated:
        allclient = Client.objects.all()
        
        return render(request,'invoice_report.html', {'allclient':allclient})                    
    
    else:
        return HttpResponseRedirect('/')    
    
    
    
def gst_report(request,pk):
    if request.user.is_authenticated:
        
        clientData = Client.objects.get(id = pk)
        
        
        try:
            companyData = Company.objects.get(client_id = pk)
        except Company.DoesNotExist:
            companyData = {'Key':'val'}
            
            
        try :
            servicesData = Services.objects.filter(client_id = pk)
        except Services.DoesNotExist:
            servicesData = {'Key':'val'}  
            
            
        context = {'clientData':clientData, 'companyData':companyData
                   ,'servicesData':servicesData}
        
        
        return render (request,'gst_report.html', context)
    
    else:
        return HttpResponseRedirect('/')       
           

            
                