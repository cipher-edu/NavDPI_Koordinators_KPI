from django.contrib.auth import logout
from django.utils import timezone

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')

            if last_activity and (timezone.now() - last_activity).seconds > 3600:
                logout(request)

            request.session['last_activity'] = timezone.now()

        response = self.get_response(request)

        return response
