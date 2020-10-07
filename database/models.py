from django.db import models

# Create your models here.
class user(models.Model):
    id= models.IntegerField(primary_key=True)
    name =models.CharField(max_length=100)
    email=models.EmailField()
    pas =models.CharField(max_length=100)
    msg =models.CharField(max_length=240)
    def __str__(self):
        return (self.name)

class products(models.Model):
    id= models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    purchase_date=models.DateField()
    old_quantity= models.IntegerField()
    quantity= models.IntegerField()
    total_quantity= models.IntegerField()
    base_price= models.IntegerField()
    description=models.CharField(max_length=1000)
    distributor_name=models.CharField(max_length=100)
    distributor_no= models.IntegerField()
    remark=models.CharField(max_length=1000)
    expected_date_for_new_stock=models.DateField()
    distributor_email=models.EmailField()

    def __str__(self):
        return (str(self.id))
