from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.db.models import Q
from . import forms
from django.forms import modelformset_factory
from .models import products,user
import os
from django.utils.timezone import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
os.system('cls')
# Create your views here......

def ad(a,s):
    s=str(s)
    if (s in a) != True:
        a+=s+'-'
    return a
def listit(s):
    tem=s.split('-')
    tem=tem[:len(tem)-1]
    return(tem)
def delit(request,s):
    print('\n\nk\n\n')
    a=''
    k=listit(request.session['result'])
    for i in k:
        if i != s:
            a+=str(i)+'-'
    return a


date=''
def index(request):

    global date
    d=str(datetime.today())[:10]
    a=user.objects.get(id=0)

    """
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "stoct report for today: "+str(d)
    msg['From'] = a.email
    msg['To'] = a.email
    for i in match:
        msg1+='<tr><td>'+str(i.id)+'</td>'+'<td>'+str(i.name)+'</td>'+'<td>'+str(i.distributor_email)+'</td>'+'<td>'+str(i.total_quantity)+'</td></tr>\n'

    #'''
    print(msg1)
    part2 = MIMEText(msg1, 'html')
    msg.attach(part2)
    s =smtplib.SMTP('smtp.gmail.com:587')#'smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('freefresh012@gmail.com','itismypas')
    s.sendmail(a.email, a.email, msg.as_string())
    s.quit()
"""


    if d!=date:
        match=products.objects.filter(Q(expected_date_for_new_stock__icontains=d))
        print(match)
        date=d
        #'''
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "stoct report for today: "+str(d)
            msg['From'] = a.email
            msg['To'] = a.email

            if match!=[]:
                msg1="""
                <table style="
    border: 1px solid black;
    text-align: center;
    border-collapse: collapse;">



      <tr style="
    	border: 1px solid black;
    	text-align: center;
    	background-color: #7fcce9;
    	">
        <th style="
	border: 1px solid black;
  border-collapse: collapse;">ID</th>
        <th style="
	border: 1px solid black;
  border-collapse: collapse;"> PRODUCT NAME</th>
    	<th style="
	border: 1px solid black;"> DISTRIBUTOR EMAIL</th>
    	<th style="
	border: 1px solid black;
  border-collapse: collapse;">STOCK LEFT</th>
      </tr>
                    """
                for i in match:
                    msg1+='<tr>'+'''<td style="
	border: 1px solid black;
  border-collapse: collapse;">'''+str(i.id)+'</td>'+'''<td style="
	border: 1px solid black;
  border-collapse: collapse;">'''+str(i.name)+'</td>'+'''<td style="
	border: 1px solid black;
  border-collapse: collapse;">'''+str(i.distributor_email)+'</td>'+'''<td style="
	border: 1px solid black;
  border-collapse: collapse;">'''+str(i.total_quantity)+'</td></tr>\n'
                msg1+='</table>'
                print(msg1)
                part2 = MIMEText(msg1, 'html')
                msg.attach(part2)
                s =smtplib.SMTP('smtp.gmail.com:587')#'smtp.gmail.com',587)
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(a.email,a.pas)
                s.sendmail(a.email, a.email, msg.as_string())
                s.quit()

        except:
            print('error1')
            pass
    return render(request,'index.html',context={'insert':"hellow world"})
#'''
def product_entry_page(request):
    form=forms.product_entry()
    if (request.method=='POST'):
        form=forms.product_entry(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form=forms.product_entry()
            return render(request,'product_entry.html',context={"form":form})
        else:
            print('\n\nerror\n\n')
    return render(request,'product_entry.html',context={"form":form})


def search(request):
    form=forms.search()
    if (request.method=='POST'):
        form=forms.search(request.POST)
        if form.is_valid():
            #print('\n(1)\n',form,'\n\n')
            if (form.cleaned_data['ref']=='mel'):
                match=[]
                list_name=[]
                list=[
                form.cleaned_data['id'],
                form.cleaned_data['name'],
                form.cleaned_data['purchase_date'],
                form.cleaned_data['quantity'],
                form.cleaned_data['total_quantity'],
                form.cleaned_data['base_price'],
                form.cleaned_data['description'],
                form.cleaned_data['distributor_name'],
                form.cleaned_data['distributor_no'],
                form.cleaned_data['expected_date_for_new_stock'],
                form.cleaned_data['distributor_email']]

                if list[0]!=None:
                    match+=products.objects.filter(Q(id__icontains=list[0]))
                if list[1]!='':
                    match+=products.objects.filter(Q(name__icontains=list[1]))
                if list[2]!=None:
                    match+products.objects.filter(Q(purchase_date__icontains=list[2]))
                if list[3]!=None:
                    match+=products.objects.filter(Q(quantity__icontains=list[3]))
                if list[4]!=None:
                    match+=products.objects.filter(Q(total_quantity__icontains=list[4]))
                if list[5]!=None:
                    match+=products.objects.filter(Q(base_price__icontains=list[5]))
                if list[6]!='':
                    match+=products.objects.filter(Q(description__icontains=list[6]))
                if list[7]!='':
                    match+=products.objects.filter(Q(distributor_name__icontains=list[7]))
                if list[8]!=None:
                    match+=products.objects.filter(Q(distributor_no__icontains=list[8]))
                if list[9]!=None:
                    match+=products.objects.filter(Q(expected_date_for_new_stock__icontains=list[9]))
                if list[10]!='':
                    match+=products.objects.filter(Q(distributor_email__icontains=list[10]))
                tem=''
                for i in match:
                    print(i.id)
                    tem=ad(tem,i.id)
                request.session['result']=tem
                print(tem)
                return redirect('result/')
    return render(request,'search.html',context={"form":form})
def del_object(request, pk):

        #print('\nIN------------\n ')
        post=get_object_or_404(products,pk=pk)
        #print('check=',request.POST.getlist('checks'))
        post.delete()
        request.session['result']=delit(request,pk)
        return redirect('/search/result/')#redirect('/redirect-success/')
#redirect('/dsfasd',m)


def result(request):
    rearsh_result =[]
    if request.session['result']!='':
        for i in listit(request.session['result']):
            rearsh_result.append(get_object_or_404(products,pk=i))

        form=forms.resultt()
        #print('delit=',delit(request,'0'))

        if (request.method=='POST'):
            form=forms.resultt(request.POST)
            if form.is_valid():
                l=[
                form.cleaned_data['list'],
                form.cleaned_data['Action']
                ]
                print('\n{yoo}\n',l,'\n\n')

                if l[1]=='1':
                    print('\nl[1]\n')
                    t=[]
                    for i in listit(l[0]):
                        t.append(get_object_or_404(products,pk=i))
                        request.session['result']=delit(request,i)
                        print("request.session['result']=",request.session['result'])
                    for i in t:
                        i.delete()

                    return redirect('result/')
                if l[1]=='2':
                    print('yooooooooooo')
                    a=user.objects.get(id=0)
                    per=[]
                    a=user.objects.get(id=0)#'supplier we need to buy more stuff from you'
                    msg=a.msg
                    for i in listit(l[0]):
                        t=(get_object_or_404(products,pk=i))
                        per.append(t.distributor_email)
                    print(per)
                    try:
                        emaillist = [elem.strip().split(',') for elem in per]
                        server = smtplib.SMTP("smtp.gmail.com:587")
                        server.ehlo()
                        server.starttls()
                        server.login(a.email, a.pas)
                        server.sendmail(a.email, emaillist, msg)#'''
                    except:
                        print('error')
                        pass


        print(rearsh_result[0].distributor_email)
        return render(request,'result.html',context={"result":rearsh_result,"form":form,'count':len(rearsh_result)})
    else:

        return render(request,'noresult.html')
def edit(request,pk):

    post=get_object_or_404(products,pk=pk)#object
    #forms.products(instance=post)
    form=forms.edit(initial={'id':post.id,
    'name':post.name,
    'purchase_date':post.purchase_date,
    'quantity':post.quantity,
    'total_quantity':post.total_quantity,
    'base_price':post.base_price,
    'description':post.description,
    'distributor_name':post.distributor_name,
    'distributor_no':post.distributor_no,
    'expected_date_for_new_stock':post.expected_date_for_new_stock,
    'old_quantity':post.old_quantity,
    'description':post.description,
    'remark':post.remark,
    'distributor_email':post.distributor_email})
    #print(form)
    #formsett=inlineformset_factory(post,products,fields='__all__')
    if (request.method=='POST'):
        print('\nin EDIT POST\n')
        form=forms.edit(request.POST)
        if form.is_valid() or 1==1:
            list=[
            form.cleaned_data['id'],
            form.cleaned_data['name'],
            form.cleaned_data['purchase_date'],
            form.cleaned_data['quantity'],
            form.cleaned_data['total_quantity'],
            form.cleaned_data['base_price'],
            form.cleaned_data['description'],
            form.cleaned_data['distributor_name'],
            form.cleaned_data['distributor_no'],
            form.cleaned_data['old_quantity'],
            form.cleaned_data['remark'],
            form.cleaned_data['expected_date_for_new_stock'],
            form.cleaned_data['distributor_email']]
            print(list)
            a=products.objects.get(id=pk)
            if list[0]!=None:
                a.id=list[0]
            if list[1]!=None:
                a.name=list[1]
            if list[2]!=None:
                a.purchase_date=list[2]
            if list[3]!=None:
                a.quantity=list[3]
            if list[4]!=None:
                a.total_quantity=list[4]
            if list[5]!=None:
                a.base_price=list[5]
            if list[6]!=None:
                a.description=list[6]
            if list[7]!=None:
                a.distributor_name=list[7]
            if list[8]!=None:
                a.distributor_no=list[8]
            if list[9]!=None:
                a.old_quantity=list[9]
            if list[10]!=None:
                a.remark=list[10]
            if list[11]!=None:
                a.expected_date_for_new_stock=list[11]
            if list[12]!=None:
                a.distributor_email=list[12]
            a.save()
            return redirect('/search/result/')
    #print (form,products.objects.filter(id=pk))
    return render(request,'edit.html',context={"form":form})
def setting(request):
    post=get_object_or_404(user,pk=0)
    form=forms.setting(initial={
    'name':post.name,
    'email':post.email,
    'pas':post.pas,
    'msg':post.msg})
    if (request.method=='POST'):
        print('\n\n','POST','\n\n')
        form=forms.setting(request.POST)
        if form.is_valid():
            list=[
            form.cleaned_data['name'],
            form.cleaned_data['email'],
            form.cleaned_data['pas'],
            form.cleaned_data['msg']
            ]
            print('\n\n',list,'\n\n')
            a=user.objects.get(id=0)
            if list[0]!=None:
                a.name=list[0]
            if list[1]!=None:
                a.email=list[1]
            if list[2]!=None:
                a.pas=list[2]
            if list[3]!=None:
                a.msg=list[3]
            a.save()
            return redirect('/')
    return render(request,'settings.html',context={"form":form})
