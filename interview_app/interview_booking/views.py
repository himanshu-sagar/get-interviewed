from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


class InterviewApp(View):
    def get(self, request):
        return render(request, template_name='main/index.html', context={})
