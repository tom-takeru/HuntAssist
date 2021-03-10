from django.views.generic import TemplateView
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.contrib import messages

from .models import EntrySheet, Category, Company

from .forms import InquiryForm, EntrySheetCreateForm

import logging

logger = logging.getLogger(__name__)

class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'


class InquiryView(FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('es_manager:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


class EntrySheetListView(LoginRequiredMixin, ListView):
    model = EntrySheet
    context_object_name = 'es_list'
    template_name = 'es_manager/es_list.html'
    paginate_by = 5

    def get_queryset(self):
        entry_sheets = EntrySheet.objects.filter(user_id=self.request.user).order_by('-created_at')
        return entry_sheets

class EntrySheetDetailView(LoginRequiredMixin, DetailView):
    model = EntrySheet
    template_name = 'es_manager/es_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = self.object.categories.all()
        context['company_list'] = self.object.companies.all()
        return context

class EntrySheetCreateView(LoginRequiredMixin, CreateView):
    model = EntrySheet
    template_name = 'es_manager/es_create.html'
    form_class = EntrySheetCreateForm
    success_url = reverse_lazy('es_manager:es_list')

    def form_valid(self, form):
        es = form.save(commit=False)
        es.user = self.request.user
        es.save()
        messages.success(self.request, 'エントリーシートを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "エントリーシートの作成に失敗しました。")
        return super().form_invalid(form)

class EntrySheetUpdateView(LoginRequiredMixin, UpdateView):
    model = EntrySheet
    template_name = 'es_manager/es_update.html'
    form_class = EntrySheetCreateForm

    def get_success_url(self):
        return reverse_lazy('es_manager:es_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, 'エントリーシートを更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'エントリーシートの更新に失敗しました。')
        return super().form_invalid(form)

class EntrySheetDeleteView(LoginRequiredMixin, DeleteView):
    model = EntrySheet
    template_name = 'es_manager/es_delete.html'
    success_url = reverse_lazy('es_manager:es_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'エントリーシートを削除しました。')
        return super().delete(request, *args, **kwargs)
