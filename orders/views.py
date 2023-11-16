from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

from common.mixins import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'orders/index.html'
    title = _('Main')


class AboutUsView(TitleMixin, TemplateView):
    template_name = 'orders/about.html'
    title = _('About us')
