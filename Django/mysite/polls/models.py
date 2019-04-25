from __future__ import unicode_literals
from django.db import models

class Choice(models.Model):
   
    name=models.CharField(db_column="name",max_length=100,blank=True,null=True)
    author=models.CharField(db_column="author",max_length=100,blank=True,null=True)
    publisher=models.CharField(db_column="publisher",max_length=100,blank=True,null=True)
    date=models.CharField(db_column="date",max_length=100,blank=True,null=True)
    price=models.CharField(db_column="price",max_length=100,blank=True,null=True)
    rate=models.CharField(db_column="rate",max_length=100,blank=True,null=True)
    comments=models.CharField(db_column="comments",max_length=100,blank=True,null=True)
class jingdong(models.Model):
    title=models.CharField(db_column="title",max_length=100,blank=True,null=True)
    price=models.CharField(db_column="price",max_length=100,blank=True,null=True)
    comment=models.CharField(db_column="comment",max_length=100,blank=True,null=True)
