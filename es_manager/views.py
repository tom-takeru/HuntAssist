from django.views.generic import TemplateView
from django.views.generic import FormView

from django.urls import reverse_lazy

from .forms import InquiryForm

import logging

logger = logging.getLogger(__name__)

class IndexView(TemplateView):
    template_name = 'index.html'

class InquiryView(FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('es_manager:inquiry')

    def form_vlaid(self, form):
        form.senf_email()
        logger.info('Inquiry sent by {}'.format(form.clianed_data['name']))
        return super().form_valid(form)