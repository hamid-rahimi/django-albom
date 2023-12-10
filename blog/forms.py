from django import forms
from django.contrib.auth.models import User
from django_jalali.forms import forms as jforms
from django.contrib.admin import widgets
from blog.models import Person

error_messages = {
    'required': "این فیلد الزامی است..."
}


class CreateArticle(forms.Form):
    title = forms.CharField(max_length=250, error_messages=error_messages, label="عنوان مقاله",
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    text = forms.CharField(max_length=650, error_messages=error_messages, widget=forms.Textarea(
        attrs={'class': "form-control"}), label="متن مقاله")

    created_date = forms.DateField(label="تاریخ", required=False, widget=forms.DateInput(
        attrs={'class': "form-control"}))

    is_show = forms.BooleanField(required=False,label="نمایش داده شود؟", error_messages=error_messages,
                                 widget=forms.CheckboxInput(attrs={'class': "form-check-input"}))

    image = forms.ImageField(label="عکس", error_messages=error_messages, widget=forms.FileInput(
        attrs={'class': "form-control"}))

    # author = forms.ModelChoiceField(queryset=User.objects.all(), error_messages=error_messages,
    #                                 widget=forms.Select(attrs={'class': "form-control"}))


class AddPerson(forms.Form):
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': "form-control"}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    email = forms.EmailField(max_length=300, widget=forms.EmailInput(attrs={'class': "form-control"}))

class UpdateArticle(forms.Form):
    title = forms.CharField(max_length=250, error_messages=error_messages, label="عنوان مقاله",
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    text = forms.CharField(max_length=650, error_messages=error_messages, 
                           widget=forms.Textarea(attrs={'class': "form-control"}), label="متن مقاله")

    # created_date = forms.DateField(label="تاریخ", required=False, 
    #                                widget=forms.DateInput(attrs={'class': "form-control"}))

    is_show = forms.BooleanField(required=False,label="نمایش داده شود؟", error_messages=error_messages,
                                 widget=forms.CheckboxInput(attrs={'class': "form-check-input"}))

    image = forms.ImageField(label="عکس",required=False, error_messages=error_messages, 
                             widget=forms.FileInput(attrs={'class': "form-control"}))