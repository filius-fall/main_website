from django import forms
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from .models import Post




# Create your views here.
# def home(request):

#     posts = Post.objects.all()
#     user = User.objects.filter(username='sreeram').first()
#     for i in posts:
#         if i.author == user:
#             date = i.date_post
#             f_date = date.strftime("%H-%m-%d, %Y")

#     context = {
#         'test_data':posts
#     }
#     return render(request,'blog/blog.html',context)


class PostListView(ListView):
    model = Post
    template_name='blog/blog.html'
    context_object_name='test_data'
    ordering = ['-date_post']

class PostDetailView(DetailView):
    model = Post


class CreateForm(forms.ModelForm):
    """
        This Class is model for forms that will be used in the create form.
        I created this form to add clases to forms manually.
    """
    class Meta:
        model = Post
        fields = ('title','content','banner_image')
        widgets = {
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
        }

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = CreateForm

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = CreateForm

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request,'blog/about.html')