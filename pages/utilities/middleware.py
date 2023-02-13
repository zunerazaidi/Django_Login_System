from django.shortcuts import HttpResponseRedirect


class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        redirect_url = '/login'
        if request.path == redirect_url:
            return self.get_response(request)

        response = self.get_response(request)
        if not request.user.is_authenticated: # in Django > 3 this is a boolean
            return HttpResponseRedirect(redirect_url)

        # Code to be executed for each request/response after
        # the view is called.

        return response
