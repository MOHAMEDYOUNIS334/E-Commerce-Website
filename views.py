import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_payment_intent(request):
    try:
        intent = stripe.PaymentIntent.create(
            amount=1000,  # بالسنت
            currency='usd',
            payment_method_types=['card'],
        )
        return JsonResponse({'client_secret': intent.client_secret})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)      