from .models import Recipe
from django import forms


class RecipeCreatForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name','detail','category','image']
        widgets ={
            'name':forms.TextInput(attrs={'class':'input'}),
            'detail':forms.Textarea(attrs={'class':'input','rows':10}),
            # 'category':forms.ChoiceField(),
            'image':forms.FileInput(attrs={'class':'file-input'}),
        }