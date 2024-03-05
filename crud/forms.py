from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя", help_text="Введите свое имя", min_length=2, max_length=20, required=True)
    age = forms.IntegerField(label="Ваш возраст?", help_text="Введите свой возраст", required=True)


class ContactForm(forms.Form):
    age = forms.IntegerField()
    nationality = forms.CharField()
    captcha_answer = forms.IntegerField(label='2 + 2', label_suffix=' = ')


class CommentForm(forms.Form):
    name = forms.CharField(initial='Ваше имя')
    url = forms.URLField(initial='http://')
    comment = forms.CharField()


class HelpTextContactForm(forms.Form):
    subject = forms.CharField(max_length=100, help_text='He более 100 символов')
    message = forms.CharField()
    sender = forms.EmailField(help_text='email адрес')
    cc_myself = forms.BooleanField(required=False)
