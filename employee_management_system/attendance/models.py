from django.db import models
from employee.models import Employee
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, null=True , on_delete=models.SET_NULL)
    date = models.DateField(null=False)
    in_time = models.TimeField(null=False)
    out_time = models.TimeField(null=False)
    created_by = models.ForeignKey(User, null=True,
                                   related_name='attendance_created_by',
                                   on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(User, null=True,
                                    related_name='attendance_modified_by',
                                    on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    






