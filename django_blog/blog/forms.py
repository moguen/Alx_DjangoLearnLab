from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment, Tag
from .widgets import TagWidget

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture')

class PostForm(forms.ModelForm):
    tags = forms.CharField(required = False, help_text='Enter tags seperated by commas')
    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'tags')

    def clean_tags(self):
        tag_string = self.cleaned_data['tags']
        tag_names = [name.strip() for name in tag_string.split(',') if name.strip()]
        return tag_names
    
    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        if instance.pk:
            instance.tags.clear()
            tag_names = self.cleaned_data['tags']
            for tag_name in tag_names:
                tag,_ = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)
        return instance

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].widget = TagWidget()
        self.fields['author'].queryset = User.objects.all()

#Comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter your comment here...'}),
        }

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 10:
            raise forms.ValidationError("Comment must be at least 10 characters long.")
        return content