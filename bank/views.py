from django.shortcuts import render, redirect
from django.urls import reverse
from bank.forms import customer_details,createform,CreditForm,NewUserForm,DebitForm,Balance_enquiryForm
from bank.models import customers,user
from decimal import Decimal

# Create your views here.
def yod(request):
    return render(request,"bk.html")
def cus(request):
    a = customer_details()
    return render(request,"csform.html",{'c':a})
def debi(request):
    b = customer_details()
    return render(request,"deb.html",{'t': b})
def dat(request):
    obj1 = customers.objects.all()
    return render(request,"ins.html",{'d':obj1})
def homepage(request):
    return render(request,'home.html')
def cere(request):
    r = createform()
    if request.method == 'POST':
        r = createform(request.POST)
        if r.is_valid():
            p = r.save()
            return redirect(reverse('bank:actionpage',kwargs=
                {'Account_no': p.Account_no,
                 'Customer_NAME': p.Customer_NAME,
                 'Balance': str(p.Balance) }))
    return render(request,"fr.html",{'b':r})
def actionpage(request,Account_no,Customer_NAME,Balance):
    ac = {'Account_no':Account_no,'Customer_NAME':Customer_NAME,'Balance':Decimal(Balance)}
    return render(request,'action_page.html',ac)
def credit(request,Account_no = None):
    form = CreditForm()
    if request.method == 'POST':
        form = CreditForm(request.POST)
        if form.is_valid():
            Account_no = form.cleaned_data['Account_no']
            Amount = form.cleaned_data['Amount']
            try:
                customer = customers.objects.get(Account_no = Account_no)
            except customers.DoesNotExist:
                return render(request, 'credit_form.html',{'form':form, 'error_message': 'Account not found.'})
            customer.Balance += Amount
            customer.save()
            return redirect(reverse('bank:success_page', kwargs={
                'Account_no': customer.Account_no,
                'Customer_NAME': customer.Customer_NAME,
                'Balance': customer.Balance}))
    else:
        return render(request,"credit_form.html",{'form':form})
def success_page(request, Account_no, Customer_NAME, Balance):
    s = {'Account_no':Account_no,'Customer_NAME':Customer_NAME,'Balance':Decimal(Balance)}
    return render(request, 'success.html',s)

def Debit(request, Account_no = None):
    d = DebitForm()
    if request.method == 'POST':
        d = DebitForm(request.POST)
        if d.is_valid():
            Account_no = d.cleaned_data['Account_no']
            Amount = d.cleaned_data['Amount']
            try:
                c = customers.objects.get(Account_no = Account_no)
            except customers.DoesNotExist:
                return render(request, 'debit_form.html',{'f':d,'error_message':'Account not found'})
            c.Balance -= Amount
            c.save()
            return redirect(reverse('bank:success_page', kwargs={
                'Account_no':c.Account_no,
                'Customer_NAME':c.Customer_NAME,
                'Balance':str(c.Balance)}))
    else:
        return render(request,'debit_form.html',{'f':d})

def balance_enquiry(request):
    e = Balance_enquiryForm()
    bal = None
    error_message = None
    if request.method == 'POST':
        e = Balance_enquiryForm(request.POST)
        if e.is_valid():
            Account_no = e.cleaned_data['Account_no']
            try:
                q = customers.objects.get(Account_no = Account_no)
                bal = q.Balance
            except customers.DoesNotExist:
                error_message = 'Account not found'
    eq = {'e':e,'bal':bal,'error_message': error_message}
    return render(request,'bal_enquiry.html',eq)

def nuser(request):
    un = NewUserForm()
    return render(request,"nuser.html",{'s':un})
def newuser(request):
    if request.method == 'POST':
        n = NewUserForm(request.POST)
        if n.is_valid():
            n.save()
            return nuser(request)
    else:
        n = NewUserForm()
    return render(request,"newuser.html",{'u':n})

def c_user(request):
    if request.method == 'POST':
        f = user(request.POST)
        if f.is_valid():
            f.save()    
            return redirect(user_created)
    else:
        f = user()
    return render(request,'cuser.html',{'form':f})
def user_created(request):
    return render(request,'user_created.html')