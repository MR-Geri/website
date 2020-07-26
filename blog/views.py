from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import *
from .forms import TagForm, PostForm


class Posts(generic.ListView):
    template_name = 'blog/blog.html'
    model = Post
    paginate_by = 2
    flag = False

    def get_queryset(self):
        queryset = super(Posts, self).get_queryset()
        self.q = self.request.GET.get("q")
        if self.q:
            self.flag = True
            return queryset.filter(Q(title__icontains=self.q) | Q(body__icontains=self.q))
        return queryset


class PostDetail(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = {'admin_object': self.object, 'detail': True}
        context.update(kwargs)
        return super().get_context_data(**context)


class PostCreate(LoginRequiredMixin, generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_update.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blog')
    template_name = 'blog/post_delete.html'
    raise_exception = True


class TagsList(generic.ListView):
    template_name = 'blog/tags_list.html'
    model = Tag


class TagDetail(generic.DetailView):
    model = Tag

    def get_context_data(self, **kwargs):
        context = {'admin_object': self.object, 'detail': True}
        context.update(kwargs)
        return super().get_context_data(**context)


class TagCreate(LoginRequiredMixin, generic.CreateView):
    form_class = TagForm
    template_name = 'blog/tag_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'blog/tag_update.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy('tags_list')
    template_name = 'blog/tag_delete.html'
    raise_exception = True
