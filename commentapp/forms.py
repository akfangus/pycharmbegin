from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

# 모델 만드는 작업을 했으면 mygration을 해줘야합니다.