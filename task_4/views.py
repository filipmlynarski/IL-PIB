from django.views.generic import UpdateView

from .forms import EnterpriseForm


class enterprise_view(UpdateView):  # Class name should be PascalCase: 'EnterpriseView'
    # Missing docstring explaining view's purpose

    form_class = EnterpriseForm
    # Missing required attributes for UpdateView:
    # - template_name
    # - model or queryset
    # - success_url

    def get_context_data(self):  # Missing **kwargs parameter
        # Not calling super().get_context_data()
        # This means losing all default context data
        context = {
            "user": self.request.user,
        }
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs[
            "short_name"
        ] = self.get_object().short_name()  # short_name is property, not method
        return kwargs
