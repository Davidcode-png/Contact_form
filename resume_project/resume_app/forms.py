from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=250)
    title = forms.CharField(max_length=200,default='')
    message = forms.TextField(default='')

    def __str__(self):
        return self.name