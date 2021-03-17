from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Employee(models.Model):
    user = models.ForeignKey(User,related_name='employee_name',null=True, on_delete= models.SET_NULL)
    phone = models.CharField('Cell phone', max_length=20)
    address = models.TextField('Address', max_length=200,null=True, blank=True)
    
    def __str__(self):
        return str(self.id)

    def get_role(self):
        if self.user.is_superuser:
            return 'admin'
        else:
            return 'employee'



