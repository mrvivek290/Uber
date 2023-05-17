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


class Orders(models.Model):
    order_name = models.CharField(max_length=10,null = True ,blank = True)
    order_price = models.IntegerField(max_length=10,null = True ,blank = True)
    order_discount = models.IntegerField(max_length=10,null = True ,blank = True)
    order_quantity_od_order = models.IntegerField(max_length=10,null = True ,blank = True)
    order_adress = models.IntegerField(max_length=10,null = True ,blank = True)
    order_at = models.DateField(null = True ,blank = True)
