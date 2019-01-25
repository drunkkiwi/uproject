from django                         import forms
from .models                        import AnswerPost
from .models                        import QuestionPost

class QuestionPostForm(forms.ModelForm):
    question_body = forms.CharField(max_length=10000, required=True, widget=forms.Textarea(attrs={'placeholder': 'Wanna ask a question?', 'onfocus': 'this.placeholder=""', 'onblur': 'this.placeholder="Wanna ask a question?"'}))

    class Meta:
        model = QuestionPost
        fields = ('question_body',)


class AnswerPostForm(forms.ModelForm):
    answer_body = forms.CharField(max_length=10000, required=True, widget=forms.Textarea(attrs={'placeholder': 'Wanna answer the question?', 'onfocus': 'this.placeholder=""', 'onblur': 'this.placeholder="Wanna answer the question?"'}))

    class Meta:
        model = AnswerPost
        fields = ('answer_body',)
