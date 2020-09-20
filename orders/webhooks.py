from django.http import HttpResponse


class StripeWebhookHandler:
    """Handles Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, request):
        """Handle a webhook event"""
        return HttpResponse(
            content=f'Webhook received: {event{"type"}}',
            status=200)
