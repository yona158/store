from django.db import models
from datetime import datetime

#Database table
class Product(models.Model):  

    category_choices=[
        ('phone','phone'),
        ('computer','computer'),
        ('head phone','head phone'),
    ]

    # afeter any modifying you should do makemigrations & migrate
    name=models.CharField(max_length=100,verbose_name='title')
    content=models.TextField(blank=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    image=models.ImageField(upload_to='photos/%y/%m/%d',default='photos/24/11/20/COLOR_WOW.png')
    active=models.BooleanField(default=True) 
    category=models.CharField(max_length=50,null=True,blank=True,choices=category_choices)

    def __str__(self): 
        return self.name
    
    class Meta:
        verbose_name='our product'   #change the title at admin pannel
        ordering=['-price'] # order them by price from high to low

class Test(models.Model):
    date=models.DateField()
    time=models.TimeField(null=True)
    created=models.DateTimeField(default=datetime.now)