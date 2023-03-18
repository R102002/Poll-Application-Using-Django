from django.contrib.auth.models import User
from django.db import models
class Poll(models.Model):
    question=models.TextField()
    op1=models.CharField(max_length=40)
    op2=models.CharField(max_length=40)
    op3=models.CharField(max_length=40)
    op1c=models.IntegerField(default=0)
    op2c=models.IntegerField(default=0)
    op3c=models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def total(self):
        return self.op1c+self.op2c+self.op3c