from django import forms
from Chats.models import Text


class GetTxt(forms.ModelForm):
    # text = forms.TimeField(widget=forms.TextInput(attrs={'class':'container'}))
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'container', 'id': 'gra_txt'}), label='')

    class Meta:
        model = Text
        fields = ('text',)


class SearchForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'searchTerm',
                                                                         'placeholder': 'Search people'}))
    AGE_ANY = '0'
    AGE_UNDER_30 = '1'
    AGE_30_TO_50 = '2'
    AGE_ABOVE_50 = '3'
    AGE = [
        (AGE_ANY, 'Any age'),
        (AGE_UNDER_30, 'Until the 30'),
        (AGE_30_TO_50, '30 to 50'),
        (AGE_ABOVE_50, 'Above 50')
    ]
    age = forms.ChoiceField(label='age', choices=AGE, required=False, widget=forms.Select())

    def get_age(self):
        price_level = self.cleaned_data['age']
        if price_level == SearchForm.AGE_UNDER_30:
            return None, 30
        elif price_level == SearchForm.AGE_30_TO_50:
            return 30, 50
        elif price_level == SearchForm.AGE_ABOVE_50:
            return 50, None
        else:
            return None, None
