from django.db import models
class Students(models.Model):
    first_name = models.CharField(max_length=10,null = True ,blank = True)
    last_name = models.CharField(max_length=10,null = True ,blank = True)
    date_of_birth = models.IntegerField(max_length=10,null = True ,blank = True)
    mobile = models.IntegerField(max_length=10,null = True ,blank = True)
    GENDER_TYPES = (
        (1, 'male'),
        (2, 'female'),
        (3, 'other'),
    )
    GENDER_TYPES = models.IntegerField(
        choices = GENDER_TYPES
    )        

    def __str__(self):
        return str(self.last_name)


class Orders(models.Model):
    order_name = models.CharField(max_length=10,null = True ,blank = True)
    order_price = models.IntegerField(max_length=10,null = True ,blank = True)
    order_discount = models.IntegerField(max_length=10,null = True ,blank = True)
    order_quantity_od_order = models.IntegerField(max_length=10,null = True ,blank = True)
    order_adress = models.IntegerField(max_length=20,null = True ,blank = True)
    order_at = models.DateField(null = True ,blank = True)

    def __str__(self):
        return str(self.order_name)


class StudentsAdress(models.Model):
    students = models.ForeignKey(Students,on_delete = models.CASCADE,null = True)
    street_name = models.CharField(max_length=10,null = True ,blank = True)
    house_number=models.IntegerField(max_length=6,null = True ,blank = True)
    city=models.CharField(max_length=13,null = True ,blank = True)
    state = models.CharField(max_length=15,null = True ,blank = True)
    country=models.CharField(max_length=16,null = True ,blank = True)
    pin_code= models.CharField(max_length=10,null = True ,blank = True)

    def __str__(self):
        return str(self.street_name)
   

