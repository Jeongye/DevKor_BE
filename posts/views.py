from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from .models import Post

# Create your views here.
def index(request):
    if request.method == 'GET':
        return JsonResponse({'req_method': 'get'}, status=200)
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        date = timezone.localtime()
        new_post = request.POST.objects.create(title=title, content=content, date=date)
        return JsonResponse({'req_method': 'post'}, status=200)
    else:
        return JsonResponse({'error': 'request method not allowed'}, status=405)
    # return HttpResponse("aaaa")

def post(request, post_id):
    get_object_or_404(Post, id=post_id)
    post = request.Post.objects.get(pk=post_id)
    if request.method == 'GET':
        data = {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'date': post.date,
        }
        return JsonResponse(data, status=200)
    
    if request.method == 'POST':
        for key, value in request.POST.items():
            setattr(post, key, value)
        post.save()
        return JsonResponse({"update": "updated the post"}, status=200)
    
    if request.method == 'DELETE':
        post.delete()
        return JsonResponse({"delete": "deleted the post"}, status=200)