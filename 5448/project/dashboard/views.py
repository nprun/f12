from django.http import HttpResponse


def index(request):
    return HttpResponse('{0}'.format(request.session.keys()))
