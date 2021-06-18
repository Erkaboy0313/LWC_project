from django import forms

class Search(forms.Form):
    search = forms.CharField(label='', max_length=200 , widget=forms.TextInput(attrs={'class': 'search-box' , 'placeholder':'search'}))