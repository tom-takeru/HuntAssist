from django.views.generic import TemplateView
from django.views.generic import FormView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.contrib import messages

from .forms import InquiryForm

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

from .models import EntrySheet

class EntrySheetListView(LoginRequiredMixin, ListView):
    model = EntrySheet
    context_object_name = 'es_list'
    template_name = 'es_manager/es_list.html'
    paginate_by = 2

    def get_queryset(self):
        entry_sheets = EntrySheet.objects.filter(user_id=self.request.user).order_by('-created_at')
        return entry_sheets
