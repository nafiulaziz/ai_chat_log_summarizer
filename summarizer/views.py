from django.shortcuts import render
from .forms import UploadChatForm
from .utils import parse_chat_log, summarize_chat

def upload_view(request):
    summary = None
    if request.method == 'POST':
        form = UploadChatForm(request.POST, request.FILES)
        if form.is_valid():
            file_obj = request.FILES['chat_file']
            user_msgs, ai_msgs, all_msgs = parse_chat_log(file_obj)
            summary = summarize_chat(user_msgs, ai_msgs, all_msgs)
    else:
        form = UploadChatForm()
    return render(request, 'summarizer/upload.html', {'form': form, 'summary': summary})
