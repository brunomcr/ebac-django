from django.http import HttpResponse
from django.views import generic


class Post(generic.View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Ola Python')
