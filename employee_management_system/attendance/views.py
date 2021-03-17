from django.shortcuts import render
from django.views.generic.list import ListView
from employee.models import Employee
from attendance.models import Attendance

# Create your views here.
class EmployeeList(ListView):
    template_name = "employee.html"
    title = "Employee"
    model = Employee
    context_object_name = 'employees'

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args,*kwargs)
    #     context['Attandence'] = Attendance.objects.values('category').order_by().annotate(Count('category'))
    #     context['order'] = {'get_cart_total': {'total_items': 0}}

    #     if self.request.user.is_authenticated:
    #         order_instance = Order.objects.filter(user=self.request.user, is_completed=False).last()
    #         if order_instance:
    #             context['order'] = order_instance
    #     return context