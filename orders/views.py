from django.views.generic import TemplateView

class OrdersPageView(TemplateView):
    template_name = "pages/orders.html"

