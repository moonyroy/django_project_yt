from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True , null=True , blank=True)
    author = models.ForeignKey(User , on_delete = models.CASCADE , null=True , blank=True)
    image = models.ImageField(upload_to = '%Y/%m/%d' ,null=True , blank=True )
    likes = models.ManyToManyField(User , related_name='BlogLikes' , blank=True)

    def __str__(self):
        return self.title

    def getsnippet(self):
        return self.content[0:30] + '...'