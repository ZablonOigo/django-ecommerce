from django import forms
from .models import *

class Newform(forms.ModelForm):
    class Meta:
        model=Item
        fields=('category','name','description','price','image',)

        input_classes='w-full py-4 px-6 rounded-xl border'
        widget={
            'category':forms.Select(attrs={
            'class':input_classes
            }),
            'name':forms.TextInput(attrs={
            'class':input_classes
            }),
            'description':forms.Textarea(attrs={
            'class':input_classes
            }),
            'price':forms.TextInput(attrs={
            'class':input_classes
            }),
            'image':forms.FileInput(attrs={
            'class':input_classes
            }),
        }

class Updateform(forms.ModelForm):
    class Meta:
        model=Item
        fields=('name','description','price','image','is_sold')

        input_classes='w-full py-4 px-6 rounded-xl border'
        widget={
            'name':forms.TextInput(attrs={
            'class':input_classes
            }),
            'description':forms.Textarea(attrs={
            'class':input_classes
            }),
            'price':forms.TextInput(attrs={
            'class':input_classes
            }),
            'image':forms.FileInput(attrs={
            'class':input_classes
            }),
        }        