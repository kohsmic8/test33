from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']   #유저한테 받는거는 models.py 에서 content 밖에 없으므로