from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


class IndexForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    uploaded_image = forms.ImageField()
