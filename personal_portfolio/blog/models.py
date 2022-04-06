from django.db import models

# Create your models here.




class BlogPost(models.Model):
    post_date= models.DateField()
    title= models.TextField()
    post_text = models.CharField(max_length=1000)
    

    def __str__(self):
        return self.title