from django.shortcuts import redirect
from django.urls import resolve


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        if request.path_info == '/Mpanel/':
            if request.COOKIES.get('ssid'):
                print('COOKIE')
            else:
                return redirect('/Mpanel/login')

        #redirect()
        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_request(request):
        return request
