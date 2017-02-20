from django.apps.AppConfig import get_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from ..services import get_identities_for_user


class DashboardView(LoginRequiredMixin, ListView):
    model = get_model("identity", "Identity")
    login_url = "/account/login/"
    template_name = "dashboard.html"

    def get_queryset(self, request):
        return get_identities_for_user(request.user)
