from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,UpdateView,DeleteView,CreateView
from .models import Post,Category
from django.urls import reverse_lazy


# class IndexPageView(ListView):
# 	model = Post
# 	template_name = 'index.html'


def indexPageView(request):
	posts = Post.objects.all()
	context = {
	"yangiliklar":posts
	}
	return render(request,'index.html',context) 



# class PostDetailPageView(DetailView):
# 	model = Post
# 	template_name = 'post_detail.html'


def postDetailPageView(request,post_id):
	post  = Post.objects.filter(id=post_id)
	ctx = {
	"yangilik":post[0]
	}
	return render(request,'post_detail.html',ctx)



def categoryPage(request,category_id):
	category = Category.objects.get(pk=category_id)
	posts = Post.objects.all().filter(category_id=category_id)
	ctx = {
	"category": category,
	"xabarlar": posts 
	} 
	return render(request,'category.html',ctx)



class PostUpdateView(UpdateView):
	model = Post
	fields = ('title', 'image','body')
	template_name = 'post_edit.html'
	success_url = reverse_lazy('index')


class PostDeleteView(DeleteView):
	model = Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('index') 


class PostCreateView(CreateView):
	model = Post
	template_name = 'post_create.html'
	fields = ('category','title', 'body', 'image',)
	success_url = reverse_lazy('index')
