from django import forms
from .models import Employee,Course,Department,Book


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' 

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__' 

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__' 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__' 