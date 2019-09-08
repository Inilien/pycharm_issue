from myapp.forms import ContactForm
from django.views.generic.edit import FormView

SUBDIR = 'subdir/'


class CanResolve(FormView):
    template_name = 'resolve.html'
    form_class = ContactForm


class CanResolveSubdir(FormView):
    template_name = 'subdir/CanResolve.html'
    form_class = ContactForm


class CannotResolveSubdir(FormView):
    template_name = SUBDIR + 'CannotResolve.html'
    form_class = ContactForm

