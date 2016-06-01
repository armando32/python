from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

from rest_framework import status
from rest_framework.decorators import api_view
from django.template import RequestContext
from rest_framework.response import Response
from blog.serializers import PostSerializer 
# Create your views here.


@api_view(['GET', 'POST'])
def PostList(request):
        """
        Create or list Posts
        """
        if request.method=='GET':
                post = Post.objects.all()
                serializer = PostSerializer(post, many=True)
                return Response(serializer.data)
        
        elif request.method=='POST':
                serializer = PostSerializer(data=request.DATA)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        
#return render_to_response('fileupload/upload.html', {'form': c['UploadFileForm']},  RequestContext(request))

def post_list(request):
	posts = Post.objects.filter(published_date__lte = timezone.now())
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.method == "POST" :
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
