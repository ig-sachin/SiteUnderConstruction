from django.shortcuts import HttpResponse
class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Call from Middleware before view")
        response = HttpResponse("This site is under construction")
        print("Call from Middleware after view")
        return response