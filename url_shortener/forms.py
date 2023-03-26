from django import forms


class UrlForm(forms.Form):
    url = forms.URLField(label='Enter URL here', required=True)

    url.widget.attrs.update({'class': 'form-control', 'value': "http://"})
