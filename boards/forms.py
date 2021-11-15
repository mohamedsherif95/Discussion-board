from django import forms
from .models import Topic, Post


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5}),
        max_length=4000,
        help_text='max length is 4000 characters',
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class NewPostForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5}))

    class Meta:
        model = Post
        fields = ['message']