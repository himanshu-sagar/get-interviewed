from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


class InterviewApp(View):
    def get(self, request):
        return HttpResponse("Welcome to Interview Booking APP")

    def post(self, request):
        return HttpResponse("Your form is submitted successfully")
