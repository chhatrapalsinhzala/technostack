from .models import Employee
from django import forms

class CreateEmployeeForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = Employee
        fields =('id','first_name','last_name','phone','address')
        
    def __init__(self,*args, **kwargs):
            super(CreateEmployeeForm, self).__init__(*args, **kwargs)
            for form_field in self.fields.values():
                self.fields['first_name'].required = False
                self.fields['last_name'].required = False
                self.fields['email'].required = True
                self.fields['phone'].required = True
                self.fields['address'].required = True



