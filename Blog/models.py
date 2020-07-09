from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=10000,null=True)
    content = models.TextField(max_length=2000000,null=True)
    image = models.ImageField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    name= models.CharField(max_length=1000,null=True)
    email = models.EmailField(max_length=1000,null=True)
    comment= models.TextField(null=True)
    post_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE,null=True)


class Projects(models.Model):
    status = (
        ('Active','Active'),
        ('Accomplished','Accomplished')
    )
    name = models.CharField(max_length=1000,null=True)
    image = models.ImageField(null=True,blank=True)
    description = models.TextField(max_length=1000,null=True)
    status = models.CharField(null=True,max_length=100,choices=status)
    github_link = models.URLField(max_length=10000,null=True)
    