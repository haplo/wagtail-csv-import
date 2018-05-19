from django import forms
from django.utils.translation import ugettext as _

try:
    from wagtail.admin.widgets import AdminPageChooser
    from wagtail.core.models import Page
except ImportError:  # fallback for Wagtail <2.0
    from wagtail.wagtailadmin.widgets import AdminPageChooser
    from wagtail.wagtailcore.models import Page

class ImportFromFileForm(forms.Form):
    file = forms.FileField(label=_("File to import"))
    parent_page = forms.ModelChoiceField(
        queryset=Page.objects.all(),
        widget=AdminPageChooser(can_choose_root=True, user_perms='copy_to'),
        label=_("Destination parent page"),
        help_text=_("Imported pages will be created as children of this page.")
    )


class ExportForm(forms.Form):
    root_page = forms.ModelChoiceField(
        queryset=Page.objects.all(),
        widget=AdminPageChooser(can_choose_root=True),
    )
