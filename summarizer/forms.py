from django import forms

class UploadChatForm(forms.Form):
    chat_file = forms.FileField(label='Upload Chat Log (.txt)')
class UploadFileForm(forms.Form):
    chat_file = forms.FileField(label='Upload Chat Log (.txt)')
