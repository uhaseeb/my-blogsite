from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment"
        }
        error_messages = {
            'user_name': {
                        'required': 'Please input this mandatory field',
                        'max_length': 'Please enter the shorter input'},
            'text': {
                'required': 'Please input this mandatory field',
                'max_length': 'Please enter the shorter input'}
        }
