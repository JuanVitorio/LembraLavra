from django import forms
from .models import Word, Category, Languages

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Languages
        fields = '__all__'