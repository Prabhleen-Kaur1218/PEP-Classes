from django.db import models

from django.db import models
class blog(models.Model):
    Title= models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    
 
    def __str__(self):
        return self.Title
