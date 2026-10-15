from django.shortcuts import render , redirect , get_object_or_404
from .models import Notice
# Create your views here.


def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author_name = request.POST.get('author_name')
        Notice.objects.create(title=title, content=content, author_name=author_name)
        return redirect('index')
    notices = Notice.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'notices': notices})

def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'notice_detail.html', {'notice': notice})
