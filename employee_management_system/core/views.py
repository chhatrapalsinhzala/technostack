from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from rest_framework.authtoken import models as token_models
from .forms import LoginForm
from django.views.generic import TemplateView
from attendance.models import Attendance
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

# Common login for both employee and admin.
class LoginView(FormView):
    template_name = "index.html"
    title = "login"
    success_url =reverse_lazy('index')
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username = username,password=password)
        
        if user and user.is_staff:
            login(self.request,user)
            print("***** successfully Logged in as an admin......*****")
            token_instance = token_models.Token.objects.filter(user=user).last()
            if token_instance:
                token_instance.delete()
            token_instance, _ = token_models.Token.objects.get_or_create(user=user)
            print(token_instance)
            return redirect('employee/employee-list/')

        elif user and not user.is_staff:
            login(self.request,user)
            print("***** successfully Logged in as an employee......*****")
            token_instance = token_models.Token.objects.filter(user=user).last()
            if token_instance:
                token_instance.delete()
            token_instance, _ = token_models.Token.objects.get_or_create(user=user)
            print(token_instance)   
            attendance = Attendance.objects.create(
                employee = user.id,
                date = datetime.today().date(),
                in_time = datetime.now().time()
            )
            return redirect('/individual-attendence/')
            
        else:
            print("user doesnot exist..")
            return render(self.request,"landmark/login.html",{'form': form})
        return super(LoginView, self).form_valid(form)


def Logout(request):
    print(request.user)
    token_instance = token_models.Token.objects.filter(user=request.user).last()
    attendance = Attendance.objects.filter(
                employee = request.user.id,
                date = datetime.today().date(),
    )
    if attendance :
        attendance.out_time = datetime.now().time()
        attendance.save()
    else:
        print("there are no user logged in currently")
    logout(request)
    if token_instance:
        try:
            token_instance.delete()
        except:  # noqa
            pass
    return redirect('/login/')