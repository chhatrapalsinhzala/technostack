from .models import Employee
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from .forms import CreateEmployeeForm
from django.contrib import messages
from django.views.generic.list import ListView


# Create your views here.
class EmployeeList(ListView):
    """
    View for the list of all Employees
    """
    model = Employee
    template_name = "employee-list.html"
    queryset = Employee.objects.all().order_by("-id")
    context_object_name = "audit_references"


class EmployeeCreateView(FormView):
    """
    View to create Employee
    """
    
    model = Employee
    template_name = 'create-emp.html'
    queryset = Employee.objects.all().order_by()
    form_class = CreateEmployeeForm
    success_url = "/create_employee/"

    
    def form_valid(self, form):
        record = form.save()
        if record:
            
            messages.success(self.request, 'New Employee successfully created :-'+str(record.id))
        return super().form_valid(form)
    
    def get(self,request):
        
        if request.user.is_superuser:
            return render(request, "create-emp.html", {'form':self.form_class})
        else:
            return redirect('login')




class EmployeeUpdateView(FormView):
    def get(self, request, *args, **kwargs):
        
        if request.user.is_superuser:
            if "id" in kwargs:
                emp_ref = Employee.objects.filter(id = kwargs["id"]).first()
                
                emp_ref_dict = dict(first_name= emp_ref.user.first_name, last_name = emp_ref.user.first_name, id=emp_ref.pk,
                                email = emp_ref.user.email,phone=emp_ref.phone,address = emp_ref.address
                               )
                form = CreateEmployeeForm(initial= emp_ref_dict)
                return render(request, "update-emp.html", {'form':form,'id' :emp_ref.id })    
            else:
                form = CreateEmployeeForm()
                return render(request, "update-emp.html", {'form':form})    
        else:
            return redirect("login")

    def form_valid(self, form,**kwargs):
        form = form.cleaned_data
        emp_ref_id = self.request.POST['emp_ref_id']
        if emp_ref_id:
            emp_ref = Employee.objects.filter(id = emp_ref_id).last()
            
            try:
                form = CreateEmployeeForm(self.request.POST, instance=emp_ref)
                saved = form.save()
                if saved:
                    
                    messages.success(self.request, 'Record Updated')
            except Exception as e:
                raise e
        return redirect("/emp_list/")










