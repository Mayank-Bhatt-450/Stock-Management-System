from django import forms
from .models import user,products
from django.contrib.auth.forms import UserChangeForm
class product_entry(forms.ModelForm):
    class Meta():
        model= products
        fields= '__all__'
class search(forms.Form):
    id= forms.IntegerField(required=False)
    name=forms.CharField(required=False)
    purchase_date=forms.DateField(required=False)
    quantity= forms.IntegerField(required=False)
    total_quantity= forms.IntegerField(required=False)
    base_price= forms.IntegerField(required=False)
    description=forms.CharField(required=False)
    distributor_name=forms.CharField(required=False)
    distributor_no=forms.IntegerField(required=False)
    expected_date_for_new_stock=forms.DateField(required=False)
    ref=forms.CharField(required=False,widget=forms.HiddenInput,initial='mel')
    distributor_email=forms.EmailField(required=False)

class edit(forms.Form):
    id= forms.IntegerField(required=False)
    name=forms.CharField(required=False)
    purchase_date=forms.DateField(required=False)
    old_quantity= forms.IntegerField(required=False)
    quantity= forms.IntegerField(required=False)
    total_quantity= forms.IntegerField(required=False)
    base_price= forms.IntegerField(required=False)
    description=forms.CharField(required=False)
    distributor_name=forms.CharField(required=False)
    distributor_no=forms.IntegerField(required=False)
    remark=forms.CharField(required=False)
    expected_date_for_new_stock=forms.DateField(required=False)
    distributor_email=forms.EmailField(required=False)
class resultt(forms.Form):
    list=forms.CharField(required=False,widget=forms.HiddenInput)#forms.CharField(required=False,widget=forms.HiddenInput,initial='')

    options= [
    ('0', '―――SELECT―――'),
    ('1', 'Delete'),
    ('2', 'send reminder email')
    ]
    Action= forms.CharField(widget=forms.Select(choices=options))
class setting(forms.ModelForm):
    class Meta():
        model= user
        fields=('name','email','pas','msg')
        #widgets={'passwprd':forms.PasswordInput()}
        widget={'pas':forms.PasswordInput()}
