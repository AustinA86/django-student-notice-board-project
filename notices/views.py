from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Notice
from .forms import NoticeForm

# SELECT: List all notices
class NoticeListView(ListView):
    model = Notice
    template_name = 'notices/notice_list.html'
    context_object_name = 'notices'
    ordering = ['-created_at']

# SELECT: View single notice
class NoticeDetailView(DetailView):
    model = Notice
    template_name = 'notices/notice_detail.html'

# INSERT: Create notice
class NoticeCreateView(LoginRequiredMixin, CreateView):
    model = Notice
    form_class = NoticeForm
    template_name = 'notices/notice_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# UPDATE: Edit notice (Author only)
class NoticeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notice
    form_class = NoticeForm
    template_name = 'notices/notice_form.html'
    success_url = '/'

    def test_func(self):
        notice = self.get_object()
        return self.request.user == notice.author

# DELETE: Remove notice (Author only)
class NoticeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notice
    template_name = 'notices/notice_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        notice = self.get_object()
        return self.request.user == notice.author

# AJAX CRUD (Update likes)
@login_required
def like_notice(request, pk):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        notice = get_object_or_404(Notice, pk=pk)
        if notice.liked_by.filter(id=request.user.id).exists():
            notice.liked_by.remove(request.user)
            liked = False
        else:
            notice.liked_by.add(request.user)
            liked = True
        return JsonResponse({'likes': notice.total_likes(), 'liked': liked})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def session_example_view(request):
    request.session['last_visit'] = 'You last visited the session page just now!'
    return render(request, 'notices/session_info.html')
