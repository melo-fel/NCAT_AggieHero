"""AggieHeroNCAT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import openai
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.views import View
from . import views

def chatbot_response(user_input):
    # Generate a response from GPT-3
    response = openai.Completion.create(engine="gpt-3.5-turbo", prompt=user_input, temperature=0.5, max_tokens=1024,
                                        top_p=1, frequency_penalty=0, presence_penalty=0)
    return response["choices"][0]["text"]

class ChatbotView(View):
    def post(self, request):
        user_input = request.POST["user_input"]
        response = chatbot_response(user_input)
        return HttpResponse(response)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index')
]
