from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

JOP_TYPE = (
    ("Full Time","Full Time"),
    ("Part Time","Part Time"),


)

def image_upload (instance , filename):
    imagename , extenstion = filename.split(".")
    return "jop_image/%s.%s"%(instance.id,extenstion) 

class Jop (models.Model): #Table
    owner = models.ForeignKey(User , related_name='job_owner',on_delete= models.CASCADE)
    title = models.CharField (max_length=100) #column
    #location
    jop_type = models.CharField (max_length=15 , choices=JOP_TYPE)

    jop_description = models.TextField (max_length=1000)
    
    published_at = models.DateField (auto_now=True)

    vacancy = models.IntegerField (default= 1)

    salary = models.IntegerField (default= 0)

    experience = models.IntegerField (default=1)

    category = models.ForeignKey ('Category' , on_delete = models.CASCADE)

    jop_image = models.ImageField (upload_to = image_upload , default = "",blank=True,null=True)

    slug = models.SlugField (blank=True , null= True )


    def save (self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(Jop,self).save(*args,**kwargs)
   
    def __str__ (self):
        return self.title

class Applyer(models.Model):
    job = models.ForeignKey("Jop" , related_name='apply_jop' , on_delete= models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    coverletter = models.TextField(max_length=500)
    created_at = models.DateField (auto_now=True)


    def __str__(self):
        return self.name

class Category (models.Model):
    name = models.CharField (max_length=25)

    def __str__(self):
        return self.name
