from django.shortcuts import render, redirect
from .forms import UploadChatForm, UploadFileForm
from .utils import parse_chat_log, summarize_chat

def upload_view(request):
    summary = None
    if request.method == 'POST':
        form = UploadChatForm(request.POST, request.FILES)
        if form.is_valid():
            file_obj = request.FILES['chat_file']
            use_tfidf = form.cleaned_data.get('use_tfidf', False)
            user_msgs, ai_msgs, all_msgs = parse_chat_log(file_obj)
            summary = summarize_chat(user_msgs, ai_msgs, all_msgs, use_tfidf=use_tfidf)
            
               # Save summary to session (or another method)
            request.session['summary'] = summary
            return redirect('summary')  # Redirect to avoid re-POSTing
    else:
        form = UploadChatForm()
    return render(request, 'summarizer/upload.html', {'form': form, 'summary': summary})

def summary_view(request):
    summary = request.session.get('summary', None)
    return render(request, 'summarizer/summary.html', {'summary': summary})
