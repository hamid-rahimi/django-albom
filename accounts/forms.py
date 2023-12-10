from django import forms as f
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

error_messages = {
    'required' : "پرکردن این فیلد الزامی است"
}

class UserAcountLoginForm(f.Form):
    username = f.CharField(widget=f.TextInput(
        attrs={'placeholder':"تلفن یا ایمیل",'class':"form-control"}), error_messages=error_messages, label="نام کاربری")
    
    password = f.CharField(widget=f.PasswordInput(
        attrs={'class':"form-control"}), error_messages=error_messages, label="رمز ورود")
    
class UserAccountRegisterForm(f.Form):
    first_name = f.CharField(label="نام", error_messages=error_messages, widget=f.TextInput(
        attrs={'class':"form-control", 'placeholder':"نام خود را وارد کنید..."}))
    
    last_name = f.CharField(label="نام خانوادگی", error_messages=error_messages, widget=f.TextInput(
        attrs={'class':"form-control", 'placeholder':"فامیلی خود را وارد کنید..."}))
    
    email = f.CharField(label="ایمیل", error_messages=error_messages, widget=f.EmailInput(
        attrs={'class':"form-control", 'placeholder':"ایمیل خود را وارد کنید..."}))
    
    username = f.CharField(label="نام کاربری", error_messages=error_messages, widget=f.TextInput(
        attrs={'class':"form-control", 'placeholder':"نام کاربری خود را وارد کنید..."}))
    
    password = f.CharField(label="رمز ورود", error_messages=error_messages, widget=f.PasswordInput(
        attrs={'class':"form-control", 'placeholder':"رمز ورود خود را وارد کنید..."}))
    
    password_2 = f.CharField(label="تکرار رمز ورود", error_messages=error_messages, widget=f.PasswordInput(
        attrs={'class':"form-control", 'placeholder':"دوباره رمز ورود خود را وارد کنید..."}))
    

    def clean(self):
        cleaned_data = super().clean()
        fname = cleaned_data.get('first_name')
        lname = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password_2 = cleaned_data.get('password_2')
        
        if len(fname) > 150:
            self.add_error('first_name',ValidationError('بزرگتر'))
            
        if len(lname) < 1:
            self.add_error('last_name',ValidationError('کوچکتر'))
            
        if ('@' not in email) or ('.' not in email):
            self.add_error('email',ValidationError('نامعتبر'))
            
        is_user_exists = User.objects.filter(username=username).exists()
        if is_user_exists:
            self.add_error('username',ValidationError('نام کاربری تکراری'))
            
        if password_2 != password:
            self.add_error('password_2',ValidationError('رمز ورود یکسان نیست'))

        return cleaned_data

    
    
    # def clean_last_name(self):
    #     data = self.cleaned_data.get('last_name')
    #     if (data):
    #         raise ValidationError('نام را بنویس')
    #     return data
    
    # def clean_email(self):
    #     data = self.cleaned_data.get('email')
    #     if is_none(data):
    #         raise ValidationError('نام را بنویس')
    #     return data
    
    # def clean_username(self):
    #     data = self.cleaned_data["username"]
    #     is_user_exists = User.objects.filter(username=data).exists()
    #     if is_user_exists:
    #         raise ValidationError("نام کاربری تکراری...")
    #     return data
    
    # def clean_first_name(self):
    #     data = self.cleaned_data["username"]
    #     if data:
    #         self.add_error('first_name', ValidationError('نام را بنویس'))
    #     return data

    # def clean_password_2(self):
    #     pass_1 = self.cleaned_data.get('password')
    #     pass_2 = self.cleaned_data.get('password_2')
    #     if pass_1 != pass_2:
    #         raise ValidationError('تکرار پسورد اشتباه...')
    #     return pass_2