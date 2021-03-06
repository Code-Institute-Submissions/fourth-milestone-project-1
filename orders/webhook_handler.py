from django.http import HttpResponse


# Webhook code largely taken from Boutique Ado course content
class StripeWebhookHandler:
    """Handles Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle a generic webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded_event(self, event):
        """Handle a payment_intent.succeeded webhook event"""
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed_event(self, event):
        """Handle a payment_intent.payment_failed webhook event"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
