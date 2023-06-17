from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class newsletter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    number = models.IntegerField()
    # service = models.CharField(max_length=100)
    SERVICE=(
        ('Web Designing','Web Designing'),
        ('Email Marketing','Email Marketing'),
        ('SEO','SEO'),
    )
    service_options=models.CharField(choices=SERVICE,max_length=200,default="")
    specialNotes = models.TextField()
    def __str__(self):
        return self.name
    


class contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.TextField()
    message = models.TextField()  
    def __str__(self):
        return self.name
    

class product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/services/products", null=True)
    url = models.CharField(max_length=100, default=' ')