from django.views import View
from django.shortcuts import render


class AboutUs(View):
    def get(self, request):
        return render(self.request, 'pages/about_us.html')

