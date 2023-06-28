from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField

from .models import Teacher, Student, TeacherProfile, Class, School


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentSearchForm(forms.Form):
    name_or_class = forms.CharField(max_length=50, required=False)


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['phone', 'class_rel', 'subject']


class RegisterForm(UserCreationForm):
    class Meta:
        model = Teacher
        fields = ('phone', 'password1', 'password2')


class BroadcastForm(forms.Form):
    message = forms.CharField(max_length=200, required=False)


class LoginForm(forms.Form):
    phone = PhoneNumberField()
    password = forms.CharField(widget=forms.PasswordInput)
