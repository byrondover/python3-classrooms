from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from rest_framework import filters, viewsets

from students import models, serializers

# Create your views here.

def index(request):
    template = loader.get_template('students/index.html')
    return HttpResponse(template.render(dict(), request))


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)