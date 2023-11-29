from django.contrib.auth import logout
from django.utils import timezone

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity_str = request.session.get('last_activity')

            if last_activity_str:
                last_activity = timezone.datetime.strptime(last_activity_str, '%Y-%m-%d %H:%M:%S.%f%z')
                if (timezone.now() - last_activity).seconds > 3600:
                    logout(request)

            # Serialize the current datetime as a string
            request.session['last_activity'] = timezone.now().strftime('%Y-%m-%d %H:%M:%S.%f%z')

        response = self.get_response(request)

        return response
