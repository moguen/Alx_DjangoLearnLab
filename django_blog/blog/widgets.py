from django.forms.widgets import TextInput

class TagWidget(TextInput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['class'] = 'form-control'

    def value_from_datadict(self, data, files, name):
        value = data.get(name)
        return [tag.strip() for tag in value.split(',') if tag.strip()]