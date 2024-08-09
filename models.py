from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.name
    

    
class Author(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    
    def __str__(self):
        return self.user.first_name + " | " + self.user.last_name
    
class Blog(models.Model):
    title = models.CharField(max_length = 145)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True)
    last_edit = models.DateField(auto_now=True)
    image = models.ImageField(null= True,blank=True)
    
    def __str__(self):
        return self.title + " | " + self.category.name

    
    @property         
    def imageURL(self):
        url=""                 
        try:  
            url = self.image.url
        except:
            url =""
            
        return url
    
    

    
    
    
