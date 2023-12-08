from django import forms

class GenreForm(forms.Form):
    genres = forms.ChoiceField(label='Géneros', choices=[], required=False)

