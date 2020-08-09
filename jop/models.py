from django.db import models

# Create your models here.

JOP_TYPE = (
    ("Full Time","Full Time"),
    ("Part Time","Part Time"),


)

def image_upload (instance , filename):
    imagename , extenstion = filename.split(".")
    return "jop_image/%s.%s"%(instance.id,extenstion) 

class Jop (models.Model): #Table
    title = models.CharField (max_length=100) #column
    #location
    jop_type = models.CharField (max_length=15 , choices=JOP_TYPE)
    
    jop_description = models.TextField (max_length=1000)
    
    published_at = models.DateField (auto_now=True)

    vacancy = models.IntegerField (default= 1)

    salary = models.IntegerField (default= 0)

    experience = models.IntegerField (default=1)

    category = models.ForeignKey ('Category' , on_delete = models.CASCADE)

    jop_image = models.ImageField (upload_to = image_upload , default = "")

    def __str__ (self):
        return self.title 

class Category (models.Model):
    name = models.CharField (max_length=25)

    def __str__(self):
        return self.name
